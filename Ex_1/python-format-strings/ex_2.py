#these are helper functions- provide aditional functionality

# 1. Capitalizing the first letter of the sentence
#method 1
message = str.capitalize('victoria is my beautiful name')
print(message)

#method2
message2='victoria'.capitalize()
print(message2)

#method3
message3='hi very much'
print(message3.capitalize())

# 2. modigying cases of a string
print(message.lower())
print(message.upper())
print(message.title())
print(message.swapcase())

# 3. number of times a string appears in another
a= 'mississippi'
print(a.count('s'))

# 4. find the position of a string in a sentence
b= 'my name is vicky monari' 
print(b.find('e'))

#5. removes empty characters from both left and right side of a string

c= '   o o g o o p a  '
print(c.strip())

#6. replacement
c= 'kwani ni kesho'
print(c.replace('kwani','alah'))

#7. adding empty characters to the left/right of a string
message4= 'laptop'
print(message4.ljust(13))
print(message4.ljust(10,'='))
print(message4.rjust(10,'.'))
