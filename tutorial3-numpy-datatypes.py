import numpy as np

a = np.array([[1,2,3], [4, "Hello", 6], [7,8,9]]) # this is possible with ordinary python arrays but not with numpy

b = np.array([[1,2,3], [4, 5, 6], [7,8,9]])
print(a.dtype) # <U11 = string with less than or equal to 11 characters

print(type(a[0][0])) # <class 'numpy.str_'> which means its a string not a number
print(a[0][0].dtype) # <U1 = a string with less than 1 character

print(type(b[0][0])) # <class 'numpy.int64'> which mens its a integer in array b

