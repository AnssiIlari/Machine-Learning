import sys
import time
import pandas
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

inputfile='mittaus.csv'


data=pandas.read_csv(inputfile)

#Your code here

# Luodaan PolynomialFeatures-luokan instanssi toisen asteen polynomille.
poly_features = PolynomialFeatures(degree=2)

# Muunnetaan x-sarakkeen arvot polynomisiksi ominaisuuksiksi.
X_poly = poly_features.fit_transform(data[['x']])

# Luodaan lineaarisen regression malli.
model = linear_model.LinearRegression()

# Koulutetaan malli käyttäen muunnettuja ominaisuuksia ja y-saraketta.
model.fit(X_poly, data['y'])

# Ennustetaan y-koordinaatit koko x-sarakealueelle mallimme avulla.
y_pred = model.predict(X_poly)

# Juuren määrittelyä

# Mallin kertoimet (vakiotermi jätetään pois, koska etsimme juuria)
coefficients = model.coef_[1:]  # Otetaan vakiotermi pois
coefficients = np.insert(coefficients, 0, model.intercept_)  # Lisätään vakiotermi alkuun

# Luodaan polynomi kertoimista
p = np.polynomial.Polynomial(coefficients)

# Etsitään polynomin juuret
roots = p.roots()

# Valitaan juurista se, joka on positiivinen ja suurempi kuin suurin x (oletus työnnön päättymisestä)
x_landing = roots[roots > data['x'].max()].real[0] if roots[roots > data['x'].max()].size > 0 else None



#Print your solution

print(x_landing)