import sys
import time
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score # Tämä kommentissa


X=np.load('teach_data.npy')
Y=np.load('teach_class.npy')

################################################
#Your code below this line

# Muuttuja datan jakamista varten
train_fraction = 0.8
# Jaetaan data joukkoihin + rndm siemen
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1-train_fraction, random_state=42)

# Tulostetaan jaettujen joukkojen muodot, kommentoi
# print("Training set features shape:", X_train.shape)
# print("Training set labels shape:", Y_train.shape)
# print("Test set features shape:", X_test.shape)
# print("Test set labels shape:", Y_test.shape)

# Standardisointi
# Tässä tapauksessa tarkkuus ilman standardisaatiota parempi??
# Pidetty kuitenkin tässä muodossa koska < 0.92
# 0.9520497803806734 vs. 0.9333821376281113
stdev=X_train.std(axis=0)
mean=X_train.mean(axis=0)
X_train=(X_train-mean)/stdev
X_test=(X_test-mean)/stdev

# Muuttuja naapurien lukumäärälle
n_neighbours=3

# Valitaan luokittelija
model = KNeighborsClassifier(n_neighbors=n_neighbours)
# Koulutetaan luokittelija
model.fit(X_train, Y_train)

# ennustetaan
# esimMalli =model.predict(X_test)

# Lasketaan tarkkuus ennustetulle testidatalle
# accuracy = accuracy_score(Y_test, esimMalli)

# Tällä voi tarkastaa tarkkuuden
# print("Accuracy:", accuracy)


#Your code above this line
################################################

print('Compute real predictions')
real_X=np.load('data_in.npy')

print('real_X -', np.shape(real_X))
pred = model.predict(real_X)
print('pred -', np.shape(pred))
np.save('data_classified.npy', pred)

