import pandas 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

filename1='grading.csv'
train_fraction = 0.8
Y_column='Passed'

#Load data
data=pandas.read_csv(filename1)
print("Read data shape = "+str(data.shape))
print(data)


#################################################
#Your code here
#
#Create a classifier that classifies students

# Ei tarvetta poistaa puuttuvia arvoja koska niitä ei ole

# Boolean -> int, voisi tehdä myös Y määrittelyssä
data['Passed'] = data['Passed'].astype(int)

# Sekoitellaan , random_state=42
data = shuffle(data, random_state=42)

# Poistetaan Name sarake, ei anna hyödyllistä informaatiota mallille
# Passed tiputetaan pois koska se on kohdevektori y
# X = data.drop(['Name', 'Passed'], axis=1)

# X ver 2
X = data[['Assignment A', 'Assignment B', 'Assignment C']]

# Kohdevektori Y, eli tätä ennustetaan jatkossa
Y = data['Passed']

# Jakosuhde
train_fraction = 0.8
# Jaetaan data tarvittaviin osiin , random_state=42
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1-train_fraction, random_state=42)

# Standardisointi nosti mallin tarkkuutta koulutusdatalla, mutta laski
# varsinaisen ennustuksen tarkkuutta, nyt kommentoitu pois
# Varsinaista dataa ei standardisoida, johtuneeko tästä ???

# Manuaalinen standardointi
# stdev=X_train.std(axis=0)
# mean=X_train.mean(axis=0)
# X_train=(X_train-mean)/stdev
# X_test=(X_test-mean)/stdev

# Muunnos numpy muotoon, ei tarpeellinen StandardScalerin kanssa koska
# palauttaa numpy taulukon
# X_train=X_train.to_numpy()
# X_test=X_test.to_numpy()

# sklearn standardointi
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train) # Huom fit_transform. ERROR
# X_test = scaler.transform(X_test) # Huom transform. ERROR

# Tämä versio ei herjaa
# X_train = pandas.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns)
# X_test = pandas.DataFrame(scaler.transform(X_test), columns=X_test.columns)

# Malli = SVM
classifier = svm.SVC() # Parametrit???
# Koulutus
classifier.fit(X_train, Y_train)

#Ennustus testailuun
# esim=classifier.predict(X_test)

# Lasketaan tarkkuus ennustetulle testidatalle ja tulostetaan, KOMMENTOI
# accuracy = accuracy_score(Y_test, esim)
# print(accuracy)
# accuracy2 = accuracy_score(Y_test, predY)
# print(accuracy2)


#
#################################################

#Load real data
filename2='assignments.csv'
data=pandas.read_csv(filename2)
names=data['Name']

#Remove name column
for col in ["Name"]:
    print("Remove "+col)
    data.drop(col, axis=1, inplace=True)
print()

print("Read data shape = "+str(data.shape))
print(data)
predY=classifier.predict(data)

#Create dataframe from numpy data
df = pandas.DataFrame({'Name': names, 'Passed': predY})
print(df)
df.to_csv('prediction.csv', index=False)

