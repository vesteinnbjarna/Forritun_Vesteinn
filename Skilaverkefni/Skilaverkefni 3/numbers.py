# The program should do the following:
# If a two digit number is exactly = (sum of it's digits)**2
# it should print the number.
# The program should also print all the two digit numbers that have exactly 
# 10 divisors.



answer_1 = 0
answer_2 = 0
answer_3 = 0
    



for i in range (10,100):
    
    
    num_1 = i // 10         # Finding the first digit of two digit number
    num_2 = i % 10          # Finding the second digit of two digit number
    sum_of_uniq_num_pwr_2 = (num_1+num_2)**2    # Squaring the sum of the digits

    if sum_of_uniq_num_pwr_2 == i:      
        answer_1 =i 

    
    divisor_counter = 0
    n = 0
    while i >= n:
        n += 1
        if i % n == 0:
            divisor_counter += 1
    
    # Added these two if loops to get the correct output
    if divisor_counter == 10 and answer_2 == 0:
        answer_2 = i
    
    if divisor_counter == 10 and answer_2 < i:
        answer_3 = i
        
    

print(answer_1) # sum of square of the digits
print(answer_2) # lower number with 10 divisors
print(answer_3) # higher number with 10 divisors