# first and step inputs:

first = int(input('First: '))
step = int(input('Step: '))

# creating counters for sum of series and counter to + the step with 
# in the loop 

sum_of_series = 0
counter = first


while sum_of_series <= 100:
    print (counter, end = ' ')
    sum_of_series += counter
    counter += step
    
    if sum_of_series >= 100:
        print (' ')
        print('Sum of series:',sum_of_series)



