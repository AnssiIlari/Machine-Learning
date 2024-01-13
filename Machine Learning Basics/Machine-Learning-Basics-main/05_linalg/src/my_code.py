import sys
import time
import numpy as np


def is_orthogonal(a, b):
    return np.isclose(np.dot(a,b), 0)
