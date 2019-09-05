turns = int(input('How many turns do you want to take? '))

counter = 0
num_of_negative_integers = 0 
num_of_positive_integers = 0
sum_of_negative_integers = 0
sum_of_positive_integers = 0

while counter < turns:
    num = int(input('Enter a integer: '))
    counter += 1
    if num < 0:
        num_of_negative_integers +=1
        sum_of_negative_integers += num
    if num > 0:
        num_of_positive_integers +=1
        sum_of_positive_integers += num
    if counter == turns:
        print('You entered' ,num_of_negative_integers, 'negative numbers')
        print('Sum of negative numbers:', sum_of_negative_integers)
        print('You entered', num_of_positive_integers, 'positive numbers' )
        print('Sum of positive numbers', sum_of_positive_integers)