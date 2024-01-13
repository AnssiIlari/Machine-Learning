import sys
import time
import numpy as np

def project(x, y):
    dot_product = np.dot(x, y)
    norm_y_squared = np.dot(y, y)
    return (dot_product / norm_y_squared) * y
