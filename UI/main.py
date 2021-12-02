

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QInputDialog, QCompleter

import re


class Ui_MainWindow(object):
    """
    Making the first window to the user, where he inserts the name of the players and which color he is using.
    """
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("4-player Chess predictor")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 400, 151, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Submit")
        self.pushButton.clicked.connect(self.getInfoAboutGame)

        self.welcometext = QtWidgets.QTextEdit(self.centralwidget)
        self.welcometext.setGeometry(QtCore.QRect(30, 30, 600, 101))
        self.welcometext.setObjectName("lineEdit")
        self.welcometext.setText("Welcome to the 4 player chess predictor, please insert the three players and which "
                                 "colour you are playing with in this game. Please notice that all the three "
                                 "players have to exist in our data for this to work.")
        self.welcometext.setDisabled(True)
        self.welcometext.setFont(QtGui.QFont("Arial", 12))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 200, 47, 13))
        self.label.setObjectName("label")
        self.label.setText("Player 1")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(30, 270, 47, 13))
        self.label2.setObjectName("label_2")
        self.label2.setText("Player 2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 340, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Player 3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(520, 200, 221, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Which color are you?")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(660, 200, 69, 22))
        self.comboBox.setObjectName("comboBoxColor")
        self.comboBox.addItem("Red")
        self.comboBox.addItem("Blue")
        self.comboBox.addItem("Yellow")
        self.comboBox.addItem("Green")

        l1 = self.addPlayer()
        self.player1 = QtWidgets.QLineEdit(self.centralwidget)
        self.player1.setGeometry(QtCore.QRect(110, 200, 113, 20))
        self.player1.setObjectName("player1")

        self.player1.setCompleter(QCompleter(l1))

        self.player2 = QtWidgets.QLineEdit(self.centralwidget)
        self.player2.setGeometry(QtCore.QRect(110, 270, 113, 20))
        self.player2.setObjectName("player2")
        self.player2.setCompleter(QCompleter(l1))

        self.player3 = QtWidgets.QLineEdit(self.centralwidget)
        self.player3.setGeometry(QtCore.QRect(110, 340, 113, 20))
        self.player3.setObjectName("player3")
        self.player3.setCompleter(QCompleter(l1))

        MainWindow.setCentralWidget(self.centralwidget)


    def getInfoAboutGame(self):
        """
        Get information about the game, after the user has confirmed the Dialog, to use it for the training of the model
        :return:
        """
        #getting the color inserted of the user
        self.userColor = self.comboBox.currentText()

        #getting each player and appending it to a list.
        p1 = self.player1.text()
        p2 = self.player2.text()
        p3 = self.player3.text()
        self.opponents = [p1, p2, p3]



        dlg = ConfirmDialog(self.opponents[0], self.opponents[1], self.opponents[2], self.userColor)
        if dlg.exec():
            print("Success!")
            self.window2()
            #send players to training model
        else:
            print("Cancel!")


    def addPlayer(self): # have to fix that he cant add the same player three times.
        """
        Add player is a function which takes the top 100 players of team and solo and concatenate them into a bigger
        list. It only accepts one name once in case a player plays both. Then we are sending the list to the input
        field for the user to select players.
        :return: a list of all available players
        """

        with open('top100players_ffa.txt') as f1:
            teams = f1.read().splitlines()

        with open('top100players_solo.txt') as f2:
            solo = f2.read().splitlines()

        # adding both lists
        listOfPlayersAvailable = teams + solo
        # to delete duplicates
        listOfPlayersAvailable = list(dict.fromkeys(listOfPlayersAvailable))


        return listOfPlayersAvailable


    def opponentsColor(self):
        """
        This function takes in what color the user has inserted and changes the colors displayed on window 2 later,
        to understand better which player is which.

        """

        #if confirm then make the colors.
        self.colors = ["Red", "Blue", "Yellow", "Green"]
        # deleting the color the user has inserted to set the style with the other.
        self.colors.remove(self.userColor)
        self.tableView.setStyleSheet(f"background-color: {self.colors[0]}")
        self.tableView_2.setStyleSheet(f"background-color: {self.colors[1]}")
        self.tableView_3.setStyleSheet(f"background-color: {self.colors[2]}")

    def window2(self):
        """
        This is the window to add moves and start prediction, which will be the main window after the user inserted
        the value needed. Here we have all labels for players being predicted as well as adding moves or changing
        the history of moves.

        """

        print(self.opponents, "checking if players are coming into window")
        #print(self.player1.currentText(), self.player2.currentText(), self.player3.currentText())
        self.historyOfMoves = ""
        self.movesListForPrediction = []
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowTitle("4-player Chess predictor")
        self.centralwidget.setObjectName("centralwidget")

        self.tableView = QtWidgets.QTextEdit(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(40, 30, 201, 100))
        self.tableView.setObjectName("player1")
        self.tableView.setDisabled(True)

        self.tableView_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(290, 30, 201, 100))
        self.tableView_2.setObjectName("player2")
        self.tableView_2.setDisabled(True)

        self.tableView_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.tableView_3.setGeometry(QtCore.QRect(540, 30, 201, 100))
        self.tableView_3.setObjectName("player3")
        self.tableView_3.setDisabled(True)

        #LABEL 2-10 is labels for later showing the predicted players and adding the percentage

        #THE PREDICTION OF THE FIRST PLAYER
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 140, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_2.setText(self.player1.text().capitalize())
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

        #THE PREDICTION OF THE SECOND PLAYER
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

        #THE PREDICTION OF THE THIRD PLAYER
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

        self.infotext = QtWidgets.QTextEdit(self.centralwidget)
        self.infotext.setGeometry(QtCore.QRect(70, 220, 630, 140))
        self.infotext.setObjectName("lineEdit")
        self.infotext.setText("Here you have to add four moves per round, so one move per player. The accepted moves "
                              "are setting which piece following with where it is moving on the board.\nIf a player has "
                              "dropped out replace his turn with a '0'."
                              "\n\nExample:"
                              "'Qa2-Qb4 g4-g6 b2-b1 Qh7-Qh8'"
                              "\nExample: 'a2-a3 a1-a2 Qb5-Qb7 0'\nIf you wants to change the history, press"
                              "the button and change the mistake")
        self.infotext.setDisabled(True)
        self.infotext.setFont(QtGui.QFont("Arial", 11))

        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(120, 370, 451, 41))
        self.lineEdit1.setObjectName("lineEdit")
        self.lineEdit1.setPlaceholderText("a1-b3 h12-g8 a1-a12 b4-b44")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 380, 131, 23))
        self.pushButton.setText("addMoves")
        self.pushButton.clicked.connect(self.addMoves)

        self.historyText = QtWidgets.QTextEdit(self.centralwidget)
        self.historyText.setGeometry(QtCore.QRect(120, 420, 451, 101))
        self.historyText.setObjectName("textEdit")
        self.historyText.setDisabled(True)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 440, 131, 41))
        self.pushButton_2.setText("changeHistory")
        self.pushButton_2.clicked.connect(self.changedH)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 560, 70, 30))
        self.pushButton_3.setText("predict")
        self.pushButton_3.clicked.connect(self.predictButton)



        MainWindow.setCentralWidget(self.centralwidget)
        self.opponentsColor()

    def addMoves(self):
        """This functions adds the moves, for now to a string, to later add them to the prediction
        The user has to add the right format example: 'Qa1-a2 a1-a2 a1-a2 a1-a2' or when a player is
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
            print(self.movesListForPrediction, "before add")
            self.movesListForPrediction.append([self.lineEdit1.text().replace(", ", " ").replace(",", " ")])
            print(self.movesListForPrediction, "after add")
            # maybe here and or to include the players dropping with a 0?

            for i in self.movesListForPrediction:
                self.historyOfMoves += "".join(i)
                self.historyOfMoves += ","

            self.historyText.setText(self.historyOfMoves)
            # setting the historyofMoves string to empty because we are using from the list each time to string.
            self.historyOfMoves = ""

        #have to clear the labelwindow
        self.lineEdit1.clear()
        #print(self.movesListForPrediction) # this list is for Henrik

    def changedH(self):
        """
        This function is used when the player wants to change the history of moves he has added if any mistakes.
        Here we are looking what state we are in to change the disable function in case the user shall type or not
        The tricky part is that set text only accepts string, so converting to and from to the main list which is
        self.movesListForPrediction which later will go into the prediction tool
        :return:
        """

        if self.pushButton_2.text() == "confirm changes":
            self.historyText.setDisabled(True)

            self.historyOfMoves = self.historyText.toPlainText()
            splittingData = self.historyOfMoves.split(",")
            newList = []
            # accessing each round and making a new list.
            for w in splittingData:
                list1 = w.split(",")
                newList.append(list1)

            self.movesListForPrediction = newList
            self.historyOfMoves = ""

            self.pushButton_2.setText("Change history")
            #deleting any comma which may be there.
            for i in range(len(self.movesListForPrediction)):
                if self.movesListForPrediction[i] == [""]:
                    self.movesListForPrediction.pop(i)

            print(self.movesListForPrediction, "after changing history")
        else:
            self.pushButton_2.setText("confirm changes")
            #print(self.pushButton_2.text())
            self.historyText.setDisabled(False)




    def predictButton(self):
        """
        This predict button for now is a simulation with random prediction.
        :return:
        """

        import random

        #5, 10, 15, 20 moves access the precidtion tool on those players
        print(self.opponents)
        random.shuffle(self.opponents)
        print(self.opponents)

        print("predictbutton")
        self.label_2.setText(self.opponents[0]) #first color player
        self.label_3.setText(self.opponents[1])
        self.label_4.setText(self.opponents[2])
        self.label_5.setText(self.opponents[0])# second color
        self.label_6.setText(self.opponents[1])
        self.label_7.setText(self.opponents[2])
        self.label_8.setText(self.opponents[0]) # third color
        self.label_9.setText(self.opponents[1])
        self.label_10.setText(self.opponents[2])
        listOfLabelsOfPlayers = [self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7,
                                 self.label_8, self.label_9, self.label_10]
        for i in listOfLabelsOfPlayers:
            i.adjustSize()
        # here we also know the order of colors, so we can add the labels accordingly



class ConfirmDialog(QDialog):
    """
        Class for the dialog
    """

    def __init__(self, player1, player2, player3, color, parent=None):
        """

        :param player1: getting the value of the first player
        :param player2: getting the value of the second player
        :param player3: getting the value of the third player
        :param color: getting the color of the user
        :param parent: So we making the window in front of the main window.
        """
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.userColor = color
        super().__init__(parent)
        self.setWindowTitle('Confirm players and  your color')

        QBtn = QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)


        self.buttonBox.accepted.connect(self.accept)

        self.buttonBox.rejected.connect(self.reject)

        self.layout = QtWidgets.QVBoxLayout()
        messageToSend = (f"player 1 = {self.player1}, player2 = {self.player2}, player3 = {self.player3}, your color is = {self.userColor}")
        message = QtWidgets.QLabel(messageToSend)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



