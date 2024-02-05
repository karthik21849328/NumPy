# This module helps in slicing the array 
# silicing means getting list of values from array



#slicing one-dimensional array
# Syntax array_name[start:end:step] start is inclusive, end is exclusive, step by default its 1

import numpy as np

list1=[1,2,3,4,5,6,7,8]
array1=np.array(list1)
print(array1[0:5]) 
print(array1[:]) #prints all the elements
print(array1[:4]) # by default starts from 0 index of array

# slicing two dimensional array 

list2=[[[1,2,3,4],[5,6,7,8],[9,10,11,12]]]
array2=np.array(list2)