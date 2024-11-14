import numpy as np

# python list
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]

# numpy list
a1 = np.array(l1)
a2 = np.array(l2)

print(l1 * 5) # repeat the list 5 times
print(a1 * 5) # multiple the list with

# print(l1 +3) # this gives an error
print(a1 +3) # this adds 3 to each element inside the array

print(l1 + l2) # this combines the lists
print(a1 + a2) # this combines each elemenets of each list
# print(l1 * l2) # this gives an error
print (a1 * a2) # multiplies each elemeents

a3 = np.array([1,2,3]) # 1 dimension 3 elemenets
a4 = np.array([[1], [2]]) # 2 dimensions 1 elements
a5 = np.array([[1,2], [3,4]]) # 2 dimensions 2 elements

print(a3 + a4) # this will return a 3 by 2 matrix
# print(a3 + a5) # numpy does not support this kind of shapes

b1 = np.array([[1,2,3], [4,5,6]]) # 2 dimensional array

print(np.sqrt(b1)) # sqrt of b1