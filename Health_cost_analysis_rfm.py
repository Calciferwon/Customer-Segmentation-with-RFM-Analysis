import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

#load data into pandas dataframe..
dataset = pd.read_csv(r'D:\DATest_Monkey\Đỗ Thùy_test answer\viện phí.csv')
df = pd.DataFrame(dataset)
df.head()

#information of dataset..
df.info()
df.describe()

#Set bmi, age, charges & children quantiles
def get_group(Q1, Q2, Q3, value):
    if value <= Q1:
        return '1'
    elif Q1 < value <= Q2:
        return '2'
    elif Q2 < value <= Q3:
        return '3'
    elif Q3 < value:
        return '4'
bmi_Q1, bmi_Q2, bmi_Q3 = df['bmi'].quantile([0.015,0.1838,0.472])
age_Q1, age_Q2, age_Q3 = df['age'].quantile([0.3,0.5,0.9])
char_Q1, char_Q2, char_Q3 = df['charges'].quantile([0.25,0.5,0.75])
chil_Q1, chil_Q2, chil_Q3 = df['children'].quantile([0.5, 0.95, 0.97])

bmi_group = []
for i in range(len(df)):
    bmi = df.iloc[i]['bmi']
    bmi_group.append(get_group(bmi_Q1, bmi_Q2, bmi_Q3, bmi)) 
df['bmi_group'] = bmi_group

age_group = []
for i in range(len(df)):
    age = df.iloc[i]['age']
    age_group.append(get_group(age_Q1, age_Q2, age_Q3, age)) 
df['age_group'] = age_group

char_group = []
for i in range(len(df)):
    char = df.iloc[i]['charges']
    char_group.append(get_group(char_Q1, char_Q2, char_Q3, char))
df['char_group'] = char_group

chil_group = []
for i in range(len(df)):
    chil = df.iloc[i]['children']
    chil_group.append(get_group(chil_Q1, chil_Q2, chil_Q3, chil))
df['chil_group'] = chil_group

#compute health_score & total_Score
df['health_score'] = df['bmi_group'] + df['age_group'] + df['char_group'] + df['smoking'].astype(str) + df['chil_group']
df['total_score'] = df.bmi_group.astype(int) + df.age_group.astype(int) + df.char_group.astype(int) + df['smoking'] + \
df['chil_group'].astype(int)
df.head()
print(df)

print(df.groupby('health_score')['charges'].mean())
print(df.groupby('total_score')['charges'].mean())

df.groupby('total_score')['charges'].mean().plot(kind='bar', colormap='Blues_r')
plt.plot()
plt.show()

df.groupby('total_score')['children'].mean().plot(kind='bar', colormap='Greens_r')
plt.plot()
plt.show()

df.groupby('total_score')['age'].mean().plot(kind='bar', colormap='Reds_r')
plt.plot()
plt.show()

df.groupby('total_score')['bmi'].mean().plot(kind='bar', colormap='Purples_r')
plt.plot()
plt.show()

print("Best Customers: ",len(df[df['total_score'].between(14, 15, inclusive = True)]))
print("Potential Customers: ",len(df[df['total_score'].between(12, 13, inclusive = True)]))
print("Smoking Warning: ",len(df[df['smoking']==1]))
print("Weight Warning: ",len(df[df['bmi_group']=='4']))
print("Big Health Spenders: ",len(df[df['char_group']=='4']))
print("Small Health Spenders: ",len(df[df['total_score']==5]))
print("Least Potential Customer: ",len(df[df['total_score'].between(4, 5, inclusive = True)]))
print('Normal Customers: ',len(df[df['total_score'].between(6, 10, inclusive = True)]))

df.query('total_score > 11', inplace=True)
print(df)
