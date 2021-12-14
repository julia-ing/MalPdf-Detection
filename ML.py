from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

X = pd.read_csv(('output.csv')).T.iloc[1:].T
Y = pd.read_csv(('output.csv')).T.iloc[0]

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=0)

# clf = Sequential()
# clf = SVC(gamma='auto')
clf = RandomForestClassifier()
clf.fit(x_train, y_train)
joblib.dump(clf, './model.pkl')
