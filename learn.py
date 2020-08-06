#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 21:12:56 2020

@author: kenton
"""

# learning

import pandas as pd
from webscrape import scrapeWeather
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

june = scrapeWeather('2020','06')
#july = scrapeWeather('2020','07')
weather = june


#import weather rating data
filename = 'data/sunsetquali.csv'
sunsetq = pd.read_csv(filename)
sunsetq['Date'] = pd.to_datetime(sunsetq['Date'])

X = weather.iloc[:,1:].values
y = sunsetq.iloc[:, 1].values[0:30]

#algorithm
l_reg = linear_model.LinearRegression()

#plt.scatter(X.T[7],y)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

#train 
model = l_reg.fit(X_train, y_train)
predictions = model.predict(X_test)


print("Predictions: ", predictions)
print("R^2 value: ", l_reg.score(X,y))
print("coedd: ", l_reg.coef_)
print("intercept: ", l_reg.intercept_)

