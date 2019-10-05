
def  my_function(param_list):
    print("param_list before modification: ", param_list)
    param_list[0] = 100
    print('param_list after modification: ', param_list)

def get_list_from_user():
    a_list = input('Enter a list seperated by space: ')
    a_list = a_list.split()
    return a_list

# Main:

list_from_user = get_list_from_user()
my_function(list_from_user)
