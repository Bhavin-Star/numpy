import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

new_arr = arr.reshape(2,3,2)
print(new_arr)

'''
Can We Reshape Into any Shape?
Yes, as long as the elements required for 
reshaping are equal in both shapes.

We can reshape an 8 elements 1D array into 
4 elements in 2 rows 2D array 
but we cannot reshape it into a 
3 elements 3 rows 2D array 
as that would require 3x3 = 9 elements.
'''

print()
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr2.reshape(2, 4).base)
print()
newarr = arr2.reshape(2,2,-1) 
# transform it into a 3d array
# we are allowed to have one dimension unknown
print(newarr)