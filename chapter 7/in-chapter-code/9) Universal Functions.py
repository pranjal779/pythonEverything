# universal functions or ufuncs

# sqrt

import numpy as np

numbers = np.array([1, 4, 9, 16, 25, 36])

print(numbers)

numbers2 = np.arange(1, 7) * 10
print(numbers2)

numbers3 = np.add(numbers, numbers2)
print(numbers3)

# The expression np.add(numbers, numbers2) is equivalent to:
# numbers + numbers2

# Broadcasting with Universal Functions
# multiply universal function
nu = np.multiply(numbers2, 5)

# numbers2 * 5

numbers4 = numbers2.reshape(2, 3)

print(numbers4)

numbers5 = np.array([2, 4, 6])

numbers6 = np.multiply(numbers4, numbers5)

# other ufuncs - https://docs.scipy.org/doc/numpy/reference/ufuncs.html

# self check

numbers7 = np.arange(1, 6)
print(numbers7)

numbers8 = np.power(numbers7, 3)
print(numbers8)
