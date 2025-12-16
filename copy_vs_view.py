import numpy

arr = numpy.array([1,2,3,4,5])

x = arr.copy()
y = arr.view()

arr[0] = 7
arr[1] = 9

print("Original array: ", arr)
print("x: ", x)
print("y: ", y)

print()
y[-1] = 69
print(y)
print(arr)

print()
print(x.base)
print(y.base)