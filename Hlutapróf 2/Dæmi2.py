def open_file(user_input):
    file_obj = open(user_input,'r')
    return file_obj

def split_file(file_object):
    for word in file_object:
        a_list = []
        word.split()
        a_list += word
        for ch 


    return a_list


def length_of_list (a_list):
    length_list = len(a_list)
    return length_list


# Main
filename = input('Enter filename: ')
try:
    file_opened = open_file(filename)
except Exception:
    print('File', filename, 'not found!')
    quit()
file_split = split_file(file_opened)
