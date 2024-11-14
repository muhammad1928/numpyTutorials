import numpy as np

# create a list array full of 7
# first we pass in shape of array and value of array
a = np.full((2,3,4), 7)  # 2 x 3 x 4 shape of array only 7
b = np.zeros((4,4,4))       # 4 x 4 x 4 shape of array only 0
c = np.ones ((3,3,3))       # 3 x 3 x 3 shape of array only 1
d = np.empty((5,5,5))       # illocates space only ( rezerves space)

x_values = np.arange(0, 1000, 10) # from value (0) to value(1000) stepsize (10)
# y_values = np.linspace(0, 1000, 20)
y_values = np.linspace(0, 1000, 21) # from value(0) to value(1000) how many values do we want (21 values) its gonna split the value evenly inclusive 0 and 1000
print(a)
print(b)
print(c)
print(d)
print(x_values)
print(y_values)

