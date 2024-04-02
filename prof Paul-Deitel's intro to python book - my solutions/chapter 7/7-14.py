"""
Horizontal and Vertical Stacking) Create the two-dimensional arrays
array1 = np.array([[0, 1], [2, 3]])
array2 = np.array([[4, 5], [6, 7]])
a) Use vertical stacking to create the 4-by-2 array named array3 with array1
stacked on top of array2.
b) Use horizontal stacking to create the 2-by-4 array named array4 with array2
to the right of array1.
c) Use vertical stacking with two copies of array4 to create a 4-by-4 array5.
d) Use horizontal stacking with two copies of array3 to create a 4-by-4 array6.
"""

import numpy as np

array1 = np.array([[0, 1], [2, 3]])
array2 = np.array([[4, 5], [6, 7]])

print("a")
array3 = np.vstack((array1, array2)).reshape(4, 2)
print(array3)

print("b")
array4 = np.hstack((array2, array1)).reshape(2, 4)
print(array4)

print("c")
# array5 = array4.view().reshape(4, 4)

# print(array5)

print("d")
