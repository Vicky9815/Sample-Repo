first_num= input('First Number: ')
second_num= input('Second Number: ')

if first_num.isnumeric()==False or second_num.isnumeric() ==False:
    print('Please enter numbers only.')
    exit()
first_num= int(first_num)
second_num= int(second_num)
sum = first_num + second_num
print(sum)
