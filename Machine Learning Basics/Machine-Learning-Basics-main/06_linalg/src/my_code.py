import sys
import time

import numpy as np

def angle_between(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    cos_angle = dot_product / (norm_a * norm_b)
    
    return np.arccos(cos_angle)


