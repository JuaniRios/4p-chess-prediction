from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QCompleter

import re


def get_player():
    """
    Add player is a function which takes the top 100 players of team and solo and concatenate them into a bigger
    list. It only accepts one name once in case a player plays both. Then we are sending the list to the input
    field for the user to select players.
    :return: a list of all available players
    """
    # getting players from team chess
    with open('top100players_ffa.txt') as f1:
        teams = f1.read().splitlines()

    # getting players from solo chess
    with open('top100players_solo.txt') as f2:
        solo = f2.read().splitlines()

    # adding both lists
    list_of_players_available = teams + solo
    # to delete duplicates
    list_of_players_available = list(dict.fromkeys(list_of_players_available))

    return list_of_players_available


class UiMainWindow(object):
    """
    Making the first window to the user, where he inserts the name of the players and which color he is using.
    """

    def start(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("4-player Chess predictor")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(590, 400, 151, 23))
        self.submit_button.setObjectName("pushButton")
        self.submit_button.setText("Submit")
        self.submit_button.clicked.connect(self.get_info_about_game)

        self.welcome_text = QtWidgets.QTextEdit(self.centralwidget)
        self.welcome_text.setGeometry(QtCore.QRect(30, 30, 680, 150))
        self.welcome_text.setObjectName("lineEdit")
        self.welcome_text.setText("Welcome to the 4 player chess predictor.\n\nPlease insert the three players and "
                                  "which colour you are playing with in this game. Please notice that all the three "
                                  "players have to exist in our data for this to work. If you entered players wrongly, "
                                  "then you will not proceed to the next window. If there is no suggestion for a player"
                                  ", then the player do not exist in our data or you might have misspelled the player.")
        self.welcome_text.setDisabled(True)
        self.welcome_text.setFont(QtGui.QFont("Arial", 12))

        self.label_inserting_p1 = QtWidgets.QLabel(self.centralwidget)
        self.label_inserting_p1.setGeometry(QtCore.QRect(30, 200, 47, 13))
        self.label_inserting_p1.setObjectName("label")
        self.label_inserting_p1.setText("Player 1")

        self.label_inserting_p2 = QtWidgets.QLabel(self.centralwidget)
        self.label_inserting_p2.setGeometry(QtCore.QRect(30, 270, 47, 13))
        self.label_inserting_p2.setObjectName("label_2")
        self.label_inserting_p2.setText("Player 2")

        self.label_inserting_p3 = QtWidgets.QLabel(self.centralwidget)
        self.label_inserting_p3.setGeometry(QtCore.QRect(30, 340, 47, 13))
        self.label_inserting_p3.setObjectName("label_3")
        self.label_inserting_p3.setText("Player 3")

        self.label_color = QtWidgets.QLabel(self.centralwidget)
        self.label_color.setGeometry(QtCore.QRect(520, 200, 221, 16))
        self.label_color.setObjectName("label_4")
        self.label_color.setText("Which color are you?")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(660, 200, 69, 22))
        self.comboBox.setObjectName("comboBoxColor")
        self.comboBox.addItem("Red")
        self.comboBox.addItem("Blue")
        self.comboBox.addItem("Yellow")
        self.comboBox.addItem("Green")

        list_of_players = get_player()
        self.player1 = QtWidgets.QLineEdit(self.centralwidget)
        self.player1.setGeometry(QtCore.QRect(110, 200, 113, 20))
        self.player1.setObjectName("player1")
        self.player1.setCompleter(QCompleter(list_of_players))

        self.player2 = QtWidgets.QLineEdit(self.centralwidget)
        self.player2.setGeometry(QtCore.QRect(110, 270, 113, 20))
        self.player2.setObjectName("player2")
        self.player2.setCompleter(QCompleter(list_of_players))

        self.player3 = QtWidgets.QLineEdit(self.centralwidget)
        self.player3.setGeometry(QtCore.QRect(110, 340, 113, 20))
        self.player3.setObjectName("player3")
        self.player3.setCompleter(QCompleter(list_of_players))

        MainWindow.setCentralWidget(self.centralwidget)

    def get_info_about_game(self):
        """
        Get information about the game, after the user has confirmed the Dialog, to use it for the training of the model
        First we need to check that the players are in the data so the prediction can be done on them.
        :return:
        """
        # getting the color inserted of the user
        self.user_color = self.comboBox.currentText()

        # Taking each name of each player
        p1 = self.player1.text()
        p2 = self.player2.text()
        p3 = self.player3.text()

        # Using the function to get all players from the txt files.
        all_player_list = get_player()

        # Here we are checking that there is three different players, from our data.
        number = 0
        for name in all_player_list:

            if p1 == name and (p1 != p2 or p1 != p3):
                number += 1
            elif p2 == name and (p2 != p1 or p2 != p3):
                number += 1
            elif p3 == name and (p3 != p2 or p1 != p1):
                number += 1
        # Checking if we have three different players so we are sending the data through to the confirmation.
        if number == 3:
            self.opponents = [p1, p2, p3]
            self.opponents = list(dict.fromkeys(self.opponents))
            print(self.opponents)
            print(len(self.opponents))

            # Here is the confirm dialog, just to make sure he inserted the right thing before sending it to the
            # training model.
            dlg = ConfirmDialog(self.opponents, self.user_color)
            if dlg.exec():

                # henrik function(self.opponents, self.user_color) # what do we return from here?
                print("Success!")
                print(self.opponents, self.user_color, "to henrik")
                self.window2()

            else:
                print("Cancel!")
        else:
            print("Oops, something is wrong.")

    def opponents_color(self):
        """
        This function takes in what color the user has inserted and changes the colors displayed on window 2 later,
        to understand better which player is which.

        """

        # if confirm then make the colors.
        self.colors = ["Red", "Blue", "Yellow", "Green"]
        # deleting the color the user has inserted to set the style with the other.
        self.colors.remove(self.user_color)
        self.first_color.setStyleSheet(f"background-color: {self.colors[0]}")
        self.second_color.setStyleSheet(f"background-color: {self.colors[1]}")
        self.third_color.setStyleSheet(f"background-color: {self.colors[2]}")

    def window2(self):
        """
        This is the window to add moves and start prediction, which will be the main window after the user inserted
        the value needed. Here we have all labels for players being predicted as well as adding moves or changing
        the history of moves.

        """

        print(self.opponents, "checking if players are coming into window")
        # print(self.player1.currentText(), self.player2.currentText(), self.player3.currentText())
        self.history_of_moves = ""
        self.moves_list_prediction = []
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowTitle("4-player Chess predictor")
        self.centralwidget.setObjectName("centralwidget")

        # These three are for visualisation purposes, so we know later which player is predicted.
        self.first_color = QtWidgets.QTextEdit(self.centralwidget)
        self.first_color.setGeometry(QtCore.QRect(40, 30, 201, 100))
        self.first_color.setObjectName("player1")
        self.first_color.setDisabled(True)

        self.second_color = QtWidgets.QTextEdit(self.centralwidget)
        self.second_color.setGeometry(QtCore.QRect(290, 30, 201, 100))
        self.second_color.setObjectName("player2")
        self.second_color.setDisabled(True)

        self.third_color = QtWidgets.QTextEdit(self.centralwidget)
        self.third_color.setGeometry(QtCore.QRect(540, 30, 201, 100))
        self.third_color.setObjectName("player3")
        self.third_color.setDisabled(True)

        # LABEL 2-10 is labels for later showing the predicted players and adding the percentage

        # THE PREDICTION OF THE FIRST PLAYER
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 140, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_2.setText(self.player1.text())
        self.label_2.adjustSize()

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 160, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_3.setText(self.player2.text())
        self.label_3.adjustSize()

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 180, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_4.setText(self.player3.text())
        self.label_4.adjustSize()

        # THE PREDICTION OF THE SECOND PLAYER
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 140, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_5.setText(self.player1.text())
        self.label_5.adjustSize()

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 160, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_6.setText(self.player2.text())
        self.label_6.adjustSize()

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 180, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_7.setText(self.player3.text())
        self.label_7.adjustSize()

        # THE PREDICTION OF THE THIRD PLAYER
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(620, 140, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_8.setText(self.player1.text())
        self.label_8.adjustSize()

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(620, 160, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_9.setText(self.player2.text())
        self.label_9.adjustSize()

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(620, 180, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label_10.setText(self.player3.text())
        self.label_10.adjustSize()

        self.info_text = QtWidgets.QTextEdit(self.centralwidget)
        self.info_text.setGeometry(QtCore.QRect(70, 220, 630, 140))
        self.info_text.setObjectName("lineEdit")
        self.info_text.setText("Here you have to add four moves per round, so one move per player. The accepted moves "
                               "are setting which piece following with where it is moving on the board.\nIf a player has "
                               "dropped out replace his turn with a '0'."
                               "\n\nExample:"
                               "'Qa2-Qb4 g4-g6 b2-b1 Qh7-Qh8'"
                               "\nExample: 'a2-a3 a1-a2 Qb5-Qb7 0'\nIf you wants to change the history, press"
                               "the button and change the mistake")
        self.info_text.setDisabled(True)
        self.info_text.setFont(QtGui.QFont("Arial", 11))

        # This is the field where the user add moves and being saved in the prediction list.
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(120, 370, 451, 41))
        self.lineEdit1.setObjectName("lineEdit")
        self.lineEdit1.setPlaceholderText("Qa1-Qb3 h12-g8 a1-a12 b4-b44")

        self.add_moves_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_moves_button.setGeometry(QtCore.QRect(630, 380, 131, 23))
        self.add_moves_button.setText("Add moves")
        self.add_moves_button.clicked.connect(self.add_moves)

        # Here the user can change the history, in case something was wrong.
        self.historyText = QtWidgets.QTextEdit(self.centralwidget)
        self.historyText.setGeometry(QtCore.QRect(120, 420, 451, 101))
        self.historyText.setObjectName("textEdit")
        self.historyText.setDisabled(True)

        self.change_history_button = QtWidgets.QPushButton(self.centralwidget)
        self.change_history_button .setGeometry(QtCore.QRect(630, 440, 131, 41))
        self.change_history_button .setText("Change history")
        self.change_history_button .clicked.connect(self.changed_history)

        self.predict_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.predict_pushbutton.setGeometry(QtCore.QRect(650, 560, 70, 30))
        self.predict_pushbutton.setText("predict")
        self.predict_pushbutton.clicked.connect(self.predict_players)

        MainWindow.setCentralWidget(self.centralwidget)
        # changing the background to visualize which color is where depending on order.
        # here we are setting the visualisation with the three color user is not.
        self.opponents_color()

    def add_moves(self):
        """This functions adds the moves, for now to a string, to later add them to the prediction
        The user has to add the right format example: 'Qa1-Qa2 a1-a2 a1-a2 a1-a2' or when a player is
        missing he shall insert a 0 on this place: 'a1-a2 0 a1-a2 a1-a2"""

        # Using regex to get the right format.
        # move = r"[a-zA-Z]{1,2}\d{1,2}-[a-zA-Z]{1,2}\d{1,2}|0"
        moves = r"((([A-Z]?[a-z]\d{1,2}(-|x)[A-Z]?[a-z]\d{1,2}(=[A-Z])?)|O-O|O-O-O|0)(\s|,\s?)){3}((([A-Z]?[a-z]\d{1,2}(-|x)[A-Z]?[a-z]\d{1,2})(=[A-Z])?|O-O|O-O-O)|0)"

        # this regex accepts one or zero big character followed by exactly one small character, 1 or 2 digits, a dash or an x
        # followed by again 0 or 1 big character, exactly one small character, 1 or 2 digits, 0 or 1 =[A-Z] for pawn promotion
        # OR the castling moves OR a 0. This group represents the possible moves and
        # is followed by either exactly one space, or a comma with an optional space.
        # This group is being repeated 3 times. The whole group is then repeated
        # again but without the space or the comma in the end.

        if re.fullmatch(f'{moves}', self.lineEdit1.text()):
            print(self.moves_list_prediction, "before add")
            self.moves_list_prediction.append([self.lineEdit1.text().replace(", ", " ").replace(",", " ")])
            print(self.moves_list_prediction, "after add")
            # maybe here and or to include the players dropping with a 0?

            for i in self.moves_list_prediction:
                self.history_of_moves += "".join(i)
                self.history_of_moves += ","

            self.historyText.setText(self.history_of_moves)
            # setting the history_of_moves string to empty because we are using from the list each time to string.
            self.history_of_moves = ""

        # have to clear the label window
        self.lineEdit1.clear()
        # print(self.movesListForPrediction) # this list is for Henrik

    def changed_history(self):
        """
        This function is used when the player wants to change the history of moves he has added if any mistakes.
        Here we are looking what state we are in to change the disable function in case the user shall type or not
        The tricky part is that set text only accepts string, so converting to and from to the main list which is
        self.movesListForPrediction which later will go into the prediction tool
        :return:
        """
        # checking what state we are in with the button, if the user wants to change the data or not.
        if self.change_history_button.text() == "confirm changes":
            self.historyText.setDisabled(True)

            self.history_of_moves = self.historyText.toPlainText()
            splitting_data = self.history_of_moves.split(",")
            new_list = []
            # accessing each round and making a new list.
            for w in splitting_data:
                list1 = w.split(",")
                new_list.append(list1)

            self.moves_list_prediction = new_list
            # making the history of moves empty again.
            self.history_of_moves = ""

            self.change_history_button.setText("Change history")
            # deleting any comma which may be there.
            for i in range(len(self.moves_list_prediction)):
                if self.moves_list_prediction[i] == [""]:
                    self.moves_list_prediction.pop(i)

            print(self.moves_list_prediction, "after changing history")
        else:
            # here we changing the name of the button and making it disabled.
            self.change_history_button.setText("confirm changes")

            # making the window changeable
            self.historyText.setDisabled(False)

    def predict_players(self):
        """
        This predict button for now is a simulation with random prediction.
        :return: get the prediction from the model with the percentage of which
        """
        print(self.moves_list_prediction, "this shall go to henrik")
        # predicted = henrik_function2(self.moves_list_prediction)

        import random

        # 5, 10, 15, 20 moves access the prediction tool on those players

        random.shuffle(self.opponents)

        print(self.opponents, self.user_color, "to see if we can access it here,")
        print("predict button")
        self.label_2.setText(self.opponents[0])  # first color player
        self.label_3.setText(self.opponents[1])
        self.label_4.setText(self.opponents[2])
        self.label_5.setText(self.opponents[0])  # second color
        self.label_6.setText(self.opponents[1])
        self.label_7.setText(self.opponents[2])
        self.label_8.setText(self.opponents[0])  # third color
        self.label_9.setText(self.opponents[1])
        self.label_10.setText(self.opponents[2])
        list_of_labels_of_players = [self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7,
                                     self.label_8, self.label_9, self.label_10]
        for i in list_of_labels_of_players:
            i.adjustSize()


class ConfirmDialog(QDialog):
    """
        Class for the dialog
    """

    def __init__(self, player_list, color, parent=None):
        """

        :param player_list: getting the inserted players
        :param color: getting the color of the user
        :param parent: So we making the window in front of the main window.
        """
        self.player_list = player_list
        self.userColor = color
        # making it in front of the other window
        super().__init__(parent)
        self.setWindowTitle('Confirm players and  your color')
        q_btn = QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        self.buttonBox = QtWidgets.QDialogButtonBox(q_btn)

        # Push button, OK or cancel
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QtWidgets.QVBoxLayout()
        # Message to send to user.
        message = (
            f"player 1 = {self.player_list[0]}, player2 = {self.player_list[1]}, player3 = {self.player_list[2]}, "
            f"your color is = {self.userColor}")
        print(message)
        message = QtWidgets.QLabel(message)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


# Starting the application.
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.start(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
