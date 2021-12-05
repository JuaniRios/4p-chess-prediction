import pytest
import main

list_all_players_available = main.get_player()
@pytest.fixture
def players():
    players = ["Mzambe", "Rasen555", "rook6431"]
    return players

@pytest.fixture
def app(qtbot):
    test_hello_app = main.UiMainWindow()
    qtbot.addWidget(test_hello_app)

    return test_hello_app


def test_label(app):
    assert app.label_inserting_p1.text() == "Player 1"




# def test_add_players(players):
#     assert players[0] in list_all_players_available
#     assert players[1] in list_all_players_available
#     assert players[2] in list_all_players_available
#     assert players[0] != players[2]
#     assert "Nanna" not in list_all_players_available
#
# def test_hello(app):
#
#
#     assert app.label_inserting_p1.text() == "Player 1"
#
#
#
#



