# predictGUI.py by Comrade Akko

import sys
from PyQt5.QtWidgets import (QApplication, QGridLayout, QPushButton, QWidget, 
        QVBoxLayout, QGroupBox, QHBoxLayout, QVBoxLayout, QLineEdit, QComboBox,
        QDialog, QLabel, QTableWidget, QTabWidget, QTextEdit, QTableWidgetItem,
        QCheckBox, QScrollArea)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from regression import *

# the app itself
class App(QDialog):
    def __init__(self, parent = None):
        super(App, self).__init__(parent)

        self.title = "DALI app data regressor"

        # initialize the attribute list
        attriList = ["heightInches", "happiness", 
        "stressed", "sleepPerNight", "socialDinnerPerWeek", 
        "alcoholDrinksPerWeek", "caffeineRating", "affiliated", 
        "numOfLanguages", "gymPerWeek", "hoursOnScreen"]

        # create group boxes
        self.createOutcomeBox(attriList)
        self.createAttriLabelBox()
        self.createErrorBox()
        self.createScrollBox(attriList)
        self.createCalcBox()


        mainLayout = QGridLayout()
        mainLayout.addLayout(self.outcomeBox, 0, 0)
        mainLayout.addLayout(self.attriLabelBox, 1, 0)
        mainLayout.addLayout(self.errorBox, 2, 0)
        mainLayout.addLayout(self.scrollBox, 3, 0)
        mainLayout.addLayout(self.calcBox, 4, 0)

        self.setLayout(mainLayout)

        # initialize the UI
        self.initUI()

    # initializes the UI
    def initUI(self):
        self.setWindowTitle(self.title)
        
        self.show()

    # create a outcome selector box
    def createOutcomeBox(self, attriList):
        self.outcomeBox = QHBoxLayout()

        #create combo box and label widgets
        outcomeCombo = QComboBox()
        outcomeCombo.addItems(attriList)

        outcomeLabel = QLabel("&Outcome variable:")
        outcomeLabel.setBuddy(outcomeCombo)

        # add all the widgets to the box
        self.outcomeBox.addWidget(outcomeLabel)
        self.outcomeBox.addStretch(1)
        self.outcomeBox.addWidget(outcomeCombo)
    
    # create a box that contains buttons and labels
    def createAttriLabelBox(self):
        self.attriLabelBox = QHBoxLayout()

        # create an attribute label
        attributeLab = QLabel("Attributes:")

        # create both add and remove buttons
        addButton = QPushButton('Add', self)
        addButton.setToolTip('Adds more attribute boxes')
        # addButton.clicked.connect(self.---)

        rmButton = QPushButton('Remove', self)
        rmButton.setToolTip('Removes more attribute boxes')
        # rmButton.clicked.connect(self, ---)

        # add all the widgets to the box
        self.attriLabelBox.addWidget(attributeLab)
        self.attriLabelBox.addStretch(1)
        self.attriLabelBox.addWidget(addButton)
        self.attriLabelBox.addWidget(rmButton)

    # create an error box
    def createErrorBox(self):
        self.errorBox = QHBoxLayout()

        # create error label        
        errorLabel = QLabel(' ')

        self.errorBox.addWidget(errorLabel)

    # creates a scroll box for attribute boxes
    def createScrollBox(self, attriList):
        self.scrollBox = QVBoxLayout()
        
        # create box layout within the box
        scrollInbox = QVBoxLayout()

        # create the attribute selecting attribute
        attriCombo = QComboBox()
        attriCombo.addItems(attriList)

        scrollInbox.addWidget(attriCombo)

        # create scroll area widget
        scrollArea = QScrollArea()
        scrollArea.setLayout(scrollInbox)

        # set box layout
        self.scrollBox.addWidget(scrollArea)

    # create box that contains calculate button
    def createCalcBox(self):
        self.calcBox = QHBoxLayout()

        # create calculate button
        calcButton = QPushButton('Model Regression', self)
        calcButton.setToolTip("Calculates regression models")
        # calcButton.clicked.connect(self, ---)

        self.calcBox.addWidget(calcButton)

    # create 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())  