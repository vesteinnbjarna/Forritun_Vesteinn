turns = int(input('How many turns do you want to take? '))

counter = 0
num_of_negative_integers = 0 

while counter < turns:
    num = int(input('Enter a integer: '))
    counter += 1
    if num < 0:
        num_of_negative_integers +=1
    if counter == turns:
        print('You entered' ,num_of_negative_integers, 'negative numbers')