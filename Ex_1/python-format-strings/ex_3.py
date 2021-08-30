#1. f-strings( same as format )
name='myself'
count= 18
print(f'{name} am {count} years old')

#calsulations inside the f strings
height= 2
width =13
print(f'A {height} metres tall and {width} metres wide box has an area of {width*height} metres ')

#2. You can use the format specifier syntax to format numbers, dates, time, percentages, and exponents.
value='Hi Vicky'
print(f'.{value:>25}.') #25 empty characters to the right of the full stop
print(f'{value:<25}')
print(f'.{value:=^25}.')# value is printed in the middle with equal signs on both sides