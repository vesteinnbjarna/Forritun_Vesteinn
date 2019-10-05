# The program should scramble each word in the text.txt
# with the following instructions:
#   1.The first and last letter of each word are left unscrambled
#   2. If there is punctuation attached to a word it should be left unscrambled
#   3. The letter m should not be scrambled
#   4. The letters between the first and the last letter should swap adjacent
#      letter.
# Lastly the user should be able to input the name of the file he wishes to scramble
# If no file contains that name he should get a error message:
#   File xxx.txt not found!
#   
# Steps to do this:
#   1. Create a function that opens the tries to open the file.
#      If it cannot open it it should print a out the error message:
#      file not found.
# 
# 
#

def open_file(file_object):
    '''A function that tries to open a file
        if the filename is not found it prints a
        errorr message'''
  
        file_object = open(file_object, "r")
    
    except FileNotFoundError:
        print('File', file_object, 'not found!')
    
    return file_object 

#def write_file(file_object):
#   out_file = open(file_object,'w')
#    sentence = ''
#    for line in file_object:
#        line = line.strip()
    
#    sentence = sentence + line
#    print (sentence)

#   return out_file


def read_file(file_object):
    new_line =''
    for line in file_object:
        line = line.strip()
        line = line.replace("\n",' ')
        new_line = line + new_line

        
    print(new_line)





def main():
    valid_input_bool = False
    while not valid_input_bool:
        file_name =input('Enter name of file: ')
        try:
            file_object = open_file(file_name)
    

main ()

