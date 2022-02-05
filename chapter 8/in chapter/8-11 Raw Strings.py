# file_path = 'C:\\MyFolder\\MySubFolder\\MyFile.txt'

# * vs. + Quantifier
import re

print(re.sub(r'\t', ', ', '1\t2\t3\t4'))
"""
The sub function receives three required arguments:
• the pattern to match (the tab character '\t')
• the replacement text (', ') and
• the string to be searched ('1\t2\t3\t4')
"""

print(re.split(r',\s*', '1, 2, 3,4, 5,6,7,chapter 8'))

print("Function search—Finding the First Match Anywhere in a String")

result = re.search('Python', 'Python is fun')

print(result.group() if result else 'not found')

result2 = re.search('fun!', 'Python is fun')

print(result2.group() if result2 else 'not found')

