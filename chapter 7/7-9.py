import numpy as np

uu = np.arange(1, 16).reshape(3, 5)
print(uu)

# a
print("a")
print(uu[1])

print("b")
print(uu[:, -1:])

print("C")
print(uu[0:2])

print("d")
print(uu[:, 2:])

print("e")
print(uu[1, 4])

print("f")
print(uu[[1, 2], :][:, [0, 2, 4]])  # Selects the columns you want as well
