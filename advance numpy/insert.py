'''
np.insert(array, index, value, asix=none)
arry = original array
index -
value - 
asix = none
asix = 0 insert row wise
1 insert column wise
'''
import numpy as np
arr = np.array([12,23,45,65,67,45,34,23,45,56])
print(arr)
print(np.insert(arr,2,100))