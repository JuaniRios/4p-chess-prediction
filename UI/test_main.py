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

def test_after_submit_confirm(app, qtbot, players):
    app.player1.setText(players[0])
    app.player2.setText(players[1])
    app.player3.setText(players[2])
    app.comboBox.setCurrentText("Yellow")
    qtbot.mouseClick(app.submit_button, QtCore.Qt.LeftButton)

    assert app.opponents == [app.player1.text(), app.player2.text(), app.player3.text()]
    assert app.user_color != "Red"
    assert app.user_color == "Yellow"

def test_after_submit_cancel(app, qtbot, players):
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


def test_add_players(players):
    """
    Checking that we get the players from the txt files from the function add_players

    """
    assert players[0] in list_all_players_available
    assert players[1] in list_all_players_available
    assert players[2] in list_all_players_available
    assert players[0] != players[2]
    assert "Nanna" not in list_all_players_available
