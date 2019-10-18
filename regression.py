#regression.py by Comrade Akko

import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.pipeline import make_pipeline
from sklearn import metrics

# performs simple linear regression based on specified attribute and label
def simpleLinearReg(attribute, label):
    # get the path to the current folder
    dataPath = os.getcwd() + "\\data\\DALI_Data-Anon.json"

    # download the dataframe
    data = pd.read_json(dataPath)

    # reshape the specified values
    x = data[attribute].values.reshape(-1,1)
    y = data[label].values.reshape(-1,1)

    # split the data into training and testing sets with 80% training and 20% testing
    xTrain, xTest, yTrain, yTest = train_test_split(x,y, test_size = 0.2, random_state = 0)

    # use regression 
    regressor = LinearRegression()
    regressor.fit(xTrain, yTrain)

    yPred = regressor.predict(xTest)

    print("Mean Absolute Error:", metrics.mean_absolute_error(yTest, yPred))  
    print("Mean Squared Error:", metrics.mean_squared_error(yTest, yPred))  
    print("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(yTest, yPred)))

    return

# performs polynomial regression based on specified attribute and label
def polyReg(attribute, label, degreeNum):
    # get the path to the current folder
    dataPath = os.getcwd() + "\\data\\DALI_Data-Anon.json"

    # download the dataframe
    data = pd.read_json(dataPath)

    # reshape the specified values
    x = data[attribute].values.reshape(-1,1)
    y = data[label].values.reshape(-1,1)

    # split the data into training and testing sets with 80% training and 20% testing
    xTrain, xTest, yTrain, yTest = train_test_split(x,y, test_size = 0.2, random_state = 0)

    # use regression 
    poly = PolynomialFeatures(degreeNum)

    xTrainPoly = poly.fit_transform(xTrain)

    model = LinearRegression()
    model.fit(xTrainPoly, yTrain)

    xTestPoly = poly.fit_transform(xTest)

    yPolyPred = model.predict(xTestPoly)

    print("Mean Absolute Error:", metrics.mean_absolute_error(yTest, yPolyPred))
    print("Mean Squared Error:", metrics.mean_squared_error(yTest, yPolyPred))
    print("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(yTest, yPolyPred)))

    return

simpleLinearReg("stressed", "happiness")
polyReg("stressed", "happiness", 10)


# # how to use the predictor
# xnew =[[10.0]]
# ynew = regressor.predict(xnew)
# print("One instance prediction is", ynew[0][0])