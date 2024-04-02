# pandas series
import pandas as pd

uu = pd.Series(98.6, range(3))
print(uu)

uu2 = pd.Series(98.6, range(3))
print(uu2)

print(uu2.count())
print(uu2.mean())
print(uu2.min())
print(uu2.max())
print(uu2.std())

# describe

print(uu2.describe())

grades = pd.Series([87, 100, 94], index=['Wally', 'Eva', 'Sam'])
print(grades)

# series odf strings

hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])
print(hardware)

print(hardware.str.contains('a'))

'''
Self Check
1 (IPython Session) Use the NumPy’s random-number generation to create an array of
five random integers that represent summertime temperatures in the range 60–100, then
perform the following tasks:
a) Convert the array into the Series named temperatures and display it.
b) Determine the lowest, highest and average temperatures.
c) Produce descriptive statistics for the Series.
Answer:
In [23]: hardware.str.upper()
Out[23]: 
0 HAMMER
1 SAW
2 WRENCH
dtype: object
In [1]: import numpy as np
In [2]: import pandas as pd
In [3]: temps = np.random.randint(60, 101, 6)
In [4]: temperatures = pd.Series(temps)
In [5]: temperatures
Out[5]: 
0 98
1 62
2 63
3 70
4 69
dtype: int64
In [6]: temperatures.min()
Out[6]: 62
In [7]: temperatures.max()
Out[7]: 98
In [8]: temperatures.mean()
Out[8]: 72.4
In [9]: temperatures.describe()
Out[9]: 
count 5.000000
mean 72.000000
std 14.741099
min 62.000000
25% 63.000000
50% 69.000000
75% 70.000000
max 98.000000
dtype: float64

'''

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90],
               'Sam': [94, 77, 90], 'Katie': [100, 81, 82],
               'Bob': [83, 65, 85]}

grades = pd.DataFrame(grades_dict)

print(grades)

# index attribute
print("\nIndex attribute")

grades.index = ['Test1', 'Test2', 'Test3']

print(grades)

print("\nBoolean indexing")

print(grades[grades >= 90])

# NaN = not a number, is pandas' notation for missing values.

print(grades[(grades >= 80) & (grades < 90)])


print("\nAccessing a Specific DataFrame Cell by Row and Column")
# at
# iat
# these are like loc and iloc

print(grades.at['Test2', 'Eva'])

print(grades.iat[2, 0])

grades.at['Test2', 'Eva'] = 100
print(grades.at['Test2', 'Eva'])

grades.iat[1, 2] = 87
print(grades.iat[1, 2])

print(grades.iat[1, 2])

print("\nDescriptive Statistics pdf pg 325")

print(grades.describe())

# print("\nSet_options")
# pd.set_option('precision', 2)

# print(grades.describe())

print("\nTranspose")
print(grades.T)

print(grades.T.describe())

print("\n to see the average of all students grade")

print(grades.T.mean())

print("\nSorting by Rows by Their Indices")

print(grades.sort_index(ascending=False))

print("\nSorting by Column Indices")
print(grades.sort_index(axis=1))

print("\nSorting by Column Values")
print(grades.sort_values(by='Test1', axis=1, ascending=False))

print(grades.T.sort_values(by='Test1', ascending=False))

print("\nexperimenting with sequence slice returning items only '0' and '1' in a range of '2'")
print(grades[::2])

# 327-page
# Copy vs In-Place sorting

print("\nself-check")
"""
 Given the following dictionary;
temps = {'Mon': [68, 89], 'Tue': [71, 93], 'Wed': [66, 82],
         'Thu': [75, 97], 'Fri': [62, 79]}

perform the following tasks:
a) Convert the dictionary into the DataFrame named temperatures with 'Low'
and 'High' as the indices, then display the DataFrame.
b) Use the column names to select only the columns for 'Mon' through 'Wed'.
c) Use the row index 'Low' to select only the low temperatures for each day.
d) Set the floating-point precision to 2, then calculate the average temperature for
each day.
e) Calculate the average low and high temperatures.
"""
# a
temps = {'Mon': [68, 89], 'Tue': [71, 93], 'Wed': [66, 82],
         'Thu': [75, 97], 'Fri': [62, 79]}

temperatures = pd.DataFrame(temps, index=['Low', 'High'])  # a

print(temperatures)  # (a)

# b
print(temperatures.loc[:, 'Mon':'Wed'])

# c
print(temperatures.loc['Low'])

# d
print(temperatures.mean())

# e
print(temperatures.mean(axis=1))
