# Algorithm
# User will input a integer: 
# The algorithm will continue to run while the number
# is positive or > 0
# if a user enters a number less than 0 it will stop
# running. If the user enters a string it will tell 
# the user that his input is invalid and ask him
# to enter a number:



num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code

max_int = 0

while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line





