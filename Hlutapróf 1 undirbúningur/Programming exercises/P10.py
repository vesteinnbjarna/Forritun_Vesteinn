num = int(input('Enter a number: '))

if num < 10 and num > 0:
    print('The number is less than 10')
elif num >= 10 and num < 20:
    print('Between 10 and 20')
elif num >= 20:
    print('Too high!')
else:
    print('Too low')