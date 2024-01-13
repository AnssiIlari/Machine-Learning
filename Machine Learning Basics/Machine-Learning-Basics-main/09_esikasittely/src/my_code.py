import sys
import time
import pandas

inputfile='weather_data.csv'
outputfile='preprocessed.csv'

data=pandas.read_csv(inputfile)

#Your code here

# Poistetaan sarake jonka nimi on määritelty parametrissä
data.drop(columns=['utc_timestamp'], inplace=True)

#Poistetaan rivit, joilla on puuttuvia tietoja
data.dropna(inplace=True)

#Your code here

data.to_csv(outputfile)
