# shallow copies
# view

import numpy as np

numbers = np.arange(1, 6)

print(numbers)

numbers2 = numbers.view()

print(numbers2)

