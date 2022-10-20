import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel,QLineEdit,QMainWindow,QApplication,QPushButton,QWidget,QVBoxLayout
from PyQt5 import uic
import sys
#defining a class of type QMainWindow
class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        # Loading the created UI file in the class
        uic.loadUi("Choose Wisely.ui", self)
        # Setting title of the window
        self.setWindowTitle("Choose Wisely")
        # Setting pushbutton "image1" and "image2" as the images being generated
        self.image1 = self.findChild(QPushButton, "pushButton")
        self.image2 = self.findChild(QPushButton,"pushButton_2")
        #this label displays the question
        self.instruction = self.findChild(QLabel, "label")
        #this dislapys the inuput it gets from img2 and img1
        self.result = self.findChild(QLabel, "label_2")

        #when the pushbutton "image1" is clicked the function "img1" is executed
        self.image1.clicked.connect(self.img1)
        # when the pushbutton "image2" is clicked the function "img2" is executed
        self.image2.clicked.connect(self.img2)
        #here we set the label "result" as hidden
        self.result.setHidden(True)

        # Showing all the widgets we have used
        self.show()

    def img1(self):
        #here we set the widgets "image1","image2" and "instruction" as hidden
        self.image1.setHidden(True)
        self.image2.setHidden(True)
        self.instruction.setHidden(True)
        #we set the texts of the result label as "You are HUMAN"
        self.result.setText("You are HUMAN")
        #we set the widget "result" as unhide
        self.result.setHidden(False)

    def img2(self):
        # here we set the widgets "image1","image2" and "instruction" as hidden
        self.image1.setHidden(True)
        self.image2.setHidden(True)
        self.instruction.setHidden(True)
        # we set the texts of the result label as "You are BOT"
        self.result.setText("You are Bot")
        # we set the widget "result" as unhide
        self.result.setHidden(False)

app = QApplication(sys.argv)
UIWindow = mainwindow()
app.exec_()
