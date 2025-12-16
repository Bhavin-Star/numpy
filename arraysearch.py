import numpy as np

arr = np.array([1,2,3,4,5,4,4])

x =  np.where(arr==4)
print(x) #prints the index  where elements in thee array are equal to 4


arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.where(arr2%2 == 0)
print(y)