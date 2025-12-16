import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])
# slices 2nd arrays index 1 to 4 excluding 4
# [7 8 9]


print(arr[0:2, 2])
# slices [0,2] then [1,2] ie 3 and 8