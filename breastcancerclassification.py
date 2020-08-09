# -*- coding: utf-8 -*-
"""BreastCancerClassification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PRI3B_K34E5faNvSciiMKSvzuTxa2l04

Importing Libraries
"""

import numpy as np
import pandas as pd

"""Import Dataset"""

data = pd.read_csv('breast_cancer.csv')
x = data.iloc[:, 1:-1].values
y = data.iloc[:, -1].values

"""Splitting the dataset into Training Set and Test Set"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.8)

"""Training Logistic Regression Model on the Dataset"""

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(x_train, y_train)

"""Predicting a Single Value"""

y_pred = classifier.predict(x_test)

"""Making the Confusion Matrix"""

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)

"""Calculating accuracy"""

print(accuracy_score(y_test, y_pred))