import pandas
from scipy import stats
import numpy as np
from sklearn import preprocessing

inputfile='time_series.csv'
trainfile='train.csv'
testfile='test.csv'

data=pandas.read_csv(inputfile)

#Your code here

#Haetaan parametrien mukaiset tiedot
data = data[(data['region'] == 'DE') & (data['variable'] == 'wind') & (data['attribute'] == 'generation_actual')]

#Poistetaan seuraavat sarakkeet koska niiden arvo on nyt jokaisessa kohdassa sama
data = data.drop(columns=['region', 'variable', 'attribute'])

# Poistetaan puuttuvat tiedot
data = data.dropna()

# Z-testin kynnysarvo
z_threshold=4.0

# Poistetaan outlierit
data = data[(np.abs(stats.zscore(data['data'])) < z_threshold)]

# Instanssi
scaler = preprocessing.MinMaxScaler()

# Normalisoidaan "data" sarake välille 0 - 1
data['data'] = scaler.fit_transform(data[['data']])

#Muuttuja suhteelle opetusjoukko & testijoukko
train_fraction=0.7

# Opetusjoukko
traindata=data.sample(frac=train_fraction,random_state=200)

# Testijoukko
testdata = data.drop(traindata.index)


#Your code here
#Save train data
print("Save train data")
traindata.to_csv(trainfile)

#Save test data
print("Save test data")
testdata.to_csv(testfile)

