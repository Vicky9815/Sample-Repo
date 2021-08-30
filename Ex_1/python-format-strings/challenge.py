first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
first_value=first_value.strip() #removing all the empty characters
first_value=first_value.lower() # transform to lower case
first_value=first_value.title()# convert to title format
first_value=f'{first_value: ^30}'

# Second challenge
second_value= second_value.replace("-"," ") #replacing the hyphens with white space/empty character
second_value= second_value.strip()
second_value=second_value.capitalize()


# Third challenge
third_value=third_value.replace(' ','') #replaces space characters with non-empty
third_value=third_value.replace('-','')
third_value=third_value.swapcase() # converts lower case caracters to uppercase and uppercase to lower
third_value=f'{third_value: >30}'


print(first_value)
print(second_value)
print(third_value)

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value, fifth_value, sixth_value, sep='#', end='!')


# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print(f'\n\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}')
