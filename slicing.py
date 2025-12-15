import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])
#includes index 1 but excludes index 5
# output 2,3,4,5

arr2 = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr2[4:])
#slices from index 4 till last ie --> 5,6,7

print(arr2[:4])
# slices from begining till index 4 (excluded) ie --> [1 2 3 4]

#negative slicing
print(arr2[-3:-1])
#slices from 3rd last element to last element excluding last element

#use step value to determine step of slicing 
print(arr[1:5:2])
# slices index no 1 3 5 but excluding 5
# output --> [2 4]

print(arr[::2])
#slices element from begining till end by a step value 2 
#output --> [1 3 5 7]