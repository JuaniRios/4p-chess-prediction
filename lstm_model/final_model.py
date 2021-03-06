import warnings
import os

import numpy as np
import pandas as pd
from sklearn.utils import class_weight
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Input, Dense, Embedding, LSTM, SpatialDropout1D
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical

from data_cleaning.main import txt_to_h5


def warn(*args, **kwargs):
    pass
warnings.warn = warn



def read_data(players_list):
    '''
    Read data from hdf with a query that returns data only of those players in the players_list,
    so there is no need to read the whole dataset.'

    :param players_list: list of players in the game
    :return: dataframe with data of 3 players
    '''

    # if the .h5 does not exist, create the file from .txt file (one time)
    if not os.path.exists("./data_set.h5"):
        txt_to_h5("data_set.txt")

    fpath = "./data_set.h5"
    df = read_from_hdf(players_list, fpath)
    return df

def read_from_hdf(players_list, fpath):
    df = pd.read_hdf(fpath, where=f'"player" = {players_list}')
    return df


def split_player(moves):
    '''
    Change the moves of move inputs from user in the UI to the correct format accepted by the model
    :params moves: list of lists of string of moves for each round
    '''
    player_moves = {0: [], 1: [], 2: []}

    for m in moves:
        list_moves = m[0].split(" ")
        for i, move in enumerate(list_moves):
            player_moves[i] += [move]

    player_moves = list(player_moves.values())
    output = [[" ".join(x)] for x in player_moves]

    return output


def data_preprocessing(dataframe, players, n_rounds):
    '''
    Creates categorical encoding for the dependent variable based on
    the number of rounds played so far in the game"n_rounds".


    :param dataframe: Dataframe to preprocess
    :param players: list of players in the game
    :param n_rounds: number of rounds we are making the prediction on
    :return: X,independent variable with n_rounds number of moves,
             y, dependent variable y with player names
             labels, categorically encoded dependent variable
    '''
    # Set players as categories for LSTM
    df_temp = dataframe.copy()
    df_temp.y = 0
    df_temp.loc[df_temp.player == players[0], 'y'] = 0
    df_temp.loc[df_temp.player == players[1], 'y'] = 1
    df_temp.loc[df_temp.player == players[2], 'y'] = 2

    df_temp["y"] = df_temp["y"].astype("int")
    labels = to_categorical(df_temp["y"], num_classes=3)

    # selecting the correct column based whether user has entered 5,10,15 or 20 moves to moves list
    # for prediction.
    try:
        if n_rounds == 5:
            X = df_temp[["moves_5"]]
            y = df_temp["y"]
        elif n_rounds == 10:
            X = df_temp[["moves_10"]]
            y = df_temp["y"]
        elif n_rounds == 15:
            X = df_temp[["moves_15"]]
            y = df_temp["y"]
        elif n_rounds == 20:
            X = df_temp[["moves_20"]]
            y = df_temp["y"]
    except:
        print("Wrong amount of moves given.")
        raise

    return X, labels


def embedding_presets(X_train, max_len):
    '''
    Creating embeddings for the data.

    Two possibilities:
        If we only provide the X_train, we are building the final model,
        but if X_test is provided we are running the algorithm with train/test split.


    :param X_train: Data we are training the model on
    :param X_test: OPTIONAL; data the model is tested on.
    :return:
    '''

    n_most_common_words = 6000

    # tokenize the words. This is to represent the strings as numerical format
    tokenizer = Tokenizer(num_words=n_most_common_words, lower=False, split=" ")
    tokenizer.fit_on_texts(X_train.iloc[:, 0].values)
    X_train_seq = tokenizer.texts_to_sequences(X_train.iloc[:, 0].values)

    # create word dictionary
    word_index = tokenizer.word_index
    print('Found %s unique tokens.' % len(word_index))

    #pad the sequences to pre-defined length
    X_train = pad_sequences(X_train_seq, maxlen=max_len)

    return X_train, tokenizer, word_index



def get_class_weights(y_train):
    '''
    Get class weights to combat imbalance issues with predictions

    :param y_train:
    :return class_weights: a dictionary of class weights
    '''

    y_ints = [y.argmax() for y in y_train]

    # use the class_weight module from sklearn.utils to calculate class weights
    class_weights = class_weight.compute_class_weight(class_weight='balanced', classes=np.unique(y_ints), y=y_ints)
    class_weights = dict(enumerate(class_weights))

    return class_weights


def train_model(X_train, y_train, word_index, max_len, class_weights=None):
    '''
    Running the algorithm to train the model.

    :param X_train: Independent variables
    :param y_train: dependent variable
    :param class_weights:   class weights
    :param word_index:  lookup table/word dictionary for creation of word embedding layer
    :param max_len: max length of word embedding layer input
    :param X_test:  OPTIONAL
    :param y_test:
    :return: Returns the trained model object
    '''

    # Setting parameters for model
    epochs = 7
    emb_dim = 50
    batch_size = 32

    # Building the infrastructure for the model
    inp = Input(shape=(max_len)) # define the input shape for training data
    embed = Embedding(len(word_index) + 1, emb_dim)(inp) # define the word dictionary and embedding dimension parameters
    spatiald = SpatialDropout1D(0.4)(embed) # spatial Dropout to prevent overfitting and reduce generalization error
    LSTM_Layer_1 = LSTM(64, dropout=0.3, return_sequences=False)(spatiald)
    dense_layer_final = Dense(3, activation='softmax')(LSTM_Layer_1) # using softmax function to change to probabilities
    model = Model(inputs=inp, outputs=dense_layer_final) # define the inputs and outputs

    # defining error metrics for training
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['acc'])

    # starting the algorithm to train the model
    history = model.fit(x=X_train,
                        y=y_train,
                        epochs=epochs,
                        class_weight=class_weights,
                        batch_size=batch_size,
                        callbacks=[EarlyStopping(monitor='loss', patience=4, min_delta=0.0001)])

    return model


def model_predict(model, player_moves, tokenizer, max_len):
    '''
    use model to get predictions.

    :param model: trained finalized model
    :param player_moves: moves list from UI
    :param tokenizer: tokenizer to make sure we use the same word index for unseen data
    :param max_len:
    :return: returns list of list of predictions
    '''

    preds = []

    # for each player set of moves, tokenize the strings and use predict() function to append predictions
    for mov in player_moves:
        seq = tokenizer.texts_to_sequences(mov)
        padded = pad_sequences(seq, maxlen=max_len)
        padded = padded.reshape(1, -1)
        preds.append(model.predict(padded))

    return preds


def finalize_model(players, n_rounds):
    '''
    Builds the pipeline of functions for the algorithm to train the model.
        1. Query player data from .h5
        2. Preprocess data
        3. Get class weights to fix possible imbalanced classes
        4. Tokenize the moves from data
        5. Train the model

        :param players: list of players in game
        :param n_rounds: number of rounds with what to predict
    '''

    max_len = 22

    data = read_data(players)
    X, labels = data_preprocessing(data, players, n_rounds)
    weights = get_class_weights(labels)
    X, tokenizer, word_index = embedding_presets(X, max_len)
    if len(weights) == 3:
        model = train_model(X, labels, word_index, max_len, weights)
    else:
        model = train_model(X, labels, word_index, max_len)

    return model, tokenizer, max_len


def interface_call(players, moves, n_moves):
    try:
        '''
        Function to start the pipeline:
            1. Finalize model
            2. Edit the moves added by user to a correct format for the model
            3. Start prediction function that returns the predictions to the UI
    
        :param players: list of players in the game
        :param user_color: The color user is playing
        :return:
        '''

        final_model, tokenizer, max_len = finalize_model(players, n_moves)
        list_moves = split_player(moves)
        predictions = model_predict(final_model, list_moves, tokenizer, max_len)

        return predictions

    except Exception as ER:
        print(ER)
