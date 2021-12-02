import joblib

def predict(new_data):
  model = joblib.load('./model.pkl')
  predict = model.predict(new_data)

  #score = accuracy_score(y_test, predict)
  #print('svm  prediction score : %s' % score)

  #print(predict)
  return predict

