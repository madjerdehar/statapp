from scipy.io import mmread
with open('features-small.matrixMarket.mtx') as f:
    X = mmread(f)
X.shape


import csv
cr=csv.reader(open("insults.csv","rb")
y=[int(row[0]) for row in cr]
