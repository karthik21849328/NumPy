# splitting array means dividing array into equal parts accroding to the elements in an array 


import numpy as np

# split on 1-d array 
a=np.arange(6)
b=np.split(a,2)
print(b)


#split on 2d array 

c=np.array([[1,2],[3,4],[5,6],[7,8]])
print("array is ",c)
d=np.hsplit(c,2)
print("array after division is",d)