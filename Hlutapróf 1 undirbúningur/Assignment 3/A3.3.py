# Write a program using a while statement, 
# that given a series of numbers as input, 
# adds them up until the input is 10 and then prints the total.
# Do not add the final 10.

# For example, if the following numbers are input
# 8
# 3
# 11
# 10

# The output should be:
# 22

num = int(input("Input an int: ")) # Do not change this line

# Fill in the missing code below
num_sum = 0
while num != 10:
    num_sum += num
    num = int(input("Input an int: "))
    
    if num == 10:
        print(num_sum)
   