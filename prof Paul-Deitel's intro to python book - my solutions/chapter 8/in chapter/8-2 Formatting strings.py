from decimal import Decimal

# chapter 8.2.1 Presentation Types
print(f'{17.489:.2f}')

print(f'{10:d}')  # integers

print(f'{65:c} {97:c}')  # characters

print(f'{"hello":s} {7}')

# Floating-Point and Decimal Values

print(f'{Decimal("10000000000000000000000000.0"):.3f}')

print(f'{Decimal("10000000000000000000000000.0"):.3e}')

print("\nself check")
print(f'{58:c} {45:c} {41:c}')

# chapter 8.2.2 Field Widths and Alignment

print(f'[{27:10d}')

print(f'[{3.5:10f}')

print(f'[{"hello":10}]')

print(f'[{27:^7d}]')

print(f'[{3.5:^7.1f}]')

print(f'[{"hello":^7}]')

print("self check")

print(f'[{"Amanda":>10}]\n[{"Amanda":^10}]\n[{"Amanda":<10}]')

# chapter 8.2.3 Numeric Formatting

print(f'[{27:+10d}]')

print(f'[{27:+010d}]')

print(f'{27:d}\n{27: d}\n{-27: d}')

print("Grouping Digits")

print(f'{12345678:,d}')

print(f'{1234567.89:,.2f}')

print("self check")

print(f'{10240.473:+10,.2f}\n{-3210.9521:+10,.2f}')

print('{} {}'.format('Amanda', 'Cyan'))

print('{0} {0} {1}'.format('Happy', 'Birthday'))

print('{first} {last}'.format(first='Amanda', last='Gray'))

print('{last} {first}'.format(first='Amanda', last='Gray'))


