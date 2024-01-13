import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
#from sklearn.preprocessing import StandardScaler #Lisätty
#from sklearn.preprocessing import MinMaxScaler # Lisätty

Y_column=8

def splitXY(d):
    return d.drop(Y_column, axis=1), d[Y_column] 

data=pd.read_csv('traindata.csv', header=None)

#Your code here...

# Muunnetaan sukupuolen merkintä numeeriseksi: F -> -1, I -> 0, M -> 1
#data[0] = data[0].map({'F': -1, 'I':0, 'M': 1})
data.replace({'I':0, 'F':-1, 'M':1}, inplace=True)

#Sekoitus
data = shuffle(data)

#Jaetaan aineisto x ja y osiin käyttäen valmiiksi annettua splitXY funktiota
x, y = splitXY(data)

# Jaetaan aineisto opetus- ja testiaineistoon
trainX, testX, trainY, testY = train_test_split(x, y, test_size=0.2, random_state=42)

# Normalisointi

# Standardize data
# scaler_x = StandardScaler()
# scaler_y = StandardScaler()

# trainX = scaler_x.fit_transform(trainX)
# testX = scaler_x.transform(testX)
  
# trainY = scaler_y.fit_transform(trainY)
# testY = scaler_y.transform(testY)

n_train, width_train=np.shape(trainX)
n_test, width_test=np.shape(testX)

# assert(width_train==width_test)

model=Sequential()
model.add(Dense(64, activation='relu', input_shape=(width_train,))) #8 / width_train
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='linear'))

#KOMMENTOI pois
#model.summary()

# Kompiloidaan malli
model.compile(loss='mean_squared_error', optimizer='adam')

# Koulutetaan malli
model.fit(trainX, trainY, epochs=25)

model.save('kotilo.h5')

predY=np.round(model.predict(testX)).reshape((n_test, ))

accepted_n=(np.abs(predY-testY)<=3).sum()
print('Correct predictions:', accepted_n, '/', n_test);

