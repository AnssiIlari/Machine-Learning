import numpy as np

# naming variables
fileName = 'm4in.npz'
fileNameOut = 'm4out.npy'

# reads the file
data = np.load(fileName)

# assigns array called b from the data to the variable b
b = data['b']

# saves the array to a file
np.save(fileNameOut, b)