import numpy as np

numbers = np.arange(1, 6)

print(numbers)

number2 = numbers.copy()

print(number2)

# To prove that numbers2 has a separate copy of the data in numbers, let’s modify an
# element in numbers, then display both arrays:

numbers[1] *= 10

print(numbers)
print(number2)
