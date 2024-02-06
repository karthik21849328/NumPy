#Concatenation of array: in simple words joining two arrays to form a resultant array 

#concatenation of 1-d arrays 

import numpy as np
a=np.array([1,2,3,4])

b=np.array([10,20,30])
array=np.concatenate((a,b))
print("concatenated arrays are",array)


#concatenation of 2d arrays 
#by default axis=0 in concatenate funstion, i.e while concatenating two 2d array by row it should match with number of columns or else it will throw error
#if axis =1, then two arrays must have equal number of rows 

array3=np.array([[1,2,3],[4,5,6]])
array4=np.array([[10,20,30],[40,50,60],[70,80,90]])
ar=np.concatenate([array3,array4], axis=0)
#ar1=np.concatenate([array3,array4], axis=0) for this line it will throw error coz number of rows are not matching 
print(ar)

x = np.array([[3], [5], [7]])
y = np.array([[5], [7], [9]])
v=np.vstack((x,y))
n=np.hstack((x,y))
print(n)