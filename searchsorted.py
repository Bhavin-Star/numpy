'''
Search Sorted
There is a method called searchsorted() 
which performs a binary search in the array, 
and returns the index where the specified value 
would be inserted to maintain the search order.


The searchsorted() method is assumed to be used on sorted arrays.
'''

import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

'''
The number 7 should be inserted on index 1 to remain the sort order.
The method starts the search from the left 
and returns the first index where 
the number 7 is no longer larger than the next value.
'''

arr2 = np.array([6, 7, 8, 9])
x2 = np.searchsorted(arr2, 7, side='right')
print(x2)

'''By default the left most index is returned, 
but we can give side='right' 
to return the right most index instead.

The number 7 should be inserted on index 2 to remain the sort order.

The method starts the search from the right 
and returns the first index where the number 7 
is no longer less than the next value.
'''

arr3 = np.array([1, 3, 5, 7])
x3 = np.searchsorted(arr3, [2, 4, 6])
print(x3)

