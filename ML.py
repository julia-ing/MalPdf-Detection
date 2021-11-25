from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from keras.models import Sequential, Model
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import io

def my_model(new_data):
  X = pd.read_csv(('output.csv')).T.iloc[1:].T
  Y = pd.read_csv(('output.csv')).T.iloc[0]

  x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=0)

  #clf = Sequential()
  #clf = SVC(gamma='auto')
  clf = RandomForestClassifier()
  clf.fit(x_train, y_train)

  predict = clf.predict(new_data)

  #score = accuracy_score(y_test, predict)
  #print('svm  prediction score : %s' % score)

  #print(predict)
  return predict

