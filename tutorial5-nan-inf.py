import numpy as np

# easy to change
print(np.nan) # not a number

# return an infinity value
print(np.inf) # infinity

# we can check if its a nan
print(np.isnan(np.nan))     # true
print(np.isnan(2))          # false

# we can check if its a inf
print(np.isinf(np.inf))     # true
print(np.isinf(2))          # false

print(np.sqrt(-1)) # square root of -1 is complex number so it will return nan
print(np.array([10]) / 0)   # anyuthing divided by zero returns inf