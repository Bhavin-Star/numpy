import numpy as np

arr = np.array([ 
    [[1, 2, 3], [4, 5, 6]], #1st eleemt of outermost array [0,?,?]
    [[7, 8, 9], [10, 11, 12]] #2nd element of outermost array [1,?,?] 
    ])

print(arr[1, 0, 2]) #2nd element ka 1st element ka 3rd element

arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr2[1, -1])
# can  also use negative indexing on both 
print('Last element from 2nd dim: ', arr2[-1, -1])