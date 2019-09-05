# Accept d1 and d2, the number on two dices as input. First, check to see that they are
# in the proper range for dice (1-6). If not, print the message "Invalid input". 
# Otherwise, determine the sum. If the sum is 7 or 11, print "Winner". 
# If the sum is 2, 3 or 12, print "Loser". Otherwise print the sum.

d1 = int(input('Input of the first dice: '))
d2 = int(input('Input of the second dice: '))

if d1 < 1 or d1 > 6 or d2 < 1 or d2 > 6:
    print ('Invalid input!')

else:
    d_sum = d1 + d2
    if d_sum == 7 or d_sum == 11:
        print ('Winner')
    elif d_sum == 2 or d_sum == 3 or d_sum == 12:
        print('Loser')
    else:
        print(d_sum) 