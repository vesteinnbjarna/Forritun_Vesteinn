
# Your functions should appear here
def enter_a_value(user_input):
    if user_input != exit:
        result = user_input.split()
        result = result+result+result
    return result
    
        

    
def print_results(a_list):
    result = []
    for word in a_list:
        if word != 'exit':
            result += word
    
    for word in result:
        print(word)


def main():
    the_list_of_values = []
    user_input = input('Enter a value: ')
    enter_a_value(user_input)
    the_list_of_values += enter_a_value(user_input)
    
    
    while user_input != 'exit':
        user_input = input('Enter a value: ')
        the_list_of_values += enter_a_value(user_input)
    
    if user_input == 'exit':
        print_results(the_list_of_values)
    


        
        
    



main()