# -*- coding: utf-8 -*-
"""diabets-decisiontrees-randomforest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oZqu2LKo7n6_bEfZoVQ3LNosa7dySKSr
"""

# Commented out IPython magic to ensure Python compatibility.
#import libraties

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import warnings

#import data
data = pd.read_csv("/content/diabetes.csv")
data

"""## Applied Models:

Decision Trees

Random Forest
"""

# Creat DataFrame
diabets_df = pd.DataFrame(data)

diabets_df.describe(include = "all")

"""### Data Visualization & Analysis"""

diabets_df.head()

diabets_df.shape

# Show detaile columns
diabets_df.info()

# How many missing value?
diabets_df.isna().sum()

## plot for numerical columns
Numerical = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness','Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
i = 0
while i <8:
    fig = plt.figure(figsize =[20,4])
    plt.subplot(1,2,1)   #(one row, two plots, firs one)
    sns.boxplot(x =Numerical[i], data = diabets_df )
    i+=1
    if i==8:
        break
    plt.subplot(1,2,2)
    sns.boxplot(x =Numerical[i], data = diabets_df)
    i+=1

    plt.show()

# histogram graphics
diabets_df.hist(bins=50,figsize=(20,15))
plt.show()

diabets_df3 = diabets_df.copy()

## Show correlation
fig, ax = plt.subplots(figsize = (20, 12)) #Size of plot
ax = sns.heatmap(diabets_df3.corr(),cmap='RdBu_r',cbar=True,annot=True,linewidths=0.5,ax=ax)
plt.show()

"""###  Best correlation for Glucose"""

#correlation
diabets_df3.corr()

diabets_df3.corr()['Outcome'].sort_values(ascending=False) #Correlation for get information

"""#### Scatter matrix of uncleaned data¶

"""

sns.pairplot(diabets_df3,hue='Outcome')

# clear outlier data
for col in ['Glucose','Insulin','SkinThickness']:
    median_col = np.median(diabets_df3[diabets_df3[col].notna()][col])
    diabets_df3[col] = diabets_df3[col].fillna(median_col)
for col in ['BMI','BloodPressure']:
    mean_col = np.mean(diabets_df3[diabets_df3[col].notna()][col])
    diabets_df3[col] = diabets_df3[col].fillna(mean_col)

#histogram
diabets_df3.hist(bins=50,figsize=(20,15))
plt.show()

"""## Creating & Training Decision Trees Model"""

# Sellecting features
X = pd.DataFrame(diabets_df3, columns = ["Glucose", "BloodPressure", "SkinThickness", "BMI", "DiabetesPedigreeFunction", "Age"])
Y = diabets_df3.Outcome.values.reshape(-1,1)

# Splitting the data
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.3 ,random_state = 1)

"""### Modeling use gini"""

clf = DecisionTreeClassifier(max_depth = 3)
clf = clf.fit(X_train,Y_train )
y_pred = clf.predict(X_test)

print("Accuracy: ", metrics.accuracy_score(Y_test, y_pred))

confusion_matrix(Y,clf.predict(X))

# Show plot for confusion matrix
cm = confusion_matrix(Y, clf.predict(X))
fig , ax = plt.subplots(figsize = (8,8))
ax.imshow(cm)
ax.grid(False)
ax.xaxis.set(ticks = (0,1) , ticklabels = ("predicted 0s", "predicted 1s"))
ax.yaxis.set(ticks = (0,1) , ticklabels = ("Actual 0s", "Actual 1s"))
ax.set_ylim(1.5 , -0.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i , cm[i,j], ha = "center" , va = "center", color = "red")
plt.show()

# Calculate classification
print(classification_report(Y, clf.predict(X)))

"""###  use entropy"""

clf = DecisionTreeClassifier(criterion = "entropy",max_depth = 3)
clf = clf.fit(X_train,Y_train )
y_pred = clf.predict(X_test)

print("Accuracy: ", metrics.accuracy_score(Y_test, y_pred))

confusion_matrix(Y,clf.predict(X))

# Show plot for confusion matrix
cm = confusion_matrix(Y, clf.predict(X))
fig , ax = plt.subplots(figsize = (8,8))
ax.imshow(cm)
ax.grid(False)
ax.xaxis.set(ticks = (0,1) , ticklabels = ("predicted 0s", "predicted 1s"))
ax.yaxis.set(ticks = (0,1) , ticklabels = ("Actual 0s", "Actual 1s"))
ax.set_ylim(1.5 , -0.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i , cm[i,j], ha = "center" , va = "center", color = "red")
plt.show()

"""### Creating & Training Random Forest Model"""

# Sellecting features
X = pd.DataFrame(diabets_df3, columns = ["Glucose", "BloodPressure", "SkinThickness", "BMI", "DiabetesPedigreeFunction", "Age"])
Y = diabets_df3.Outcome.values.reshape(-1,1)

# Splitting the data
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.3 ,random_state = 1)

"""### Modeling"""

clf = RandomForestClassifier(n_estimators = 15,max_depth = 3)
clf = clf.fit(X_train,Y_train )
y_pred = clf.predict(X_test)

print("Accuracy: ", metrics.accuracy_score(Y_test, y_pred))

confusion_matrix(Y,clf.predict(X))

# Show plot for confusion matrix
cm = confusion_matrix(Y, clf.predict(X))
fig , ax = plt.subplots(figsize = (8,8))
ax.imshow(cm)
ax.grid(False)
ax.xaxis.set(ticks = (0,1) , ticklabels = ("predicted 0s", "predicted 1s"))
ax.yaxis.set(ticks = (0,1) , ticklabels = ("Actual 0s", "Actual 1s"))
ax.set_ylim(1.5 , -0.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i , cm[i,j], ha = "center" , va = "center", color = "red")
plt.show()

# Calculate classification
print(classification_report(Y, clf.predict(X)))

"""### Conclusion:Best Algorithm is Random Forest
Randon Forest Accuracy: 0.7965367965367965

Decision Trees Accuracy: 0.7705627705627706
"""