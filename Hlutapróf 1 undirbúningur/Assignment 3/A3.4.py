# Write a program using a while statement, that given an int as the input, 
# prints all the factors of that number, one in each line.

# For example, if the input is
# 15

# The output will be
# 1
# 3
# 5

num = int(input('Input a number: '))

factor = 1

while num > factor:
    if num % factor == 0:
        print (factor)
    
    factor += 1
        
    
   