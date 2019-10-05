

def open_file(filename):
    file_object = open(filename, "r")
    return file_object

def read_file(file_object):
    for line in file_object:
        line = line.strip()
        print(line)

def main ():
    file_name = input("Enter filename: ")
    file_object = open_file(file_name)
    read_file(file_object)

main()