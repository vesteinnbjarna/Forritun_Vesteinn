a_str = input("Input a string: ")

new_str=''

for ch in a_str:
    if ch.isdigit():
        new_str += ch

print (new_str)