# Create a program that asks the user to open a file
# If the user input is not valid it should keep asking until the user
# enters a valid file
# Next the program should ask the user for a year
# If the year is not in the file

#def enter_a_file_name ():
#   '''Enter a filename'''
#  filename = input("Enter a filename: ")
#   return filename

def open_file (filename):
    '''opens file for reading'''
    try:
        result = open("filename","r")
    except Exception:
        print("Filename", filename, "not found!")
    
    return result
 

    

        

def file_to_list(filename):
    a_list = []
    for word in filename:
        word = word.split()
        a_list += word
    return a_list

def is_year_in_list(year, a_list):
    if year in a_list:
        return True
    else:
        return False
    



def lists_sorted(list):
    pass

def max_population(file):
    pass

def min_population(file):
    pass

def print_results(a,b):
    pass

def main():
    filename = input("Enter a filename: ")
    
    file_opened = open_file(filename)

   
        
    
    list_file = file_to_list(file_opened)
    

    # Creating a while loop that keeps asking
    # the user for a valid year
    is_year_in_file = False
    year = input("Enter a year: ")
    while not is_year_in_file:
    
        if is_year_in_list(year,list_file):
            is_year_in_file = True
        else:
            is_year_in_file = False
            year = input("Enter a year: ")
            





main()




