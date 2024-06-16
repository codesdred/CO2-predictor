from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction', methods=["POST", "GET"])
def prediction(): 
    if request.method == 'POST':
        #fetching code and year from website
        country_code = request.form['code']
        yr = request.form['year']
        type = request.form['type']
        if(yr.isnumeric()):
            yr=int(yr)
            #fetching dataset
            dataset = pd.read_csv('emissiondata.csv')
            #processing dataset
            X1 = dataset.iloc[:,4].values
            X2 = dataset.iloc[:,6:-1].values
            X = np.concatenate((X1.reshape(-1,1),X2),axis=1)
            key = dataset.iloc[:,2].values
            X = np.concatenate((key.reshape(-1,1),X),axis=1)
            y = dataset.iloc[:,5].values
            #processing dataset
            X1 = dataset.iloc[:,4].values
            X2 = dataset.iloc[:,6:-1].values
            X = np.concatenate((X1.reshape(-1,1),X2),axis=1)
            key = dataset.iloc[:,2].values
            X = np.concatenate((key.reshape(-1,1),X),axis=1)
            y = dataset.iloc[:,5].values
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
            #Handling missing values
            from sklearn.impute import SimpleImputer
            imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
            X[: , 1:-1] = imputer.fit_transform(X[: , 1:-1])
            #Handling missing values
            from sklearn.impute import SimpleImputer
            imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
            X[: , 1:-1] = imputer.fit_transform(X[: , 1:-1])
            #Feature Scaling
            from sklearn.preprocessing import StandardScaler
            sc = StandardScaler()
            X[:,2:] = sc.fit_transform(X[:,2:])
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
            yplttest = []
            for year in range(1750,yr+1):
                Xplt.append(year)
                predX = Xnew[0]
                predX[0] = year
                predX = predX.reshape(-1,4)
                predX = poly_reg.transform(predX)
                yplttest.append(lin_reg.predict(predX))
            yplt=[]
            for item in yplttest:
                yplt.append(item[0])
            datatest = dataset.iloc[:,1:3].values
            country_name = datatest[datatest[:,1]==country_code][0][0]

            return render_template("form.html", X = Xplt, y = yplt, val = yplt[len(yplt)-1], country = country_name, year = yr, type = type)
        else:
            return render_template("form.html", country = '_', year = '_', val = '_', type="line")

    else:
        return render_template("form.html", country = '_', year = '_', val = '_', type="line")

