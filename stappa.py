from scipy.io import mmread
with open('features-small.matrixMarket.mtx') as f:
    X = mmread(f)
X.shape


import csv
with open("insults.csv", "rb") as f:
    y=[int(row[0]) for row in csv.reader(f)]

with open("insults.csv", "rb") as f:
    messages=[row[1] for row in csv.reader(f)]
    
    
---    
exemple SVM:
from sklearn import svm
X = [[0, 0], [1, 1]]
y = [0, 1]
clf.fit(X, y)  
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.0, kernel='rbf', max_iter=-1, probability=False, random_state=None,
shrinking=True, tol=0.001, verbose=False)
---
