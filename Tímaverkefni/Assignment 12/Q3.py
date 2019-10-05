import string
def open_file():
    filename = input('Enter filename:')
    try:
        opened_file = open(filename, "r")
        return opened_file

    
    except Exception:
        print('Filename', filename, 'not found')
        quit()


def split_file(fileobject):
    
    a_list = []
    
    for line in fileobject:
        line = line.split()
        a_list.append(line)
    return a_list

def sort_list(a_list):
    a_new_list = sorted(a_list)
    return a_new_list

    
def remove_punc (a_list):
    new_list = []
    for element in a_list:
        for word in element:
            for letter in word:
                if letter in string.punctuation:
                    letter = letter.strip()
        a_list.append(element)
    
    return new_list




def main():
    file_Obj = open_file()
    splited_file = split_file(file_Obj)
    sorted_list = sort_list(splited_file)
    remove_the_punc = remove_punc(sorted_list)


main()