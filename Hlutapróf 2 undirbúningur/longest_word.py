
def open_file(filename):
    file_obj = open(filename, 'r')
    return file_obj

def find_longest(file_object):
    '''Return the longest word and its length found in the given file'''
    max_length = 0
    longest_word = ""

    for word in file_object:
        word = word.strip()
        length = len(word)
        if length > max_length:
            longest_word = word
            max_length = length
    return longest_word, max_length

def main():
    filename = input('Enter filename: ')
    file_object = open_file(filename)
    longest, length = find_longest(file_object)
    print("Longest word is '{:s} of length {:d}".format(longest, length))
    file_object.close()
