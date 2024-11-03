import numpy as np

# multi dimensional arrays!
a = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

b = np.array([[[1, 2, 3, 1], 
              [4, 5, 6, 1], 
              [7, 8, 9, 1]],
              [[1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1]]])

# shape of a array
print(a.shape)                      # (3, 3)
# dimensions of the array
print(a.ndim)                       # 2
# size of a 
print(a.size)                       # 9 (also know as shape in multiplicaiton, 3x3)
# datatype of a
print(a.dtype)                      # int64

# shape of b array
print(b.shape)                      # (2, 3, 4)
# dimension of the array
print(b.ndim)                       # 3
# size of b
print(b.size)                       # 24 (also know as shape in multiplicaiton, 2x3x4)
# datatype of b
print(a.dtype)                      # int64