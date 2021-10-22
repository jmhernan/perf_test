# runs test of randomness
import numpy as np 
import statistics as st
import math
import scipy.stats

def runs_test(data_array):
    data_median = st.median(data_array)

    runs = 0
    n1 = 0
    n2 = 0

    for i in range(len(data_array)):
        # no. of runs
        if(data_array[i] >= data_median and data_array[i-1] < data_median) or \
            (data_array[i] < data_median and data_array[i-1] >= data_median):
            runs += 1

        # positive values
        if(data_array[i]) >= data_median:
            n1 += 1
        # negative values
        else:
            n2 += 1
    runs_exp = ((2*n1*n2)/(n1+n2))+1
    sdev = math.sqrt((2*n1*n2*(2*n1*n2-n1-n2))/ \
                     (((n1+n2)**2)*(n1+n2-1)))

    z = (runs-runs_exp)/sdev
    # two-tailed
    p_value = scipy.stats.norm.sf(abs(z))*2

    return(z, p_value, runs, n1, n2) 


l = []

import random

for i in range(100):
    l.append(random.random())

Z, p_value = runs_test(l)

print('Z-statistic= ', Z )
print('p_value= ', p_value )

# example 1
l = [12, 16, 16, 15, 14, 18, 19, 21, 13, 13]

Z, p_value, runs, n1, n2 = runs_test(l)

print('Z-statistic= ', Z )
print('p_value= ', p_value )
print('runs= ', runs )
print('n1= ', n1 )
print('n2= ', n2 )

