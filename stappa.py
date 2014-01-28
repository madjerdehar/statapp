from scipy.io import mmread
with open('features-small.matrixMarket.mtx') as f:
    X = mmread(f)
X.shape


import csv
with open("insults.csv", "rb") as f:
    y=[int(row[0]) for row in csv.reader(f)]

with open("insults.csv", "rb") as f:
    messages=[row[1] for row in csv.reader(f)]
    
    
# ---    
# exemple SVM:
from sklearn import svm
clf = svm.SVC()
clf.fit(X, y)  
clf.predict(X)
