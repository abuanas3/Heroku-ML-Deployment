# importing required libraries
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


# loading and reading the dataset



# model building
x = pd.read_csv("mitbih_train.csv",header=None,usecols=range(187))
y = pd.read_csv("mitbih_train.csv",header=None,usecols=[187]).iloc[:,0]

print(y)
''' 
x_train = pd.read_csv("mitbih_train.csv",header=None,usecols=range(187))
y_train = pd.read_csv("mitbih_train.csv",header=None,usecols=[187]).iloc[:,0]

x_test = pd.read_csv("mitbih_test.csv",header=None,usecols=range(187))
y_test = pd.read_csv("mitbih_test.csv",header=None,usecols=[187]).iloc[:,0]'''


#fixing our data in x and y. Here y contains target data and X contains rest all the features.
#x= heart_df.drop(columns= 'target')
#y= heart_df.target

# splitting our dataset into training and testing for this we will use train_test_split library.
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.25, random_state=42)

#feature scaling
scaler= StandardScaler()
x_train_scaler= scaler.fit_transform(x_train)
x_test_scaler= scaler.fit_transform(x_test)

#----------------------------------------
'''from sklearn import svm
svm = svm.SVC()
svm.fit(x_train, y_train)
y_pred = svm.predict(x_test)'''
#=============================================

# creating K-Nearest-Neighbor classifier
model=RandomForestClassifier(n_estimators=20)
#model=KNeighborsClassifier(n_neighbors=7)

model.fit(x_train, y_train)
y_pred= model.predict(x_test)
p = model.score(x_test,y_test)
'''
model.fit(x_train_scaler, y_train)
y_pred= model.predict(x_test_scaler)
p = model.score(x_test_scaler,y_test)
print(p)'''

print('Classification Report\n', classification_report(y_test, y_pred))
print('Accuracy: {}%\n'.format(round((accuracy_score(y_test, y_pred)*100),2)))

cm = confusion_matrix(y_test, y_pred)
print(cm)

# Creating a pickle file for the classifier
filename = 'heart-disease-rf.pkl'
pickle.dump(model, open(filename, 'wb'))

