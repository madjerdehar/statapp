from scipy.io import mmread
with open('features-small.matrixMarket.mtx') as f:
    X = mmread(f)
X.shape
