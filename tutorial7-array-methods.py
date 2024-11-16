import numpy as np

# how to append, instert, delete from an array and more


a1 = np.array([1,2,3]) # 1 dimensional array

np.append(a1, [7,8,9]) # add 7,8,9 this will return the result but not save it
print(a1)   # 1 2 3
a1 = np.append(a1, [7, 8, 9]) # add 7,8,9 this will save it
print(a1)   # 1 2 3 7 8 9
a1 = np.insert(a1, 3,[4,5,6]) # we will inster 4 5 6 in the index 3
print(a1)   # 1 2 3 4 5 6 7 8 9


a2 = np.array([[1,2,3], [4,5,6]]) # 2 dimensional array
# delete element
print(np.delete(a2, 1)) # this will delete the element in index 1, it will not delete the whole array
print(np.delete(a2, 2)) # this will delete the element in index 2, it will not delete the whole array
print(np.delete(a2, 3)) # this will delete the element in index 3, it will not delete the whole array
print(np.delete(a2, 5)) # this will delete the element in index 5, it will not delete the whole array

print(np.delete(a2, 1, 0)) # this will delete the whole second row
print(np.delete(a2, 1, 1)) # this will delete the whole second column