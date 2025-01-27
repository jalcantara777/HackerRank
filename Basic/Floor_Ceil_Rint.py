import numpy as np
np.set_printoptions(legacy='1.13')

my_array = np.array(input().split(),float)
print(np.floor(my_array))
print(np.ceil(my_array))
print(np.rint(my_array))
