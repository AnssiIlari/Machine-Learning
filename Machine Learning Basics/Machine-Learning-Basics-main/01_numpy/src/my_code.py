import numpy as np

filename = 'm1out.npy'
testarray=np.zeros((3, 4))

np.save(filename, testarray)