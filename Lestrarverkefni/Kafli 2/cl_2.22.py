# sum up a series of even numbers
# make sure user input is even number

print('Allow the user to enter a series of even integers. Sum them. ')
print('Ignore odd inputs. End session by typing:"."')

number_str = input('Enter a number: ')
the_sum = 0

while number_str != '.':
    number = int(number_str)
    if number % 2 == 1: # odd number
        print('Error. Even numbers pls.')
    else:
        the_sum += number
    number_str = input('Enter a number: ')

print('The sum is ', the_sum)

