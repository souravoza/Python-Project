# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13V3APDtbzzB6gOtbEvj8YyVjxnO_f7qU
"""

#import
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

diabetes_dataset = pd.read_csv('/content/diabetes.csv')

pd.read_csv?

diabetes_dataset.head()

diabetes_dataset.shape

diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()

diabetes_dataset.groupby('Outcome').mean()

x = diabetes_dataset.drop(columns = 'Outcome', axis=1)
y = diabetes_dataset['Outcome']

print(x)

print(y)

"""traning and test"""

scaler = StandardScaler()

scaler.fit(x)

"""model training -> logistics regression"""

standardized_data = scaler.transform(x)

scaler.fit(x)

print(standardized_data)

x = standardized_data
y = diabetes_dataset['Outcome']

print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, stratify=y, random_state=2)

(x.shape, x_train.shape, x_test.shape)

classifier = svm.SVC(kernel='linear')

classifier.fit(x_train, y_train)

x_train_prediction = classifier.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)

print('accuracy score of the traning data : ', training_data_accuracy)

x_test_prediction = classifier.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction, y_test)

print('accuracy score of the test data : ', test_data_accuracy)

input_data = (4,110,92,0,0,37.6,0.191,30)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)

if(prediction[0] == 0):
  print('the person is not diabetic')
else:
  print('the person is diabetic')

