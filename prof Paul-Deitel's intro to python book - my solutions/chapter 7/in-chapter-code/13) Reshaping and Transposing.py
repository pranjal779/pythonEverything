import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90]])

print(grades)

print(grades.reshape(1, 6))

print(grades)

# grades.resize(1, 6)

# flatten vs. ravel - function

# Transposing Rows and Columns

# You can quickly transpose an array’s rows and columns—that is “flip” the array, so the
# rows become the columns and the columns become the rows. The T attribute returns a
# transposed view (shallow copy) of the array.
print("Transpose")
print(grades.T)

# Horizontal and Vertical Stacking

grades2 = np.array([[94, 77, 90], [100, 81, 82]])

'''
Let’s assume grades2 represents three additional exam grades 
for the two students in
the grades array. We can combine grades and grades2 with 
NumPy’s hstack (horizontal stack) function by passing a 
tuple containing the arrays to combine. The extra parentheses are required because hstack expects one argumen
'''

gd = np.hstack((grades, grades2))
print(gd)
# vstack (Vertical stack) function

dg = np.vstack((grades, grades2))
print(dg)

print("self check")

nb = np.arange(1, 7).reshape(2, 3)

oo = np.hstack((nb, nb))
ooo = np.vstack((nb, nb))
print("oo")
print(oo)
print("ooo")
print(ooo)
print("nb")
print(nb)
