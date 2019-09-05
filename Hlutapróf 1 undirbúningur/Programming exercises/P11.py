a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
choice = int(input('Enter 1 for addition, 2 for subtraction and 3 for multiplication: '))

if choice == 1:
    print (a+b)
elif choice == 2:
    print(a-b)
elif choice == 3:
    print(a*b)
else:
    print('Invalid input!')