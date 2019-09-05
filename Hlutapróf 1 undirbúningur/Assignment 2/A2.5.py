# Here is an algorithm to determine whether a year is a leap year:
# 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# 4. The year is a leap year (it has 366 days).
# 5. The year is not a leap year (it has 365 days).
# Write a program that prompts for a year and prints out True if the year is a leap year, 
# otherwise False.

year = int(input('Enter a year: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('The Year is a leap year!')
        else: 
            print('The Year is not a leap year')
    else:
        print ('The Year is a leap year!')
else:
    print('The year is not a leap year')