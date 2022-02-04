import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

print(grades)

'''
sum
min - min()
max - max()
mean
std (standard deviation)
var (variance) 
'''
print(grades.sum())
print(grades.min())
print(grades.max())
print(grades.mean())
print(grades.std())
print(grades.var())

print(grades.mean(axis=0))
print(grades.mean(axis=1))
