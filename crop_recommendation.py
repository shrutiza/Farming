# -*- coding: utf-8 -*-
"""Crop Recommendation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gXBKN06Qh2IO6FY30ZRZYjp9pRBbq4IE
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/My Drive/Colab Notebooks/crop_yield_dataset.csv')

df

df.dropna(inplace = True)

df.head()

df.min()

df.max()

df.info()

df.to_csv('crop_yield_dataset.csv')

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
for i in df:
  if df[i].dtype == 'object':
    df[i] = le.fit_transform(df[i].astype(str))
  else:
    continue

X = df.drop('Crop_Type', axis = 1)
y = df['Crop_Type']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import f1_score

model = RandomForestClassifier()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(y_pred[:65])

from sklearn.metrics import recall_score, accuracy_score, classification_report

accuracy = accuracy_score(y_pred, y_test)

print(accuracy)

print(classification_report(y_pred, y_test))
print('F1 Score: ', f1_score(y_pred, y_test, average = 'macro'))

from sklearn.metrics import confusion_matrix
confmat = confusion_matrix(y_true = y_test, y_pred = y_pred)
print(confmat)

fig, ax = plt.subplots(figsize=(12.5, 12.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.30)
for i in range (confmat.shape[0]):
  for j in range (confmat.shape[1]):
    ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')
plt.title("Using the Random Forest at 100% accuracy prediction from the Kaggle Crop Prediction dataset for identifying false positives, false negatives and true positives, true negatives. Others - 0.")
plt.xlabel('Predicted')
plt.ylabel('True')

df.to_csv('data_new.csv')

y=0; a=1; b=2; c=3; d=4; e=5; f=6; g=7; h=8; i=9; j=10;

import pickle

with open('crop_yield_model.pkl', 'wb') as fh:
  pickle.dump(model, fh)