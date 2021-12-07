import pytest
import pandas as pd
import numpy as np
import tensorflow
from final_model import *


@pytest.fixture
def data():
    players_list = ["SirMullih", "Cha_ChaRealSmooth", "rojitto"]
    n_rounds = 5
    max_len = 22

    df = read_from_hdf(players_list, "../data_set.h5")
    X_df, labels = data_preprocessing(df, players_list, n_rounds)
    weights = get_class_weights(labels)
    X, tokenizer, word_index = embedding_presets(X_df, max_len)
    model = train_model(X, labels, weights, word_index, max_len)

    return players_list, n_rounds, max_len, df, X_df, X, labels, weights, word_index, tokenizer, model


@pytest.fixture
def moves():
    move_list = [["h2-h3 b7-c7 m9-l9"],
             ["Ne1-f3 Qa7-b7 m8-l8"],
             ["Qg1-k5 Na5-c6 Qn8-m8"],
             ["Bi1-h2 Qb7-d9 Nn5-l6"],
             ["Nj1-i3 b11-d11 Qm8-l7"]]

    return move_list

def test_read_from_hdf(data):
    players_list, n_rounds, max_len, df, X_df, X, labels, weights, word_index, tokenizer, model = data

    df = read_from_hdf(players_list, "../data_set.h5")

    # testing that data only includes data from 3 players and that they are the correct players
    assert len(df.player.unique()) == 3
    assert all(e in list(df.player.unique()) for e in players_list)

    # testing integrity of data types and number of columns
    assert len(df.columns) == 5
    assert all(e.type == np.object_ for e in df.dtypes)


def test_data_preprocessing(data):
    players_list, n_rounds, max_len, df, X_df, X, labels, weights, word_index, tokenizer, model = data

    X, labels = data_preprocessing(df, players_list, n_rounds)

    # testing output integrity
    assert labels.dtype == 'float32'
    assert type(X) == pd.core.frame.DataFrame
    assert len(X.columns) == 1



def test_get_class_weights(data):
    players_list, n_rounds, max_len, df, X_df, X, labels, weights, word_index, tokenizer, model = data


    weights_test = get_class_weights(labels)

    assert type(weights_test) == dict
    assert len(weights_test) == 3


def test_embedding_presets(data):

    players_list, n_rounds, max_len, df, X_df, X, labels, weights, word_index, tokenizer, model = data

    x_len = len(X) # for checking that the same amount of data leaves the tested function


    X_test, tokenizer, word_index_test = embedding_presets(X_df, max_len)

    # testing that word_index is a dictionary and that it is not empty
    assert type(word_index_test) == dict
    assert len(word_index_test) != 0
    assert type(X_test) == np.ndarray
    assert len(X_test) == x_len



def test_split_player(moves):
    move_list = moves

    final_moves = split_player(move_list)

    assert type(final_moves) == list
    assert len(final_moves) == 3
    # check string type
    assert all(type(x[0]) == str for x in final_moves)

    return final_moves


def test_model_predict(data, moves):
    players_list, n_rounds, max_len, df, X_df, X, labels, weights, word_index, tokenizer, model = data
    move_list = moves


    predictions = model_predict(model, move_list, tokenizer, max_len)

    #check that list type is ndarray
    assert all(type(x) == np.ndarray for x in predictions)

    #test that all predictions contain 3 values that are less than 1
    assert all(len(x[0]) == 3 for x in predictions)
    assert all(all(i < 1) for x in predictions for i in x)