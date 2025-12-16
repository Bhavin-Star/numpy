import numpy as np

'''arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)'''


arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)

print(arr)
# 3d may imagine karo axis =1 pay [1 2 5 6] club ho jayenge
# aur [3 4 7 8] club ho jayenge