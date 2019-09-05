num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
num3 = int(input('Enter a number: '))

lowest_num = num1

if lowest_num >= num2:
    lowest_num = num2
    if lowest_num >= num3:
        lowest_num = num3
    print (lowest_num)
else:
    print(lowest_num)
