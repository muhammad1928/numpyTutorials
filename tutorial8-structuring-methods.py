import numpy as np

a1 = np.array([[1,2,3,4,5],
               [6,7,8,9,10],
               [11,12,13,14,15],
               [16,17,18,19,20]])

print(a1.shape) # 4 rows 5 columns

# reshapes does not save but only return it.
print(a1.reshape((5,4))) # reshaping the elements by 5 rows and 4 columns
print(a1.reshape((20,))) # reshaping with only 1 dimenstion
print(a1.reshape((20,1))) # reshaping with only 20 dimenstion with only 1 element each
print(a1.reshape((2,2,5))) # 2 dimension within 2 dimensions with 5 elements each
print(a1.reshape((5,2,2))) # 2 dimension withing 5 dimensions with 2 elements each
print(a1.reshape((2,5,2))) # 5 dimensions within 2 dimensions with 2 elements each

# a1.resize((10,2)) # this will save the new shape
# print(a1)

# print(a1.flatten()) # returns 1 dimension array without changing the original
# print(a1.ravel()) # # saves the new 1 dimension shape with saving the array

print(a1.transpose()) # this will swap the columns and rows
print(a1.swapaxes(0,1)) #this will swap only axis 0 and 1. not others. usefull when we have more dimensions