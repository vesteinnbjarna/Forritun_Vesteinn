# The program reads a file called test.txt 
# and prints out the content after removing all spaces and lewlines. 
# punctuation will be preserved.


def open_file(filename):
    file_object = open(filename, "r")
    return file_object

name_of_file = 'test.txt'
open_file(name_of_file)

