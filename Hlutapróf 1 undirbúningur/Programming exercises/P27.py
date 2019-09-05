turns = int(input('How many turns do you want to take? '))

counter = 0
sum_of_negative_integers = 0 

while counter < turns:
    num = int(input('Enter a integer: '))
    counter += 1
    if num < 0:
        sum_of_negative_integers += num
    if counter == turns:
        print('Sum of the entered negative numbers: ' ,sum_of_negative_integers)