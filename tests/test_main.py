import os

import pytest
import UI.main
from PyQt5 import QtCore

#### PROBLEM still is that the dialog is opening, we have to simulate that somehow.
#### Will try with a new qt bot widget for tha dialog window.
#### Maybe change the fixture to make the object have more.
list_all_players_available = UI.main.get_player()
@pytest.fixture
def players():
    players = ["empty_K3", "sumat777", "vrdtmr"]

    return players

@pytest.fixture
def app(qtbot):
    ui = UI.main.UiMainWindow()
    qtbot.addWidget(ui)

    return ui

@pytest.fixture
def moves():
    sample_moves = "h2-h3 b7-c7 m9-l9,Ne1-f3 Qa7-b7 m8-l8,Qg1-k5 Na5-c6 Qn8-m8,Bi1-h2 Qb7-d9 Nn5-l6,Nj1-i3 b11-d11 Qm8-l7"
    return sample_moves

# making a fixture with information when trying some function on the second window
@pytest.fixture
def app_with_info(qtbot):
    ui = UI.main.UiMainWindow()
    qtbot.addWidget(ui)
    players = ["empty_K3", "sumat777", "vrdtmr"]
    ui.player1.setText(players[0])
    ui.player2.setText(players[1])
    ui.player3.setText(players[2])
    ui.opponents = [ui.player1, ui.player2, ui.player3]
    ui.user_color = "Yellow"
    ui.window2()

    return ui

#
# #CONFIRMWINDOW
# @pytest.fixture
# def dialog(qtbot):
#     dialog = main.ConfirmDialog(["Mzambe", "Rasen555", "rook6431"], "Yellow")
#     qtbot.addWidget(dialog)
#
#     return dialog



def test_label_first_window(app, players):
    """
    Checking the first window, that some of the labels are there, we are checking that the input fields
    are empty before inserting, then we are trying to add one and checking that the label is that.
    :param app:
    :param players:
    :return:
    """
    assert app.label_inserting_p1.text() == "Player 1"
    assert app.label_inserting_p2.text() == "Player 2"
    assert app.player1.text() == ""
    app.player1.setText(players[0])
    assert app.player1.text() == "empty_K3"

def test_get_info_about_game_confirm(app, qtbot, players):
    """
    We are testing when the user have put in the data about opponents and the users color
    that we are coming into the dialog window and then after confirmation we are accessing
    the window 2. There we are checking that the players are inserted in the list opponents
    as well as checking that the user color is deleting for the visualisation list.
    :param app:
    :param qtbot:
    :param players:
    :return:
    """
    app.player1.setText(players[0])
    app.player2.setText(players[1])
    app.player3.setText(players[2])

    app.comboBox.setCurrentText("Yellow")
    qtbot.mouseClick(app.submit_button, QtCore.Qt.LeftButton)
    # here we have to simulate that we presses confirm!
    # and make a case if they press cancel also.



    # we have to add the

    assert app.opponents == [app.player1.text(), app.player2.text(), app.player3.text()]
    assert app.user_color != "Red"
    assert app.user_color == "Yellow"
    # making sure that the visualisation is not having yellow.
    assert "Yellow" not in app.colors
    # Checking that we come to window 2
    assert app.add_moves_button.text() == "Add moves"
    assert app.label_when_wrong.text() == ""

def test_get_info_about_game_cancel(app, qtbot, players):
    """
    Here we are simulation that the user is inserting data wrongly with two of the same players
    twice, so then is should not lead to the confirm window. Then he should see a new label stating
    what he might have done wrong and he has to retry.

    """
    app.player1.setText(players[0])
    app.player2.setText(players[0])
    app.player3.setText(players[2])
    app.comboBox.setCurrentText("Yellow")
    qtbot.mouseClick(app.submit_button, QtCore.Qt.LeftButton)

    # Making sure we are still on the first window.
    assert app.label_inserting_p1.text() == "Player 1"
    assert app.label_inserting_p2.text() == "Player 2"
    # checking that the players did not get saved in the opponents list.
    assert app.opponents == None
    assert app.player1.text() == ""
    # Checking that the info label is showing that something went wrong.
    assert app.label_when_wrong.text() == "Ooops something is wrong, check spelling and that there is different players."


def test_window2(app_with_info, qtbot):
    """
    We are testing the window2 that we are accessing it. we are checking that three players
    are set as labels for visualisation as well we are checking that the right color is there.
    We are checking that there is no data in history field.
    :param app:
    :param qtbot:
    :param players:
    :return:
    """
    app = app_with_info

    # checking that the labels 2,5,8 for now is player 1
    assert app.label_2.text() and app.label_5.text() and app.label_8.text() == app.player1.text()
    # checking that the other are not player one from start.
    assert app.label_3.text() != app.player1.text()
    assert app.historyText.toPlainText() == ""

def test_opponents_color(app_with_info, qtbot):
    """
    Checking that when the user submits the color, that we are deleting it from the list
    so that we later can see the visualisation of the other three colors.
    :param app:
    :param qtbot:
    :param players:
    :return:
    """
    app = app_with_info

    # checking that the users color gets deleted before the visualisation windows.
    assert "Yellow" not in app.colors

def test_add_moves(app_with_info, qtbot):
    """
    We are checking that when the user is adding the right moves it is coming into the history field
    and when he is putting in the wrong format, it is not added to the field. we are also checking that
    the moves inserted is getting into the prediction list which later on will be sent to the prediction
    tool. After pressing add moves, we are always adding a comma to later split it.
    :param app:
    :param qtbot:
    :param players:
    :return:
    """
    app = app_with_info
    try_move1 = "a1-a2 a1-a2 a1-a2"
    try_move2 = "a1-a2 Qf5-Qd3 0"
    # testing if we are adding a really wrong move
    try_move3 = "aqw2-Qw2 0 wkd-w"
    assert app.label_2.text() == app.player1.text()
    assert app.predict_pushbutton.text() == "predict"
    app.add_moves_lineedit.setText(try_move1)
    qtbot.mouseClick(app.add_moves_button, QtCore.Qt.LeftButton)

    # checking that after adding a move it is coming into the history field, where we add a comma.
    assert app.historyText.toPlainText() == try_move1+","

    # what is happening with the history window when entering more moves.
    app.add_moves_lineedit.setText(try_move2)
    qtbot.mouseClick(app.add_moves_button, QtCore.Qt.LeftButton)
    assert app.historyText.toPlainText() == try_move1+"," + try_move2+","

    # checking what is happening when entering a wrong move.
    # that is not added to the history text
    app.add_moves_lineedit.setText(try_move3)
    qtbot.mouseClick(app.add_moves_button, QtCore.Qt.LeftButton)
    assert app.historyText.toPlainText() != try_move3+","
    assert app.historyText.toPlainText() == try_move1+"," + try_move2+","
    # checking that the list of lists is updated!
    assert app.moves_list_prediction == [[try_move1], [try_move2]]
    assert app.moves_list_prediction != [[try_move1], [try_move2], [try_move3]]

def test_change_history(app_with_info, qtbot):
    """
    Here we are checking when there is something in the history field and the user
    would like to correct it, we are checking what the button is called, we are checking
    that the data is changed after the confirmation of changing the data.

    :param app:
    :param qtbot:
    :param players:
    :return:
    """
    app = app_with_info
    try_move1 = "a1-a2 a1-a2 a1-a2"
    try_move2 = "a1-a2 Qf5-Qd3 0"

    # adding a move
    app.add_moves_lineedit.setText(try_move1)
    qtbot.mouseClick(app.add_moves_button, QtCore.Qt.LeftButton)

    # checking that the moves are in the history
    assert app.historyText.toPlainText() != try_move1+"," + try_move2+","
    assert app.historyText.toPlainText() == try_move1+","
    # checking that the button is called change history
    assert app.change_history_button.text() == "Change history"
    qtbot.mouseClick(app.change_history_button, QtCore.Qt.LeftButton)
    # checking that after we click we are having button called confirm changes
    assert app.change_history_button.text() == "confirm changes"
    # changing the history
    app.historyText.setText(try_move1+"," + try_move2+",")

    qtbot.mouseClick(app.change_history_button, QtCore.Qt.LeftButton)
    # checking that we saved the data
    assert app.change_history_button.text() == "Change history"
    assert app.historyText.toPlainText() == try_move1+"," + try_move2+","
    assert app.historyText.toPlainText() != try_move1+","

def test_predict_button(app_with_info, qtbot, moves):
    """
    We are testing the predict button, we are first checking we have players on the second window,
    then we are checking that we have a list of lists of moves to send, and then that we get in return
    the list of list of predicted player and the percentage.

    :param app_with_info:
    :param qtbot:
    :return:
    """
    app = app_with_info
    # checking that the players are on the page
    assert app.player1.text() == app.label_2.text() == app.label_5.text() == app.label_8.text()
    assert app.player2.text() == app.label_3.text() == app.label_6.text() == app.label_9.text()
    assert app.player3.text() == app.label_4.text() == app.label_7.text() == app.label_10.text()

    # when pressing predict button, checking that we have a lists of lists of moves.
    # and we are getting in return a list of lists of which player is predicted.
    qtbot.mouseClick(app.change_history_button, QtCore.Qt.LeftButton)
    app.historyText.setText(moves)
    qtbot.mouseClick(app.change_history_button, QtCore.Qt.LeftButton)

    qtbot.mouseClick(app.predict_pushbutton, QtCore.Qt.LeftButton)
    # here we have to check that players have changed the names and it has the prediction to it.
    # we do that by checking if the percent sign has been inserted to the labels.
    assert "%" in app.label_2.text()
    assert "%" in app.label_5.text()
    assert "%" in app.label_8.text()



def test_add_players(players):
    """
    Checking that we get the players from the txt files from the function add_players

    """
    assert players[0] in list_all_players_available
    assert players[1] in list_all_players_available
    assert players[2] in list_all_players_available
    assert players[0] != players[2]
    assert "Fh-Krems" not in list_all_players_available
