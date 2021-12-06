import pytest
import main
from PyQt5 import QtCore

list_all_players_available = main.get_player()
@pytest.fixture
def players():
    players = ["Mzambe", "Rasen555", "rook6431"]

    return players

@pytest.fixture
def app(qtbot):
    ui = main.UiMainWindow()
    qtbot.addWidget(ui)

    return ui


def test_label_first_window(app, players):
    assert app.label_inserting_p1.text() == "Player 1"
    assert app.label_inserting_p2.text() == "Player 2"
    assert app.player1.text() == ""
    app.player1.setText(players[0])
    assert app.player1.text() == "Mzambe"

def test_get_info_about_game_confirm(app, qtbot, players):
    app.player1.setText(players[0])
    app.player2.setText(players[1])
    app.player3.setText(players[2])
    app.comboBox.setCurrentText("Yellow")
    qtbot.mouseClick(app.submit_button, QtCore.Qt.LeftButton)

    assert app.opponents == [app.player1.text(), app.player2.text(), app.player3.text()]
    assert app.user_color != "Red"
    assert app.user_color == "Yellow"
    # making sure that the visualisation is not having yellow.
    assert "Yellow" not in app.colors
    # Checking that we come to window 2
    assert app.add_moves_button.text() == "Add moves"

def test_get_info_about_game_cancel(app, qtbot, players):
    """
    Checking that if we are sending two of the same player name that we are not sending it through

    """
    app.player1.setText(players[0])
    app.player2.setText(players[0])
    app.player3.setText(players[2])
    qtbot.mouseClick(app.submit_button, QtCore.Qt.LeftButton)

    assert app.opponents == None
    # Making sure we are still on the first window.
    assert app.label_inserting_p1.text() == "Player 1"
    assert app.label_inserting_p2.text() == "Player 2"

def test_opponents_color(app, qtbot, players):
    pass

def test_window2(app, qtbot, players):
    app.player1.setText(players[0])
    app.player2.setText(players[1])
    app.player3.setText(players[2])
    app.opponents = [app.player1, app.player2, app.player3]
    app.user_color = "Yellow"
    # opening the second window.
    app.window2()
    # checking that the labels 2,5,8 for now is player 1
    assert app.label_2.text() and app.label_5.text() and app.label_8.text() == app.player1.text()
    # checking that the other are not player one from start.
    assert app.label_3.text() != app.player1.text()
    assert app.historyText.toPlainText() == ""




def test_add_moves(app, qtbot, players):
    app.player1.setText(players[0])
    app.player2.setText(players[0])
    app.player3.setText(players[2])
    app.opponents = [app.player1, app.player2, app.player3]
    app.user_color = "Yellow"
    try_move1 = "a1-a2 a1-a2 a1-a2 a1-a2"
    try_move2 = "a1-a2 Qf5-Qd3 0 0"
    try_move3 = "a1-a2 a1-a2 a1-a2 aaaaaaa"
    app.window2()

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
    app.add_moves_lineedit.setText(try_move3)
    qtbot.mouseClick(app.add_moves_button, QtCore.Qt.LeftButton)
    assert app.historyText.toPlainText() != try_move3+","
    # checking that the list of lists is updated!
    assert app.moves_list_prediction == [[try_move1], [try_move2]]
    assert app.moves_list_prediction != [[try_move1], [try_move2], [try_move3]]

def test_change_history(app, qtbot, players):
    pass

def test_predict_button(app, qtbot, players):
    pass








def test_add_players(players):
    """
    Checking that we get the players from the txt files from the function add_players

    """
    assert players[0] in list_all_players_available
    assert players[1] in list_all_players_available
    assert players[2] in list_all_players_available
    assert players[0] != players[2]
    assert "Nanna" not in list_all_players_available
