# slicing two dimensional array 

import numpy as np
list2=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
array2=np.array(list2)
#print(array2)

#syntax for slicing an array
#array_name[start:end:step,start:end:step] -------> row , column

print(array2[1:,0:3])
print(array2[1:,2:])

#quiz
list3=[[1,0,1,0,2,3],[1,3,0,1,2,0],[0,1,0,0,1,3]]
array3=np.array(list3)
#print(array3)
print(array3[:,1])  #this return only one column as row in 1d


