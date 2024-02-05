# This module helps in undertanding the indexing of an array 
# indexing starts from 0 in arrays 
# indexing is used to get only one element 


import numpy as np

#creating 2d array

array1=np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(array1)
#print(array1[1])   # to print any single row 
#print(array1[1,2])  # to print any particular element we should mention the position of the element 
#print(array1[1][1])   # to print any particular element we should mention the position of the element 
print(array1[:,0])    # to print any single column 

list2=[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
array2=np.array(list2)
#print(array2[[1,4,7]])





