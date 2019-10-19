# DESIGN 
by Comrade Akko

## objectives

### 1st version
Trying to create an supervised learning model that takes using `DALI_Data-Anon.json` that takes in two values, creates a regressive model, and then allows the user to input a value to get the expected value. 

## plan

### 1st version
- Will probably use Python because its easy.

- Will try to create a GUI that allows user to perform predictions easily based on existing information

- if there is only one attribute specified, only simple linear and polynomial regression will be used. In the case of polynomial, the degree of the polynomial will be 5. I don't particularly have a reason for this other than time constraints.

- if many attributes are specified, multiple linear, ridge and lasso regression will be used.
- once attributes are inputted and confirmed, the regressor will calculate the train on 80% of the data, and test on the 20% of the data. Root mean squared errors will be compared and the strategy with the least error will be selected and returned. 

- once the most accurate regression is specified, the user is then able to calculate what the predicted value of any attribute inputted is.


## regression
1. Determine how many attributes there are

2. If only 1 attribute, use simple and polynomial.
3. Get the lesser RMSE determined from the regression model
4. Present it to user and also allow them to predict other values

Alternative:
2. If multiple attributes, use multi-linear, ridge, lasso, elastic net, bayesian ridge, and decision tree regression.
3. Determine the least RMSE.
4. Present it to use and also allow them to predict other values.
