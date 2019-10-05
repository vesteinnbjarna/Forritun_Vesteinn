


def read_real_numbers ():
    '''Gets the real numbers by user'''
    '''and turns it to a list'''
    user_input = input("Enter scores separated by space: ")
    user_input = user_input.split()
    return user_input


def list_sorted (a_list):
    '''sorts the numbers'''
    sorted_list = sorted(a_list)
    return sorted_list


def remove_lowest_two (a_list):
    '''removes the lowest two numbers'''
    new_list = a_list[2::]
    return new_list

def sum_of_num(a_list):
    '''turns the list to a string'''
    '''then the string to float'''
    '''then sums it'''
    sum_float = 0
    
    for element in a_list:
        a_list = []
        element = element.split()
        a_list += element
        new_str = ' '.join(a_list)
        my_float = float(new_str)
        sum_float += my_float

    print ('Sum of scores (two lowest removed):', sum_float)
    

def main():
    get_numbers = read_real_numbers()
    length_of_user_input = len(get_numbers)
    if length_of_user_input < 2:
        print('At least two scores needed!')
        quit()
    sorted_list = list_sorted (get_numbers)

    remove_lowest = remove_lowest_two(sorted_list)
    sum_of_num(remove_lowest)

    

main()