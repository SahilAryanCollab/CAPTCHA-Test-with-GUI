from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel,QLineEdit,QMainWindow,QApplication,QPushButton,QWidget,QVBoxLayout
from PyQt5 import uic
import sys
#defining a class of type QMainWindow
class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        # Loading the created UI file in the class
        uic.loadUi("bot_catcher.ui", self)
        # Setting title of the window
        self.setWindowTitle("Character Recognition CAPTCHA")
        # Setting variable "image" as the image being generated
        self.image = self.findChild(QLabel, "question")
        # Setting variable "answer" as label which displays text "Answer"
        self.answer_label = self.findChild(QLabel,"Answer")
        # Setting variable "str_input" as the text field where user puts his answer
        self.str_input = self.findChild(QLineEdit, "answer_input")
        # Setting variable "submit" as the button the GUI for submitting the answer
        self.submit = self.findChild(QPushButton, "pushButton")
        # Setting variable "ending" as the label which displays text it receives from check function
        self.ending = self.findChild(QLabel,"ending")
        self.try_again = self.findChild(QPushButton,"pushButton_2")
        #When the "submit" button is hit the check function is called and the input in the str_input is checked
        self.submit.clicked.connect(self.check)
        #The variable "ending" is set to hidden
        self.ending.setHidden(True)
        self.try_again.setHidden(True)
        #Showing all the widgets we have used
        self.show()

    def hiding(self):
        #here we clear the text field for user
        self.str_input.setText("")
        #here we set "ending" and "try_again" hidden
        self.ending.setHidden(True)
        self.try_again.setHidden(True)
        #here we set "image","str_input","submit" and "answer_label" to unhide
        self.image.setHidden(False)
        self.str_input.setHidden(False)
        self.submit.setHidden(False)
        self.answer_label.setHidden(False)

    def check(self):
        #Compares the input given to "str_input" with the answer "arch dsjcbka"
        if self.str_input.text() == "arch dsjcbka":
            #All the widgets except "ending" is set to hidden
            self.image.setHidden(True)
            self.str_input.setHidden(True)
            self.submit.setHidden(True)
            self.answer_label.setHidden(True)
            # here the variable "ending" is given the text "You are HUMAN"
            self.ending.setText("You are HUMAN")
            #here we set the widget "ending" to unhide
            self.ending.setHidden(False)
        else:
            # All the widgets except "ending" is set to hidden
            self.image.setHidden(True)
            self.str_input.setHidden(True)
            self.submit.setHidden(True)
            self.answer_label.setHidden(True)
            # here the variable "ending" is given the text "You are a BOT"
            self.ending.setText("You are a BOT")
            #here we set the widget "ending" to unhide
            self.ending.setHidden(False)
            self.try_again.setHidden(False)
            #here when the button "try_again" is clicked the function "hiding" is
            self.try_again.clicked.connect(self.hiding)

app = QApplication(sys.argv)
UIWindow = mainwindow()
app.exec_()
