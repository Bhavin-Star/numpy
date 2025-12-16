import numpy as np

arr = np.array([1,2,3,4,5])
print(arr.shape)


arr2d = np.array([
    [1,2,3], [3,4,5]
])

print(arr2d.shape)
# returns (2, 3), which means that the array has 2 dimensions, 
# where the first dimension has 2 elements and the second has 3.

arr3d = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])

print(arr3d.shape)
# think of it is as a type of cube(cuboid to bee more precise)
# or a matrix of 2*2*3 

x = np.array([1,2,3,4,5,6], ndmin=6)
print(x.shape)