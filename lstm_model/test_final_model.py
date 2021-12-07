import pytest
import pandas as pd
import numpy as np
from final_model import *

@pytest.fixture
def data():
    players_list = ["SirMullih", "Cha_ChaRealSmooth", "rojitto"]
    n_rounds = 5
    max_len = 22
    return players_list, n_rounds, max_len

@pytest.fixture
def moves():
    move_list = [["h2-h3 b7-c7 m9-l9"],
             ["Ne1-f3 Qa7-b7 m8-l8"],
             ["Qg1-k5 Na5-c6 Qn8-m8"],
             ["Bi1-h2 Qb7-d9 Nn5-l6"],
             ["Nj1-i3 b11-d11 Qm8-l7"]]

    return move_list


@pytest.fixture
def test_get_data(data):
    players_list, n_rounds, max_len = data
    df = read_data(players_list)

    # testing that data only includes data from 3 players and that they are the correct players
    assert len(df.player.unique()) == 3
    assert all(e in list(df.player.unique()) for e in players_list)

    # testing integrity of data types and number of columns
    assert len(df.columns) == 5
    assert all(e.type == np.object_ for e in df.dtypes)
    return df

@pytest.fixture
def test_data_preprocessing(data, test_get_data):
    players_list, n_rounds, max_len = data
    df = test_get_data

    X, labels = data_preprocessing(df, players_list, n_rounds)

    # testing output integrity
    assert labels.dtype == 'float32'
    assert type(X) == pd.core.frame.DataFrame
    assert len(X.columns) == 1

    return X, labels

@pytest.fixture
def test_get_class_weights(test_data_preprocessing):
    X, labels = test_data_preprocessing
    weights = get_class_weights(labels)

    assert type(class_weights) == dict
    assert len(class_weights) == 3

    return class_weights

@pytest.fixture
def test_embedding_presets(data, test_data_preprocessing):
    players_list, n_rounds, max_len = data
    X, labels = test_data_preprocessing
    x_len = len(X) # for checking that the same amount of data leaves the tested function


    X, tokenizer, word_index = embedding_presets(X, max_len)

    # testing that word_index is a dictionary and that it is not empty
    assert type(word_index) == dict
    assert len(word_index) != 0
    assert type(X) == np.ndarray
    assert len(X) == x_len

    return X, tokenizer, word_index


@pytest.fixture
def test_train_model(data, test_data_preprocessing, test_embedding_presets, test_get_class_weights):

    players_list, n_rounds, max_len = data
    X_depr, labels = test_data_preprocessing
    X, tokenizer, word_index = test_embedding_presets
    class_weights = test_get_class_weights


    model = train_model(X, labels, weights, word_index, max_len)

    # testing that model compile was complete
    assert type(model) == tensorflow.python.keras.engine.functional.Functional

    return model, tokenizer

def test_split_player(moves):
    move_list = moves

    final_moves = split_moves(move_list)

    assert type(final_moves) == list
    assert len(final_moves) == 3
    # check string type
    assert all(type(x[0]) == str for x in final_moves)

    return final_moves


def test_model_predict(data, test_train_model):
    players_list, n_rounds, max_len = data
    final_model, tokenizer = test_train_model
    list_moves = test_split_player


    predictions = model_predict(final_model, list_moves, tokenizer, max_len)

    #check that list type is ndarray
    assert all(type(x) == np.ndarray for x in predictions)

    #test that all predictions contain 3 values that are less than 1
    assert all(len(x[0]) == 3 for x in predictions)
    assert all(all(i < 1) for x in predictions for i in x)

    return
