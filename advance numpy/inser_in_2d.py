import numpy as np 
arr = np.array([[1,2,3],[4,5,6],[3,5,6]])
print(arr)
arr_2d = np.insert(arr, 1, [10,20,30], axis=None)
print(arr_2d)