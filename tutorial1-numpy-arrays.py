import numpy as np

# np arrays are just like ordinary python list
a = np.array([0,1,2,3,4])

print(a)        # print a array                                                 [0, 1, 2, 3, 4]
print(a[1])     # print second element, (first element is 0)                    [1]
print(a[1:])    # print all after the second element                            [1, 2, 3, 4]
print(a[:-2])   # print array a except last 2 items                             [0, 1, 2]
print(a[::-1])  # print the array reversed                                      [4, 3, 2, 1]

a[2] = 10       # change the 3rd element to 10
print(a)        #                                                               [ 0  1 10  3  4]

# multi dimensional arrays!
a_mul = np.array([[1,2,3], [4, 5, 6], [7, 8, 9]])
print(a_mul)    #                                                               [[1 2 3]
                #                                                               [4 5 6]
                #                                                               [7 8 9]]
                
print(a_mul[1]) # this will print the second dimension of a_mul                 [4, 5, 6]
print(a_mul[1][2]) # this will print the second dimensions, third element       [6]

