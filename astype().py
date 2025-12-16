'''
The best way to change the data type of an existing array,
is to make a copy of the array with the astype() method.

The astype() function creates a copy of the array,
and allows you to specify the data type as a parameter.

The data type can be specified using a string,
like 'f' for float, 'i' for integer etc
or you can use the data type directly 
like float for float and int for integer.
'''

import numpy as np

arr = np.array([1.2,5.7,6.9,8.3,0.7])

new_arr = arr.astype(int)
# using astype(int) is like gif funcn

print(new_arr)
print(new_arr.dtype)

arr2 = new_arr.astype(bool)

print(arr2)
print(arr2.dtype)
