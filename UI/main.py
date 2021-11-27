

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QInputDialog
import re


class Ui_MainWindow(object):
    """First window"""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("4-player Chess predictor")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 220, 151, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Submit")
        self.pushButton.clicked.connect(self.getInfoAboutGame)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 47, 13))
        self.label.setObjectName("label")
        self.label.setText("Player 1")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(30, 130, 47, 13))
        self.label2.setObjectName("label_2")
        self.label2.setText("Player 2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 200, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Player 3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(520, 80, 221, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Which color are you?")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(660, 80, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Red")
        self.comboBox.addItem("Blue")
        self.comboBox.addItem("Yellow")
        self.comboBox.addItem("Green")

        self.player1 = QtWidgets.QLineEdit(self.centralwidget)
        self.player1.setGeometry(QtCore.QRect(110, 60, 113, 20))
        self.player1.setObjectName("p1")

        self.player2 = QtWidgets.QLineEdit(self.centralwidget)
        self.player2.setGeometry(QtCore.QRect(110, 130, 113, 20))
        self.player2.setObjectName("p2")

        self.player3 = QtWidgets.QLineEdit(self.centralwidget)
        self.player3.setGeometry(QtCore.QRect(110, 200, 113, 20))
        self.player3.setObjectName("p3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        self.menuHello = QtWidgets.QMenu(self.menubar)
        self.menuHello.setObjectName("menuHello")
        self.menuHello.setTitle("Restart")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHello.menuAction())




    #MAYBE MAKE A DROP DOWN WITH ALL PLAYERS AVAILABLE?

    def getInfoAboutGame(self, i):
        """This functions takes the input about each player to later add them to the training model."""
        self.userColor=self.comboBox.currentText()
        print(self.comboBox.currentText())
        p1 = self.player1.text()
        p2 = self.player2.text()
        p3 = self.player3.text()
        print(self.player1.text())
        print(self.player2.text())
        print(self.player3.text())
        self.opponents = [p1, p2, p3]
        if self.checkExistingPlayers(self.opponents):
            dlg = ConfirmDialog(self.opponents[0], self.opponents[1], self.opponents[2], self.userColor)
            if dlg.exec():
                print("Success!")

                self.window2()
            else:
                print("Cancel!")
        else:
            print("Sorry dude!!")
            #here I need to pop up a window saying something went wrong, either some players are not in the data.


    def checkExistingPlayers(self, args):
        """Here we go through the data to see if players are in, we need all three so perform the algorithm"""
        with open('top100players_ffa.txt') as f1:
            teams = f1.read().splitlines()

        with open('top100players_solo.txt') as f2:
            solo = f2.read().splitlines()

        #adding both lists
        listOfPlayersAvailable = teams + solo
        # to delete duplicates
        listOfPlayersAvailable = list(dict.fromkeys(listOfPlayersAvailable))

        #players inserted
        players = [*args]
        count = 0
        for i in listOfPlayersAvailable:
            if players[0] == i:
                count += 1
            elif players[1] == i:
                count += 1
            elif players[2] == i:
                count += 1
        #if we find all three players in the data we return true
        if count == 3:
            return True
        return False



        # dlg = ConfirmDialog(self.opponents[0], self.opponents[1], self.opponents[2], self.userColor)
        # if dlg.exec():
        #     print("Success!")
        #
        #
        #     self.window2()
        # else:
        #     print("Cancel!")

    # self.hidingContent(self.comboBox, self.label, self.label2,
    #                    self.label_3, self.label_4, self.pushButton)
    #
    # def hidingContent(self, *args):
    #     for i in args:
    #         i.hide()

    def opponentsColor(self):
        """This functions sets the color on the board so vizualize for the user where his opponoent are"""
        #if confirm then make the colors.
        self.colors = ["Red", "Blue", "Yellow", "Green"]
        self.colors.remove(self.userColor)
        print(self.colors)
        self.tableView.setStyleSheet(f"background-color: {self.colors[0]}")
        self.tableView_2.setStyleSheet(f"background-color: {self.colors[1]}")
        self.tableView_3.setStyleSheet(f"background-color: {self.colors[2]}")

    def window2(self):
        """Creating the window for adding moves and prediction """
        print(self.opponents, "checking if players are coming into window")
        self.historyOfMoves = ""
        self.movesListForPrediction = []
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowTitle("4-player Chess predictor")
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(120, 310, 451, 41))
        self.lineEdit1.setObjectName("lineEdit")
        self.lineEdit1.setPlaceholderText("a1-b3 h12-g8 a1-a12 b4-b44")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 320, 131, 23))
        self.pushButton.setText("addMoves")
        self.pushButton.clicked.connect(self.addMoves)

        self.historyText = QtWidgets.QTextEdit(self.centralwidget)
        self.historyText.setGeometry(QtCore.QRect(120, 380, 451, 101))
        self.historyText.setObjectName("textEdit")
        self.historyText.setDisabled(True)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 410, 131, 41))
        self.pushButton_2.setText("changeHistory")
        self.pushButton_2.clicked.connect(self.changedH)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 510, 131, 41))
        self.pushButton_3.setText("predict")
        self.pushButton_3.clicked.connect(self.predictButton)

        self.tableView = QtWidgets.QTextEdit(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(40, 50, 201, 100))
        self.tableView.setObjectName("player1")
        self.tableView.setDisabled(True)

        self.tableView_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(290, 50, 201, 100))
        self.tableView_2.setObjectName("player2")
        self.tableView_2.setDisabled(True)

        self.tableView_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.tableView_3.setGeometry(QtCore.QRect(540, 50, 201, 100))
        self.tableView_3.setObjectName("player3")
        self.tableView_3.setDisabled(True)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 160, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_2.setText(self.player1.text().capitalize())

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 180, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_3.setText(self.player2.text().capitalize())

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 200, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_4.setText(self.player3.text().capitalize())

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 160, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_5.setText(self.player1.text().capitalize())

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 180, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_6.setText(self.player2.text().capitalize())

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 200, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_7.setText(self.player3.text())

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(620, 160, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_8.setText(self.player1.text())

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(620, 180, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_9.setText(self.player2.text())

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(620, 200, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label_10.setText(self.player3.text())

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.opponentsColor()

    def addMoves(self):
        """This functions adds the moves, for now to a string, to later add them to the prediction
        The user has to add the right format example: 'a1-a2 a1-a2 a1-a2 a1-a2' or when a player is
        missing he shall insert a 0 on this place: 'a1-a2 0 a1-a2 a1-a2"""

        #Using regex to get the right format.
        move = r"[a-zA-Z]{1,2}\d{1,2}-[a-zA-Z]{1,2}\d{1,2}|0"
        if re.match(f'{move} {move} {move} {move}', self.lineEdit1.text()):
            #the last is for a space?!
            print(self.movesListForPrediction, "before add")
            self.movesListForPrediction.append([self.lineEdit1.text()])
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
        """This is when the user would like to correct the history of moves"""
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

            #only problem now is that if he doesnt add manually, he has a comma.

    def predictButton(self):
        """For now this predictbutton is only simulation random prediction. Wants to add the percentage and add the code when ready"""
        import random


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
        # here we also know the order of colors, so we can add the labels accordingly








class ConfirmDialog(QDialog):

    def __init__(self, player1, player2, player3, color, parent=None): # to make  infront of parent
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.userColor = color
        super().__init__(parent)
        self.setWindowTitle('Confirm players and color')

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



