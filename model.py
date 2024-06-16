import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#fetching dataset
dataset = pd.read_csv('emissiondata.csv')

#processing dataset
X1 = dataset.iloc[:,4].values
X2 = dataset.iloc[:,6:-1].values
X = np.concatenate((X1.reshape(-1,1),X2),axis=1)
key = dataset.iloc[:,2].values
X = np.concatenate((key.reshape(-1,1),X),axis=1)
y = dataset.iloc[:,5].values

#Handling missing values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
X[: , 1:-1] = imputer.fit_transform(X[: , 1:-1])

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X[:,2:] = sc.fit_transform(X[:,2:])

#fetching code and year from website
country_code = 'AF'
year = 3000

#shortlisting dataset
Xnew = X[X[:,0]==country_code][:,1:]
ynew = y[X[:,0]==country_code]

#Polynomial Regression on dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(Xnew)
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_poly,ynew)

#Creating predictions from 1750->{year}
Xplt = []
yplt = []
for year in range(1750,year+1):
  Xplt.append(year)
  predX = Xnew[0]
  predX[0] = year
  predX = predX.reshape(-1,4)
  predX = poly_reg.transform(predX)
  yplt.append(lin_reg.predict(predX))
Xplt = np.array(Xplt)
yplt = np.array(yplt)

