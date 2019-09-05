# Write a program that prompts for a grade (a float).  A valid grade is between 0.0 and 10.0 (both 
# inclusive).  A passing grade is between 5.0 and 10.0 (both inclusive).  The program pints out 
# "Invalid grade!", "Passing grade!", or "Failing grade!", depending on the input.

grade = float(input('Enter your grade: '))

if grade <= 10 and grade >= 0:
    if grade >= 5:
        print ('Passing grade!')
    else:
        print('Failing grade!')

else:
    print('Invalid input!')