#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 15:31:48 2022

@author: kojape
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

scaler = StandardScaler()


#Split data frame to x and y - don't modify
def splitXY(d):
    Y_column='fetal_health'
    return d.drop(Y_column, axis=1).to_numpy(), np.int32(d[Y_column]) 


def load_data(filename):
    global drop_columns
    data=pd.read_csv(filename)
    #data = pd.read_csv(filename, usecols=['baseline value', 'accelerations', 'fetal_movement', 'fetal_health'])
    #for col in drop_columns: 
        #data.drop(col, axis=1, inplace=True) 

    return data    

def init_model(datafile):
    
    global model
    global drop_columns
    

    #Modify this to drop unused columns from data
    #drop_columns=['null']
    

    data=load_data(datafile) #load dataframe
    
    X, y = splitXY(data)
    
    X_scaled = scaler.fit_transform(X)
    
    X_train, x_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    
    
    model = SVC(kernel='linear', random_state=42)
    
    #model = SVC()
    
    model.fit(X_train, y_train)

    #your code here
    # - Preprocess data
    # - Split data into two pieces; train set and test set
    # - Create and train model
    # - y_test shall contain integer values in range 1..3
    # - Use global variables to store scaling information.
    #   You may need it in compute_value function.



    return x_test, y_test #return test set for testing purposes


#Compute predicted value of x
def compute_value(x):
    global model
    
    global scaler
    x_scaled = scaler.transform(x)
    y_pred = model.predict(x_scaled)
    
    #your code here
    # - x is unscaled x value, scale it
    # - utilize model to predict y_pred vector values, y_pred is vector which 
    #   elements are integers in 1..3
    
    
    
    return y_pred

#Loads validation data set and computes predictions based on x-values
#Don't utilize y-values except for testing purposes!
def validate(filename):
    data_val=load_data(filename)
    x_val, y_val=splitXY(data_val)
    y_pred=compute_value(x_val)
    return y_pred, y_val


#Test program (don't modify)
if __name__ == "__main__":
    x_test, y_test=init_model('fetal_health.csv')

    testN, _=np.shape(x_test)
    assert(np.shape(y_test)==(testN,))

    y_pred=compute_value(x_test)
    errors=(y_pred!=y_test).sum()
    print('Errors (test set):', errors, '/', testN)

    y_pred, y_val=validate('validation.csv')
    valN=np.shape(y_val)[0]
    errors=(y_pred!=y_val).sum()
    print('Errors (validation set):', errors, '/', valN)


    
    