import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

filter_arr=[]

for i in arr:
    if(i%2 == 0):
        filter_arr.append(True)

    else:
        filter_arr.append(False)

newarr = arr[filter_arr]
print(newarr)