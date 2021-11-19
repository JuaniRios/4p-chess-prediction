

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QInputDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)



        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 220, 151, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.getInfoAboutGame)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 47, 13))
        self.label.setObjectName("label")
        self.label.setText("Player 1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(30, 130, 47, 13))
        self.label2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 200, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(520, 80, 221, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(660, 80, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Yellow")
        self.comboBox.addItem("Red")
        self.comboBox.addItem("Green")
        self.comboBox.addItem("Blue")
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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHello.menuAction())

        self.ChangeName(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def ChangeName(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label2.setText(_translate("MainWindow", "Player 2"))
        self.label_3.setText(_translate("MainWindow", "Player 3"))
        self.label_4.setText(_translate("MainWindow", "Which color are you?"))
        self.menuHello.setTitle(_translate("MainWindow", "4-player Chess predictor"))

    def getInfoAboutGame(self, i):
        self.userColor=self.comboBox.currentText()
        print(self.comboBox.currentText())
        p1 = self.player1.text()
        p2 = self.player2.text()
        p3 = self.player3.text()
        print(self.player1.text())
        print(self.player2.text())
        print(self.player3.text())

        dlg = ConfirmDialog(p1,p2,p3,self.userColor)
        if dlg.exec():
            print("Success!")

            self.window2()
        else:
            print("Cancel!")

    # self.hidingContent(self.comboBox, self.label, self.label2,
    #                    self.label_3, self.label_4, self.pushButton)
    #
    # def hidingContent(self, *args):
    #     for i in args:
    #         i.hide()

    def opponentsColor(self):
        #if confirm then make the colors.
        self.colors = ["Yellow", "Red", "Green", "Blue"]
        self.colors.remove(self.userColor)
        print(self.colors)
        self.tableView.setStyleSheet(f"background-color: {self.colors[0]}")
        self.tableView_2.setStyleSheet(f"background-color: {self.colors[1]}")
        self.tableView_3.setStyleSheet(f"background-color: {self.colors[2]}")

    def window2(self):
        self.opponents = [self.player1.text(), self.player2.text(), self.player3.text()]
        self.historyOfMoves = ""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowTitle("4-player Chess predictor")
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(120, 310, 451, 41))
        self.lineEdit1.setObjectName("lineEdit")
        self.lineEdit1.setPlaceholderText("a1-b3-h5-g8")

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
        self.label_7.setText(self.player3.text().capitalize())

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(620, 160, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_8.setText(self.player1.text().capitalize())

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(620, 180, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_9.setText(self.player2.text().capitalize())

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(620, 200, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label_10.setText(self.player3.text().capitalize())

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
        #check that he added the right format, otherwise send something back or change the format?

        #print(self.lineEdit1.text())
        self.historyOfMoves += (self.lineEdit1.text())
        #print(self.historyOfMoves)
        self.historyText.setText(self.historyOfMoves)
        self.lineEdit1.clear()

    def changedH(self):
        if self.pushButton_2.text() == "confirm changes":
            self.historyText.setDisabled(True)
            #print(self.historyText.toPlainText())

            self.historyOfMoves = self.historyText.toPlainText()
            self.pushButton_2.setText("Change history")
        else:
            self.pushButton_2.setText("confirm changes")
            #print(self.pushButton_2.text())
            self.historyText.setDisabled(False)



    def predictButton(self):
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








class ConfirmDialog(QDialog):
    def __init__(self, player1, player2, player3, color, parent=None): # to make  infront of parent
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.userColor = color
        super().__init__(parent)
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



