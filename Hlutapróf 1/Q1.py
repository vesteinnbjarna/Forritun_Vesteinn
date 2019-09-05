
# Age input variable
age = int(input('Enter your age: '))

# Setting age-range with a if elif else statement: 

if age >= 0 and  age <= 34:
    print('Young')
elif age >= 35 and  age <= 50:
    print('Mature')
elif age > 50 and age < 70:
    print('Middle-aged')
elif age >= 70:
    print('Old') 
else:
    print('Invalid age')