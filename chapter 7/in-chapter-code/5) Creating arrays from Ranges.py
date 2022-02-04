# Creating Integer Ranges with arange
import numpy as np

u = np.arange(5)
print(u)
u1 = np.arange(5, 10)
print(u1)
u2 = np.arange(10, 1, -2)
print(u2)

# Creating Floating-Point Ranges with linspace
u3 = np.linspace(0.0, 1.0, num=5)
print(u3)

# Reshaping an array
u4 = np.arange(1, 21).reshape(4, 5)
print(u4)

# chained method calls

u5 = np.arange(1, 100001).reshape(4, 25000)
print(u5)

# self check

u6 = np.arange(2, 41, 2).reshape(4, 5)
print(u6)

