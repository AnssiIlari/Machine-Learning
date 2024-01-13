import sys
import time
import numpy as np

def unit(a):
    norm_a = np.linalg.norm(a)
    return a / norm_a
