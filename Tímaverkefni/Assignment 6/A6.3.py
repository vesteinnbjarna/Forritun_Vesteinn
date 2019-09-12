a_str = input("Input a string: ")

target_str = 'o'

for index,letter in enumerate(a_str):
    if letter == target_str:
        print (index)