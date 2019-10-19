# predictGUI.py by Comrade Akko

import sys
from PyQt5.QtWidgets import (QApplication, QGridLayout, QWidget, 
        QVBoxLayout, QGroupBox, QHBoxLayout, QVBoxLayout, QDialog, 
        QLineEdit, QComboBox, QLabel, QScrollArea, QPushButton)
from PyQt5.QtCore import pyqtSlot
from sklearn.preprocessing import PolynomialFeatures 
from regression import *

# the app itself
class App(QDialog):
    def __init__(self, parent = None):
        super(App, self).__init__(parent)

        self.title = "DALI app data regressor"
        self.attriNum = 0
        self.currOutcome = " "

        # initialize the attribute list
        self.attriList = ["heightInches", "happiness", 
        "stressed", "sleepPerNight", "socialDinnerPerWeek", 
        "alcoholDrinksPerWeek", "caffeineRating", "affiliated", 
        "numOfLanguages", "gymPerWeek", "hoursOnScreen"]

        # initialize the variable list
        self.variabList = []

        # initialize the regression results
        self.res = Result()

        # create group boxes
        self.createOutcomeBox()
        self.createScrollBox()
        self.createAttriLabelBox()
        self.createErrorBox()
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
    def createOutcomeBox(self):
        self.outcomeBox = QHBoxLayout()

        #create combo box and label widgets
        outcomeCombo = QComboBox()
        outcomeCombo.addItems(self.attriList)

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
        addButton.clicked.connect(self.clickAdd)

        rmButton = QPushButton('Remove', self)
        rmButton.setToolTip('Removes more attribute boxes')
        rmButton.clicked.connect(self.clickRM)

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
    def createScrollBox(self):
        self.scrollBox = QVBoxLayout()
        
        # create central widget
        central = QWidget()

        # create scroll area widget
        scrollArea = QScrollArea()
        scrollArea.setWidget(central)
        scrollArea.setWidgetResizable(True)

        # create box layout within the box
        scrollInbox = QVBoxLayout(central)

        # set box layout
        self.scrollBox.addWidget(scrollArea)

    # create box that contains calculate button
    def createCalcBox(self):
        self.calcBox = QHBoxLayout()

        # create calculate button
        modelButton = QPushButton('Model Regression', self)
        modelButton.setToolTip("Calculates regression models")
        modelButton.clicked.connect(self.clickModel)

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

        # create central widget
        central2 = QWidget()

        # create scroll area widget
        scrollSpace = QScrollArea()
        scrollSpace.setWidget(central2)
        scrollSpace.setWidgetResizable(True)
        
        # create box layout within the box
        scrollInbox = QVBoxLayout(central2)

        # add the scroll space to the box
        self.resuScroll.addWidget(scrollSpace)
        

    # creates a box for predict button
    def createPredictBox(self):
        self.predBox = QHBoxLayout()

        # create predict button
        predButton = QPushButton('Predict', self)
        predButton.setToolTip("Predicts outcome based on model")
        predButton.clicked.connect(self.clickPredict)

        self.predBox.addWidget(predButton)

    # create box that contains outcome prediction
    def createOutcomePred(self):
        self.outcomePred = QHBoxLayout()

        outcomeLabel = QLabel('Outcome prediction:')

        self.outcomePred.addWidget(outcomeLabel)

    
    # what to do when the add button is pushed
    @pyqtSlot()
    def clickAdd(self):
        # if there are too many attribute boxes, display error
        if self.attriNum <= 9:
            # add a new combo box
            newCombo = QComboBox()
            newCombo.addItems(self.attriList)
            self.scrollBox.itemAt(0).widget().widget().layout().addWidget(newCombo)
            self.attriNum += 1

        else:
            error1 = "Error: Too many attributes. Leave as be or decrease."
            self.errorBox.itemAt(0).widget().setText(error1)

    # what to do when the remove button is pushed
    @pyqtSlot()
    def clickRM(self):
        # if there are boxes to remove, remove them
        if self.attriNum > 0:
            # clear the error box
            error0 = " "
            self.errorBox.itemAt(0).widget().setText(error0)

            # remove the newest combo box
            self.scrollBox.itemAt(0).widget().widget().layout().itemAt(self.attriNum-1).widget().deleteLater()
            self.attriNum -= 1

    # what to do when the modelling button is pushed
    @pyqtSlot()
    def clickModel(self):
        # make sure there are attributes to model with
        if self.attriNum > 0:
            # make sure there are no duplicates with either the outcome variable or the attributes
            self.variabList.clear()
            self.variabList.append(self.outcomeBox.itemAt(2).widget().currentText())

            noDupli = True
            i = 0

            # while there attributes to be appended and there are no duplicates
            while i < self.attriNum and noDupli:
                # append the selected attribute
                comboText = self.scrollBox.itemAt(0).widget().widget().layout().itemAt(i).widget().currentText()
                self.variabList.append(comboText)

                i+=1

                # if the length of the set of the current list is not equal to the length of the current list
                if len(self.variabList) != len(set(self.variabList)):
                    noDupli = False
            
            # if there was no duplicates, proceed with the current list of outcome variable and attributes
            if noDupli:
                # clear the error box
                error0 = " "
                self.errorBox.itemAt(0).widget().setText(error0)

                # if there was only one attribute selected perform single attribute regression
                if self.attriNum == 1:
                    self.res = singleAttriReg(self.variabList[0], self.variabList[1])
                
                # otherwise perform multi attribute regression
                else:
                    attributes = self.variabList[1:]
                    self.res = multiAttriReg(attributes, self.variabList[0])
                
                # post the results
                model = "Model used: " + self.res.strat
                rmse = "RMSE: " + str(self.res.rmse)

                self.modelBox.itemAt(0).widget().setText(model)
                self.rmseBox.itemAt(0).widget().setText(rmse)

                # clear the previous resuScroll
                for i in reversed(range(self.resuScroll.itemAt(0).widget().widget().layout().count())): 
                    self.resuScroll.itemAt(0).widget().widget().layout().itemAt(i).widget().setParent(None)

                # set the current outcome variable so it doesn't get affected by changing
                # on the screen elsewhere
                self.currOutcome = self.variabList[0]

                # create appropriate attribute variable input editors
                for i in range(self.attriNum):
                    placeholder = QWidget()

                    inputBox = QHBoxLayout()
                    attributes = self.variabList[1:]

                    label = QLabel(attributes[i] + ": ")
                    lineEdit = QLineEdit()
                    inputBox.addWidget(label)
                    inputBox.addWidget(lineEdit)

                    placeholder.setLayout(inputBox)

                    self.resuScroll.itemAt(0).widget().widget().layout().addWidget(placeholder)

            # if there were duplicates post error
            else:
                error3 = "Error: no duplicate variables allowed"
                self.errorBox.itemAt(0).widget().setText(error3)

        else:
            error2 = "Error: cannot model without attribute variables"
            self.errorBox.itemAt(0).widget().setText(error2)

     # what to do when the prediction button is pushed
    @pyqtSlot()
    def clickPredict(self):
        attriCount = self.resuScroll.itemAt(0).widget().widget().layout().count()
        newAttriList = []

        # make sure there are attributes to use to predict
        if attriCount > 0:
            # make sure all the inputted texts are integers
            numbers = True
            for j in range(attriCount):
                try:
                    num = int(self.resuScroll.itemAt(0).widget().widget().layout().itemAt(j).widget().layout().itemAt(1).widget().text())
                    newAttriList.append(num)
                except ValueError:
                    numbers = False
            
            # if all inputs were integers
            if numbers:
                # clear error message
                notErr = " "
                self.errorTwo.itemAt(0).widget().setText(notErr)

                # predict
                newAttriList = [newAttriList]

                # to account for special cases where polynomials screw up the code
                if self.res.strat == "polynomial regression":
                    poly = PolynomialFeatures(5)
                    newAttriList = poly.fit_transform(newAttriList)
                    prediction = self.res.reg.predict(newAttriList)

                else:
                    prediction = self.res.reg.predict(newAttriList)

                # if there is only 1 attribute
                if attriCount == 1:
                    # set results of prediction
                    predResult = "Outcome - " + self.currOutcome + ": " + str(round(prediction[0][0],4))
                    self.outcomePred.itemAt(0).widget().setText(predResult)

                # if there are more than 1 attribute
                else:
                    # set results of prediction
                    predResult = "Outcome - " + self.currOutcome + ": " + str(round(prediction[0],4))
                    self.outcomePred.itemAt(0).widget().setText(predResult)

            # set error accordingly
            else:
                error5 = "Error: One or more inputs not integers"
                self.errorTwo.itemAt(0).widget().setText(error5)
        
        # set error accordingly
        else:
            error4 = "Error: No attributes to use to predict."
            self.errorTwo.itemAt(0).widget().setText(error4)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())  