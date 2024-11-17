import numpy as np


number = np.random.randint(100)     # generate random numbers
print(number)

number = np.random.randint(100, size=(2,3,4)) # generate random matrix with shape of 2x3x4
print(number)

number = np.random.randint(90, 100, size=(2,3,4)) # generate random matrix with shape of 2x3x4 with vlaues between 90 and 100
print(number)

number = np.random.randint(2, size=(2,3,4)) # generate random matrix with shape of 2x3x4 with vlaues between 0 and 1
print(number)

numbers = np.random.binomial(10, p=0.5, size=(5,10)) # idk
print(numbers) 
# [[4 7 6 5 7 3 3 6 5 5]
#  [8 3 7 3 4 2 6 5 6 4]
#  [5 6 4 6 5 6 4 8 7 7]
#  [5 5 5 5 5 5 6 4 3 6]
#  [6 3 4 5 3 7 5 7 6 4]]

numbers = np.random.normal(loc=170, scale=15, size=(5,5)) # loc 170 means location 170, scale 15 = ((170 -15)< 170 < (170+15))
print(numbers)

numbers = np.random.choice([10,20,30,40,50]) # this will choose arandom number from thearray
print(numbers)
