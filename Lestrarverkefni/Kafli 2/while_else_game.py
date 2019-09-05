# while-else
# simple guessing game: Start with a random number and 
# guess with hints until you guess the correct number
# If the users guesses a number not in range it quits the program
# All non-typed variables are integers 

import random # get the random number module
number = random.randint(0,100) # to randomize the number between 0-100

print('Hi-Low guessing game between 0 and 100 inclusive.')
print(' ')

guess_str = input('Guess a number: ')
guess = int(guess_str) #converting int to string

while 0 <= guess <= 100:
    if guess > number:
        print('Guess is too high.')
    elif guess < number: 
        print('Guess is too low.')
    else:
        print('You guessed it! The number was: ', number)
        break

    # keep trying
    guess_str = input('Guess a number: ')
    guess = int(guess_str)
else:
    print('You quit early! The number was: ', number)

