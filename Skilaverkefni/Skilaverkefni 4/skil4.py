
# This is the main function
# It takes one variable and turns it into the index which is than used to 
# print out the new players position

def the_game(players_move):
    new_position =''
    new_position ="".join((position_string[:players_move]+'o'+ position_string[players_move:]))
    return new_position

position_string = 'xxxxxxxxx'

# Because we are working with a string with 10 inputs
# Since python starts counting from 0 we need to adjust the range
player_position = int(input('Input a poisition between 1 and 10: ')) -1

if player_position < 0 or player_position > 9:
    print('Invalid input.')
    player_position = int(input('Input a poisition between 1 and 10: '))

# Calling the function for the first time to show us the first starting position
first_position = the_game(player_position)
print (first_position)

print('l - for moving left')
print('r - for moving right')
print('Any other letter for quitting.')

moving_direction = input('Enter your choice: ')

while moving_direction == 'l' or moving_direction == 'r':
    
    # -1 basicly means to move to the left
    if moving_direction == 'l':
        player_position -=1

        # Needed to add this otherwise the loop would continue to decrease the player position
        # value way below zero
        if player_position <  0:
            player_position = 0

    # +1 basicly means the same as to move to the right
    elif moving_direction == 'r':
        player_position += 1

        # Same as before but the function would continue to give player position values
        # way over 9
        if player_position > 9:
            player_position = 9

    answer = the_game(player_position)
    print(answer)

    moving_direction = input('Enter your choice: ')


# If the user enters something other 'l' or 'r' he goes here 
if moving_direction != 'l' or moving_direction != 'r':
    answer = the_game(player_position)
    print(answer)
        

