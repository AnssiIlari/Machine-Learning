import sys
import time
import pandas
from scipy import stats
from scipy.stats import zscore
import numpy as np
from sklearn import linear_model

inputfile='measurements.csv'
m=0.75 #mass of the object


#Your code here


# Ladataan data ja poistetaan puuttuvat arvot
data = pandas.read_csv(inputfile)
data_cleaned = data.dropna()

# Suoritetaan Z-testi poistaaksesi outlierit, käyttäen z-arvoa 3
z_scores = stats.zscore(data_cleaned)
abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < 3).all(axis=1)
data_no_outliers = data_cleaned[filtered_entries]

# Alhaisemman lämpötilan arvoissa vaikutti olevan enemmän vaihtelua
# Poistettu nämä testin jäätyä pienestä kiinni

temperature_threshold = 30  # Alaraja lämpötilalle, jonka alle jäävät pisteet poistetaan

# Poistetaan datapisteet, joiden lämpötila on alhaisempi kuin asetettu kynnysarvo
data_no_outliers = data_no_outliers[data_no_outliers['T'] > temperature_threshold]


# TESTAILUA VARTEN
# data_cleaned.to_csv("first_clean.csv", index = False)
# data_no_outliers.to_csv("cleaned_data.csv", index=False, decimal=',')
# TESTAILUA VARTEN

# Lasketaan ohjeen mukaisesti ominaislämpökapasiteetin lukuarvo (...n neliö?)

# Otetaan viimeisen pisteen energia-arvo
final_energy = data_no_outliers['E'].iloc[-1]
# Lasketaan kokonaislämpötilan muutos ensimmäisestä pisteestä viimeiseen
total_temperature_change = data_no_outliers['T'].iloc[0] - data_no_outliers['T'].iloc[-1]
# Lasketaan ominaislämpökapasiteetti käyttäen viimeisen pisteen energia-arvoa ja kokonaislämpötilan muutosta
c_calculated_final = final_energy / (m * total_temperature_change)


#Your code here

#Estimated specific heat capacity 
print(c_calculated_final)
