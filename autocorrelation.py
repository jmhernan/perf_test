import statistics as st 
import numpy as np 

test_data = np.loadtxt('lew.txt')

def sample_mean(data_array):
    mean = data_array.sum()/data_array.size
    return mean 

data_array = np.array([1,2,3,4,5])
np.sum([(a-sample_mean(data_array))**2 for a in data_array]) # try this approach 

def auto_cor(data_array, k):
    (np.sum((test_data - sample_mean(test_data))) * np.sum(np.delete(test_data,0)-sample_mean(test_data)))/np.sum([(a-sample_mean(test_data))**2 for a in test_data])


first_order_res = np.sum(test_data - sample_mean(test_data))
    
