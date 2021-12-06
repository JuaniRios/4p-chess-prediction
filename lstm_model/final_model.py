import warnings
import os

import numpy as np
import pandas as pd
from sklearn.utils import class_weight
from tensorflow import keras
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Input, Dense, Embedding, LSTM, SpatialDropout1D, Dropout
from tensorflow.keras.models import Sequential, Model
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

    if not os.path.exists("./data_set.h5"):
        txt_to_h5("data_set.txt")

    df = pd.read_hdf("./data_set.h5", where=f'"player" = {players_list}')
    return df


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
        # TODO: create some kind of proper error for giving the wrong amount of games // do we want it or not?
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

    # TODO: put most common parameters in a dictionary so we dont need to push them around with returns in functions
    n_most_common_words = 6000

    # tokenize
    tokenizer = Tokenizer(num_words=n_most_common_words, lower=False, split=" ")
    tokenizer.fit_on_texts(X_train.iloc[:, 0].values)
    X_train_seq = tokenizer.texts_to_sequences(X_train.iloc[:, 0].values)

    word_index = tokenizer.word_index
    print('Found %s unique tokens.' % len(word_index))

    X_train = pad_sequences(X_train_seq, maxlen=max_len)

    return X_train, tokenizer, word_index


def get_class_weights(y_train):
    '''
    Get class weights to combat imbalance issues with predictions

    :param y_train:
    :return:
    '''

    y_ints = [y.argmax() for y in y_train]

    class_weights = class_weight.compute_class_weight(class_weight='balanced', classes=np.unique(y_ints), y=y_ints)
    class_weights = dict(enumerate(class_weights))

    return class_weights


def train_model(X_train, y_train, class_weights, word_index, max_len):
    '''
    Running the algorithm to train the model.

    :param X_train: Independent variables
    :param y_train: dependent variable
    :param class_weights:   class weights
    :param word_index:  lookup table/word dictionary for creation of word embedding layer
    :param max_len: max length of word embedding layer input
    :param X_test:  OPTIONAL
    :param y_test:
    :return:

    '''

    # Setting parameters for model
    epochs = 7
    emb_dim = 50
    batch_size = 32

    # Running model
    inp = Input(shape=(max_len))
    embed = Embedding(len(word_index) + 1, emb_dim)(inp)
    spatiald = SpatialDropout1D(0.4)(embed)
    LSTM_Layer_1 = LSTM(64, dropout=0.3, return_sequences=False)(spatiald)
    dense_layer_final = Dense(3, activation='softmax')(LSTM_Layer_1)
    model = Model(inputs=inp, outputs=dense_layer_final)

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['acc'])

    history = model.fit(x=X_train,
                        y=y_train,
                        epochs=epochs,
                        class_weight=class_weights,
                        batch_size=batch_size,
                        callbacks=[EarlyStopping(monitor='val_loss', patience=4, min_delta=0.0001)])

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
    for mov in player_moves:
        seq = tokenizer.texts_to_sequences(mov)
        padded = pad_sequences(seq, maxlen=max_len)
        padded = padded.reshape(1, -1)
        preds.append(model.predict(padded))

    return preds


def finalize_model(players, n_rounds):
    max_len = 22
    data = read_data(players)

    X, labels = data_preprocessing(data, players, n_rounds)

    weights = get_class_weights(labels)

    X, tokenizer, word_index = embedding_presets(X, max_len)

    model = train_model(X, labels, weights, word_index, max_len)

    return model, tokenizer, max_len


def interface_call(players, moves, n_moves):
    # TODO: Connect so that in UI we call this function from module "ml_model.py"
    '''
    Function to start the pipeline:
        1. Create evaluation model
        2. Finalize model
        3. returns the predictions in the correct format

    :param players:
    :param user_color:
    :return:
    '''

    final_model, tokenizer, max_len = finalize_model(players, n_moves)

    predictions = model_predict(final_model, moves, tokenizer, max_len)

    return predictions
