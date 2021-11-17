

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox


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
        self.label.setText(_translate("MainWindow", "Player 1"))
        self.label2.setText(_translate("MainWindow", "Player 2"))
        self.label_3.setText(_translate("MainWindow", "Player 3"))
        self.label_4.setText(_translate("MainWindow", "Which color are you?"))
        self.menuHello.setTitle(_translate("MainWindow", "4-player Chess predictor"))

    def getInfoAboutGame(self, i):
        userColor=self.comboBox.currentText()
        print(self.comboBox.currentText())
        p1 = self.player1.text()
        p2 = self.player2.text()
        p3 = self.player3.text()
        print(self.player1.text())
        print(self.player2.text())
        print(self.player3.text())

        dlg = ConfirmDialog(p1,p2,p3,userColor)
        if dlg.exec():
            print("Success!")
            self.hidingContent(self.player1, self.player2, self.player3, self.comboBox, self.label, self.label2,
                               self.label_3, self.label_4, self.pushButton)
            self.window2()
        else:
            print("Cancel!")



    def hidingContent(self, *args):
        for i in args:
            i.hide()

    def window2(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 310, 451, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 320, 131, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 380, 451, 101))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 410, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 510, 131, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(40, 50, 201, 192))
        self.tableView.setObjectName("tableView")
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(290, 50, 201, 192))
        self.tableView_2.setObjectName("tableView_2")
        self.tableView_3 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_3.setGeometry(QtCore.QRect(540, 50, 201, 192))
        self.tableView_3.setObjectName("tableView_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Add moves"))
        self.pushButton_2.setText(_translate("MainWindow", "Show/Change history"))
        self.pushButton_3.setText(_translate("MainWindow", "PREDICT"))



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
