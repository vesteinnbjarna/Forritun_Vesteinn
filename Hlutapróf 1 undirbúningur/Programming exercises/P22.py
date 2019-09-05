low = int(input('Enter a lower number: '))
high = int(input('Enter a higher number: '))
sum_high_low = 0
counter = 0
for i in range (low, high):
    sum_high_low +=i
    
    counter += 1
    if counter == high - 1:
        print('Sum = ', sum_high_low)
