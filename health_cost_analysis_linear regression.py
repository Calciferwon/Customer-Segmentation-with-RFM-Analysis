print("Hello, World!")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression


#Reading the dataset
dataset = pd.read_csv(r'D:\DATest_Monkey\Đỗ Thùy_test answer\viện phí.csv')
dataset = dataset.drop_duplicates()
df = pd.DataFrame(dataset)
df.head()

#information of dataset
df.info()

#define data
x = dataset[['bmi','age','children','gender','smoking','area']]
y = dataset['charges']

#linear regression model
model = LinearRegression()
model.fit(x, y)
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)

#print summary
X = sm.add_constant(x)
est = sm.OLS(y, X)
est2 = est.fit()
print(est2.summary())

#predict response
y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')

#define new data
x1 = dataset[['bmi','age','children','smoking']]
y1 = dataset['charges']

#linear regression model
model = LinearRegression()
model.fit(x1, y1)
model = LinearRegression().fit(x1, y1)
r_sq1 = model.score(x1, y1)

#print summary
X1 = sm.add_constant(x1)
est = sm.OLS(y, X1)
est2 = est.fit()
print(est2.summary())

#predict response
y_pred1 = model.predict(x1)
print('predicted response:', y_pred1, sep='\n')
