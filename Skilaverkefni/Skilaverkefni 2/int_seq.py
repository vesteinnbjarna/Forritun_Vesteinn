
#  Write an integer bigger than greater than 0:

num = int(input('Enter an integer: '))

# Creating sum counter for even and odd numbers
# Also creating total sum variable and a variable for 
# That stores the largest number

even_sum = 0
odd_sum = 0
total_sum = 0
largest_num = 0

# Starting the while loop 
# instructions say that the loop must stop if the number is less
# than or equal to 0
# so that means every number greater than zero is a viable input 
# into the loop 

while num > 0:
    # Storing cumlative total here
    total_sum += num
    print('Cumulative total:', total_sum)

    # Storing the largest number
    if num > largest_num:
        largest_num = num

    # Storing even and odd numbers with this if else statement
    if num % 2 == 0:
        even_sum += 1
    else:
        odd_sum += 1
        
    # Reseting the loop
    num = int(input('Enter an integer: '))

    # Stopping the loop
    if num <= 0:
        print('Largest number:', largest_num)
        print('Count of even numbers:', even_sum)
        print('Count of odd numbers:', odd_sum)