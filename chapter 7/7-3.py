import numpy as np

a = np.arange(2, 19, 2).reshape(3, 3)
b = np.arange(19, 1, -2).reshape(3, 3)

print(a)
print(b)

print(a * b)
