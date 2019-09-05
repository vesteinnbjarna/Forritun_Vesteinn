
turns = int(input('How many integers do you want to enter: '))
countdown = 0

if turns % 2 != 0:
    print('You picked', turns)
    
while countdown < turns:
    num = int(input('Enter a number: '))
    countdown += 1 