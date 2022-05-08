#
# 
#
import numpy as np 
from scipy import stats 
 
data = np.array([4,5,1,2,7,2,6,9,3]) 
 
# Calculate Mean 
dt_mean = np.mean(data)
print ("Mean :",round(dt_mean,2)) 
 
# Calculate Median 
dt_median = np.median(data)
print ("Median :",dt_median)          
 
# Calculate Mode 
dt_mode =  stats.mode(data)
print ("Mode :",dt_mode[0][0]) 
