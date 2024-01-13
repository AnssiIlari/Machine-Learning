import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


data = pd.read_csv("painteddata.csv")

#Your code here

# Otettu reilusti mallia esimerkkimatskuista

# sklearn standardointi
scaler = StandardScaler()
data = scaler.fit_transform(data)

# alustetaan array 2-19
n_clusters_array=[i for i in range(2, 20)]
# alustetaan taulukko silueteille
silhouette_avg=[]

# for loopissa kmeans fit -> siluetit taulukkoon
for n_clusters in n_clusters_array: 
    kmeans=KMeans(n_clusters=n_clusters, n_init= 'auto').fit(data)
    kmeans_classID=kmeans.labels_
    
    silhouette_avg.append(silhouette_score(data, kmeans_classID))
    
# Lasketaan klusterit    
max_idx=silhouette_avg.index(max(silhouette_avg))
print(n_clusters_array[max_idx])
