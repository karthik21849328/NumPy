# Stack is similar to concatenate
# there are two modes vstack and hstack
#v stack joins two array by row
#h stack joins two array by column
#vstack is similar to concatenate with axis =0

#stack on 1-d arrays 
# when we use stack to join two 1 d arrays, resuatant joined array will be in 2d array 

import numpy as np
a=np.zeros(4)
b=np.zeros(4)
c=np.vstack((a,b))
d=np.hstack((a,b))
print("resultant array for v stack",c)
print("resultant array for h stack",d)


array1=np.array([[1,2,3],[4,5,6]])
array2=np.array([[10,20,30],[40,50,60]])
array3=np.vstack((array1,array2))
array4=np.hstack((array1,array2))
print(array3)
print(array4)