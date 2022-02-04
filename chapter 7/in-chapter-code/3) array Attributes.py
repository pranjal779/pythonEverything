import numpy as np
integers = np.array([[1, 2, 3], [4, 5, 6]])
print(integers)

print(integers.dtype)

floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
print(floats)

print(floats.dtype)

# Determining an array’s Dimensions
# ndim
# shape

print(integers.ndim)
print(floats.ndim)

# print(integers.ndim, end='\n', floats.ndim)

print(integers.shape)
print(floats.shape)

# Determining an array’s Number of Elements and Element Size
# size
# itemsize

print(integers.size)
print(integers.itemsize)  # 4 if C compiler uses 32-bit ints

print(floats.size)
print(floats.itemsize)

# Iterating Through a Multidimensional array’s Elements

for row in integers:
    for column in row:
        print(column, end=' ')
    print()

# You can iterate through a multidimensional array as if it were one-dimensional by
# using its flat attribute:

for i in integers.flat:
    print(i, end=' ')

# Self check
print("\n")
a = np.array([[2, 4, 6, 8, 10], [1, 3, 5, 7, 9]])

print(a)
print(a.ndim)
print(a.shape)
