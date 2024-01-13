import sys
import time
import numpy as np
from sklearn.decomposition import PCA
from keras.datasets import mnist
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

(train_X, train_Y), (test_X, test_Y) = mnist.load_data()

reduced_N=32

########################################################
#Write your code here



# Ladataan MNIST data
(train_X, train_Y), (test_X, test_Y) = mnist.load_data()

# Haluttu pienempi dimensio
reduced_N = 32  

#Set value range -1..1
# Muokataan pikseliarvot välille -1 ja 1
train_X = train_X / 127.5 - 1
test_X = test_X / 127.5 - 1


#Convert figures to vectors
# Muunnetaan kuvat vektoreiksi
train_X_flattened = train_X.reshape(train_X.shape[0], -1)
test_X_flattened = test_X.reshape(test_X.shape[0], -1)

#Compute reduced PCA
# Lasketaan PCA:n avulla datan dimensiota pienemmäksi
pca = PCA(n_components=reduced_N)
train_X_packed = pca.fit_transform(train_X_flattened)
test_X_packed = pca.transform(test_X_flattened)


#End of your code
########################################################
#Do not modify lines below this point!




#Save packed data
print('Save packed data')
np.save('packed_train.npy', train_X_packed)
np.save('packed_test.npy', test_X_packed)

if len(sys.argv)==1:
    #Test quality
    print('Train model')
    model = KNeighborsClassifier(n_neighbors = 11)
    model.fit(train_X_packed, train_Y)

    print('Compute predictions')
    pred = model.predict(test_X_packed)
    acc = accuracy_score(test_Y, pred)

    print('Accuracy =',acc)
