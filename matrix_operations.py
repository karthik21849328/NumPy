# matrix is arrangment of elements in rectangular form 
# multi dimensional array are matrices

#operations on matrices

#with the help of numpy, we can direclty use the function to perform opration between two arrays

#addition operation between two matrices
import numpy as np
a=np.array([[10,20],[30,40]])
b=np.array([[1,2],[3,5]])
c=np.add(a,b)
print(c)

#multiplication of matrices, it is not as same as array multiplication(*)
# for matrix multiplication we use .dot()
d=np.dot(a,b)
print(d)

#to find the transpose of matrix
print("before transpose",a)
t=np.transpose(a)
print("after yranspose",t)


#----------------------------------------------------------------------------------------------------
print("-----------------------------------------------------------------------------------------")
# Numpy has a class called matrix 
#numpy.matrix(data,dtype,copy)

list1=[[1,2],[3,4]]
list2=[[10,20],[30,40]]
m1=np.matrix(list1)
m2=np.matrix(list2)

adding_matrix=m1+m2
multiplying_matrix=m1*m2
transpose_matrix=m2.T
print(adding_matrix)
print(multiplying_matrix)
print(transpose_matrix)
