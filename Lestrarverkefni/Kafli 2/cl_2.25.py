# Generate a hailstone sequence

number_str = input('Enter a positive iteger: ')
number = int(number_str)
count = 0

print('Starting with the number: ', number)
print('Sequence is: ', end=' ')

while number > 1: #stop when the sequence reaches 1

    if number % 2:
        number = number * 3 + 1 #number is odd
    else:
        number = number / 2 #number is even
    print(number, ",", end= ' ')

    count +=1

else:
    print()
    print("Sequence is ", count, " numbers long")