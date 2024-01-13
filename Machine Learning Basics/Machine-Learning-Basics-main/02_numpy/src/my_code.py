import numpy as np

filename = 'm2in.npy'

lopullinen = 'm2out.npy'

taulukko = np.load(filename)

taulukko [0, 0] = 1
taulukko [2, 3] = -1

np.save(lopullinen, taulukko)