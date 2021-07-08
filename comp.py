import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv('D:\Python programes\cell_samples.csv')
X = dataset.iloc[:, 1:-1].values
Y = dataset.iloc[:, -1].values
print(X)
print(Y)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.25,random_state=1)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
#print(X_train)
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(X_train, Y_train)
from sklearn.svm import SVC
classifier2=SVC(kernel = 'rbf',random_state=0)
classifier2.fit(X_train, Y_train)

#z=classifier.predict(sc.transform([[30,87000]]))
#print(z)

predict=classifier.predict(X_test)
print(sc.inverse_transform(X_test))
print(predict)
predict=classifier.predict([3,2,2,1,7,8,9,2])
print(predict)
print(Y_test)
predict2=classifier2.predict(X_test)
print(predict2)
from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(Y_test, predict)
print(cm)
cm=confusion_matrix(Y_test, predict2)
print(cm)
print(accuracy_score(Y_test,predict))
print(accuracy_score(Y_test,predict2))