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
        self.createResultsLabel()
        self.createModelLabel()
        self.createRMSEbox()
        self.createErrorTwo()
        self.createResuScroll()
        self.createPredictBox()
        self.createOutcomePred()

        # layout all the boxes
        mainLayout = QGridLayout()
        mainLayout.addLayout(self.outcomeBox, 0, 0)
        mainLayout.addLayout(self.attriLabelBox, 1, 0)
        mainLayout.addLayout(self.errorBox, 2, 0)
        mainLayout.addLayout(self.scrollBox, 3, 0)
        mainLayout.addLayout(self.calcBox, 4, 0)
        mainLayout.addLayout(self.resBox, 0, 1)
        mainLayout.addLayout(self.modelBox, 1, 1)
        mainLayout.addLayout(self.rmseBox, 2, 1)
        mainLayout.addLayout(self.errorTwo, 3, 1)
        mainLayout.addLayout(self.resuScroll, 4, 1)
        mainLayout.addLayout(self.predBox, 5, 1)
        mainLayout.addLayout(self.outcomePred, 6, 1)

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
        modelButton = QPushButton('Model Regression', self)
        modelButton.setToolTip("Calculates regression models")
        # calcButton.clicked.connect(self, ---)

        self.calcBox.addWidget(modelButton)

    # create box that contains the results label
    def createResultsLabel(self):
        self.resBox = QHBoxLayout()
        
        # create label
        resLabel = QLabel("Results:")

        self.resBox.addWidget(resLabel)

    # create box that contains the model label
    def createModelLabel(self):
        self.modelBox = QHBoxLayout()

        # create label
        modelLabel = QLabel("Model used:")
        self.modelBox.addWidget(modelLabel)

    # create box that contains rmse label
    def createRMSEbox(self):
        self.rmseBox = QHBoxLayout()

        rmseLabel = QLabel("RMSE:")
        self.rmseBox.addWidget(rmseLabel)

    # create box that contains error label 2
    def createErrorTwo(self):
        self.errorTwo = QHBoxLayout()
        
        errorTwoLabel = QLabel(" ")
        self.errorTwo.addWidget(errorTwoLabel)

    # creates a second scroll box for attribute boxes
    def createResuScroll(self):
        self.resuScroll = QVBoxLayout()
        
        # create box layout within the box
        scrollInbox = QVBoxLayout()

        # create scroll area widget
        scrollSpace = QScrollArea()
        scrollSpace.setLayout(scrollInbox)

        # set box layout
        self.resuScroll.addWidget(scrollSpace)

    # creates a box for predict button
    def createPredictBox(self):
        self.predBox = QHBoxLayout()

        # create predict button
        predButton = QPushButton('Predict', self)
        predButton.setToolTip("Predicts outcome based on model")
        # predButton.clicked.connect(self, ---)

        self.predBox.addWidget(predButton)

    # create box that contains outcome prediction
    def createOutcomePred(self):
        self.outcomePred = QHBoxLayout()

        outcomeLabel = QLabel('Outcome prediction:')

        self.outcomePred.addWidget(outcomeLabel)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())  