import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

inputfile='in.npy'
outputfile='out.npy'

data=np.load(inputfile)

#Your code here

# Luodaan PCA olio
pca = PCA()
# Pakataan data
packed_data = pca.fit(data)

# Lasketaan ominaisarvot ja järjestetään ne laskevaan järjestykseen
eigenvalues = pca.explained_variance_
# 1/10 suurimmasta ominaisarvosta
threshold = eigenvalues[0] / 10
# Löydetään pienin komponenttien määrä n, jonka ominaisarvot ylittävät kynnyksen
n_components = np.sum(eigenvalues >= threshold)

# Luodaan uusi PCA halutulla komponenttien määrällä
pca = PCA(n_components=n_components)
packed_data = pca.fit_transform(data)

outputfile = 'out.npy'

#Your code here

np.save(outputfile, packed_data)
