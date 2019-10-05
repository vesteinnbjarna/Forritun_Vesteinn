import string

def get_list ():
    a_string = input('Enter elements of list separated by commas: ')
    a_list = []
    for line in a_string:
        line = line.split()
        for i in range(len(line)):
            if line[i].isdigit() == False:
                print('Error only enter integers!')
                quit()
            else:
                line[i] = int(line[i])
                a_list += line
        
    
    return a_list

def are_eights (a_list):
    index = a_list.index('8')
    return index




def main():
    the_list = get_list()
    true_or_false = are_eights(the_list)
    print(true_or_false)


main ()