print('Simple Calculator!')

first_num= input('First number?')
if first_num.isnumeric() ==False:
    print('Please input a number')
    exit()


operation= input('Operation?')

second_num= input('Second number?')
if first_num.isnumeric() == False:
    print('Please input a number')
    exit()

first_num=int(first_num)
second_num= int(second_num)

result= 0
if operation== '+':
    result= first_num+ second_num
    label='sum'
elif operation=='-':
    result= first_num-second_num
    label='diff'
elif operation=='*':
    result= first_num*second_num
    label='product'
elif operation=='/':
    result= first_num/second_num
    label='quotient'
elif operation=='**':
    result= first_num**second_num
    label='exponent'
elif operation=='%':
    result= first_num%second_num
    label='modulus'
print(label +' of '+ str(first_num)+' '+ operation +' ' + str(second_num)+ 'equals' + str(result))






 