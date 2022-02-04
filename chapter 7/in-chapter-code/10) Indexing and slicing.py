import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

print(grades)

print(grades[0, 1])

print(grades[0:2])

print(grades[[1, 3]])

# Selecting a Subset of a Two-Dimensional array’s Columns

print(grades[:, 0])

print(grades[:, 1:3])

print(grades[:, [0, 2]])

print("self check")

dm = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])

print(dm)

print(dm[1])

print(dm[[0, 2]])

print(dm[:, 1:4])

