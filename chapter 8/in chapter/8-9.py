letters = 'A, B, C, D'

print(letters.split('. '))

print(letters.split('. ', 2))

print('Amanda: 89, 97, 92'.partition(': '))

lines = """This is line 1
This is line2
This is line3"""

print(lines)

print(lines.splitlines())

print("\n")

print(lines.splitlines(True))

print(', '.join(reversed('Pamela White'.split())))
