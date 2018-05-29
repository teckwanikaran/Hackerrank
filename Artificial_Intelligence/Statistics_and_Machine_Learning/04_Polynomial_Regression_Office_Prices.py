from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Set data
observed_features, number_of_rows = map(int, input().split())
# getting the values for number of features and the number of rows

# Getting the training data and appending it in the X_train and y_train variables
X_train = []
y_train = []
for _ in range(number_of_rows):
    x_constant = [0] # Adding a constant to create a vector
    data_points = list(map(float, input().split())) 
    for index in range(len(data_points)):
        if index < observed_features:
            x_constant.append(data_points[index])
        else:
            y_train.append(data_points[index])
    # Adding the values of x_constant to X_train
    X_train.append(x_constant)

# Getting the test data and appending it in the X_test variable
test_rows = int(input())
X_test = []
for _ in range(test_rows):
    x_constant = [0] # Adding a constant to create a vector
    test_data_points = list(map(float, input().split()))
    for index in range(len(test_data_points)):
        x_constant.append(test_data_points[index])
    # Adding the values of x_constant to X_test
    X_test.append(x_constant)
    
# Creating the Polynomial feature
polynomial_model = PolynomialFeatures(degree = 3)

# Creating the model
housing_model = linear_model.LinearRegression()
housing_model.fit(polynomial_model.fit_transform(np.array(X_train)), y_train)

# Predicting the y_test for X_test
y_test = housing_model.predict(polynomial_model.fit_transform(np.array(X_test)))

# Output the y_test
for each in range(len(y_test)):
    print(round(y_test[each], 2))
