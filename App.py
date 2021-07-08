import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv('D:\Python programes\cell_samples.csv')
X = dataset.iloc[:, 1:-1].values
Y = dataset.iloc[:, -1].values
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.25,random_state=1)
from sklearn.svm import SVC
classifier=SVC(kernel = 'rbf',random_state=0)
classifier.fit(X_train, Y_train)
def cal(a,b,c,d,e,f,g,h):
    predict1=classifier.predict([[a,b,c,d,e,f,g,h]])
    return predict1