import numpy as np

a1 = np.array([[1,2,3,4,5, 111],
               [6,7,8,9,10, 112]])

a2 = np.array([[11,12,13,14,15, 113],
               [16,17,18,19,20, 114]])


b1 = np.concatenate((a1, a2), axis=0) # this will add the arrays columns wise
print(b1)
b2 = np.concatenate((a1, a2), axis=1) # this will add the arrays rows wise
print(b2)

b3 = np.stack((a1,a2)) # thiswill stack a new dimension. from (2x5) to (2x2x5)
print(b3)

b3 = np.vstack((a1,a2)) # thiswill stack as concatenate. from (2x5) to (4x5) (vertical)
print(b3)
b3 = np.hstack((a1,a2)) # thiswill stack as concatenate. from (2x5) to (2x10) (horizontal)
print(b3)

print(np.split(b1, 2, axis=0)) # this will split the array to 2 arrays horizontally

print(np.split(b1, 2, axis=1)) # this will split the array to 2 arrays vertically
print(np.split(b1, 3, axis=1)) # this will split the array to 3 arrays vertically

print(b1.min())     # min value
print(b1.max())     # max value
print(b1.mean())    # mean value # ortalama veri
print(b1.std())     # standard diviation
print(b1.sum())     # sum
print(np.median(b1)) # median  # en ortadaki veri