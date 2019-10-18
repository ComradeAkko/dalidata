#regression.py by Comrade Akko

import pandas as pd
import numpy as np
import os
from sklearn import tree
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet, BayesianRidge
from sklearn.preprocessing import PolynomialFeatures 
from sklearn import metrics


# stores the name of the strat, the regressor itself, and the root mean square error
class Result:
    def __init__(self):
            self.reg = 0
            self.rmse = 0
            self.strat = "nothing"


# performs simple linear regression based on specified attribute and label
def simpleLinearReg(attribute, label):
    # get the path to the current folder
    dataPath = os.getcwd() + "\\data\\DALI_Data-Anon.json"

    # download the dataframe
    data = pd.read_json(dataPath)

    # reshape the specified values and get them
    x = data[attribute].values.reshape(-1,1)
    y = data[label].values.reshape(-1,1)

    # split the data into training and testing sets with 80% training and 20% testing
    xTrain, xTest, yTrain, yTest = train_test_split(x,y, test_size = 0.2, random_state = 0)

    # use regression 
    regressor = LinearRegression()
    regressor.fit(xTrain, yTrain)

    yPred = regressor.predict(xTest)

    print("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(yTest, yPred)))

    return

# performs polynomial regression based on specified attribute and label
def polyReg(attribute, label, degreeNum):
    # get the path to the current folder
    dataPath = os.getcwd() + "\\data\\DALI_Data-Anon.json"

    # download the dataframe
    data = pd.read_json(dataPath)

    # reshape the specified values and get them
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

    print("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(yTest, yPolyPred)))

    return

# performs multi-linear, ridge, lasso, elastic net, ridge, bayesian ridge and decision tree regression
# and returns the regression strategy with the least root mean squared error
def multiAttriReg(attriList, label):
    # get the path to the current folder
    dataPath = os.getcwd() + "\\data\\DALI_Data-Anon.json"

    # download the dataframe
    data = pd.read_json(dataPath)

    # check which columns have null values in them
    data.isnull().any()

    # remove the null values from column:
    data = data.fillna(method='ffill')

    # reshape the specified values and get them
    x = data[attriList].values
    y = data[label].values

    # split the data into training and testing sets with 80% training and 20% testing
    xTrain, xTest, yTrain, yTest = train_test_split(x,y, test_size = 0.2, random_state = 0)


    # use multi-linear regression 
    multiReg = LinearRegression()
    multiReg.fit(xTrain, yTrain)

    # predict using the test data
    yMultiPred = multiReg.predict(xTest)

    # calculate the RMSE for multi-linear regression
    multiRMSE = np.sqrt(metrics.mean_squared_error(yTest, yMultiPred))
    
    #initialize the result
    res = Result()

    # record the current regression model, name and rmse into results
    res.strat = "multi-linear regression"
    res.reg = multiReg
    res.rmse = multiRMSE


    # use ridge regression and repeat
    ridgeReg = Ridge()
    ridgeReg.fit(xTrain, yTrain)
    yRidgePred = ridgeReg.predict(xTest)
    ridgeRMSE = np.sqrt(metrics.mean_squared_error(yTest, yRidgePred))

    # if the ridge RMSE is lesser than the previous model, overwrite the results
    if ridgeRMSE < res.rmse:
        res.strat = "ridge regression"
        res.reg = ridgeReg
        res.rmse = ridgeRMSE


    # use lasso regression and repeat
    lassoReg = Lasso()
    lassoReg.fit(xTrain, yTrain)
    yLassoPred = lassoReg.predict(xTest)
    lassoRMSE = np.sqrt(metrics.mean_squared_error(yTest, yLassoPred))

    # if the lasso RMSE is lesser than the previous model, overwrite the results
    if lassoRMSE < res.rmse:
        res.strat = "lasso regression"
        res.reg = lassoReg
        res.rmse = lassoRMSE


    # use elastic net regression and repeat
    elasticNetReg = ElasticNet()
    elasticNetReg.fit(xTrain, yTrain)
    yElasticNetPred = elasticNetReg.predict(xTest)
    elasticNetRMSE = np.sqrt(metrics.mean_squared_error(yTest, yElasticNetPred))

    # if the elastic net RMSE is lesser than the previous model, overwrite the results
    if elasticNetRMSE < res.rmse:
        res.strat = "lasso regression"
        res.reg = lassoReg
        res.rmse = lassoRMSE


    # use bayesian ridge regression and repeat
    bayesianReg = BayesianRidge()
    bayesianReg.fit(xTrain, yTrain)
    yBayesianPred = bayesianReg.predict(xTest)
    bayesianRMSE = np.sqrt(metrics.mean_squared_error(yTest, yBayesianPred))

    # if the bayesian ridge RMSE is lesser than the previous model, overwrite the results
    if bayesianRMSE < res.rmse:
        res.strat = "bayesian ridge regression"
        res.reg = bayesianReg
        res.rmse = bayesianRMSE


    # use decision tree regression and repeat
    decTreeReg = tree.DecisionTreeRegressor()
    decTreeReg.fit(xTrain, yTrain)
    yDecTreePred = decTreeReg.predict(xTest)
    decTreeRMSE = np.sqrt(metrics.mean_squared_error(yTest, yDecTreePred))

    # if the bayesian ridge RMSE is lesser than the previous model, overwrite the results
    if decTreeRMSE < res.rmse:
        res.strat = "decision tree regression"
        res.reg = decTreeReg
        res.rmse = decTreeRMSE

    # return the result
    return res


aList = ["sleepPerNight", "alcoholDrinksPerWeek", "caffeineRating", "gymPerWeek", "hoursOnScreen", "socialDinnerPerWeek", "heightInches", "affiliated", "happiness"]

rez = multiAttriReg(aList, "stressed")

print(rez.rmse)
# # how to use the predictor
# xnew =[[10.0]]
# ynew = regressor.predict(xnew)
# print("One instance prediction is", ynew[0][0])

# # how to use the predictor
# xnew =[[10, 2, 3]]
# ynew = regressor.predict(xnew)
# print("One instance prediction is", ynew[0])