fahrenheit= input('What is the temperature in fahrenheit? ')
if fahrenheit.isnumeric() == False:
    print('Input is not a number')
    exit()
fahrenheit= int(fahrenheit)# this helps convert the input to integer

celsius= (fahrenheit - 32)* 5/9
print('Temperature in celsius is:{}', format(celsius))
