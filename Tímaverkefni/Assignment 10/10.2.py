
# The main program starts here
def string_to_list(user_input):
    result = user_input.replace(',',' ')
    result = result.split()
       


    return result




def main ():
    the_string = input("Enter the string: ")
    the_list = string_to_list(the_string)
# call your function here
    print(the_list)

main()
