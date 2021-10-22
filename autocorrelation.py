import numpy as np 
from scipy.ndimage.interpolation import shift
import statistics as st
import math

def sample_mean(data_array):
    mean = data_array.sum()/data_array.size
    return mean 


def auto_cor(data_array, k):
    auto_correlation = np.sum((data_array - sample_mean(data_array)) * 
        (shift(data_array, k, cval=0)-sample_mean(data_array)))/ \
        np.sum([(a-sample_mean(data_array))**2 for a in data_array])
    return auto_correlation
