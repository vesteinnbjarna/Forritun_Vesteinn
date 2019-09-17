# Prenta fjölda út fjölda tölustafa í innslegnum streng

# Fá streng frá notanda
# Reikna út fjölda tölustafa í streng
# Prenta út niðurstöðu

def get_string_from_user():
    '''Gets a string from the user and returns it'''
    a_string = input("Enter a string: ")
    return a_string


def count_digits(a_str):
    '''Returns the count of digits in a string'''
    counter = 0
    for ch in a_str: 
        if ch.isdigit():
            counter += 1
    
    return counter


a_str = get_string_from_user()

count = count_digits(a_str)
print(count)

