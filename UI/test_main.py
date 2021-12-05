import pytest
import app
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
list_all_players_available = app1.get_player()
@pytest.fixture
def players():
    players = ["Mzambe", "Rasen555", "rook6431"]
    return players


# def app():
#
#     import sys
#     from PyQt5 import QtCore, QtGui, QtWidgets
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = app1.UiMainWindow()
#     ui.start(MainWindow)
#
#     MainWindow.show()

# @pytest.fixture()
# def label( qtbot ):
#     qlabel = app.UiMainWindow()
#
#     qtbot.addWidget(qlabel)
#     return qlabel

def test_label():
    #print(app.label_color.text())
    assert a.submit_button == "Submit"


# Starting the application.
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = app.UiMainWindow()
    ui.start(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




# def test_add_players(players):
#     assert players[0] in list_all_players_available
#     assert players[1] in list_all_players_available
#     assert players[2] in list_all_players_available
#     assert players[0] != players[2]
#
# def test_hello(app):
#
#
#     assert app.label_inserting_p1.text() == "Player 1"
#
#
#
#



