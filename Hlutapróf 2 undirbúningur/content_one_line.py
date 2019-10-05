def open_file(filename):
    file_obj = open(filename, 'r')
    return file_obj

def process_file (file_obj):
    line_str = ''

    for line in file_obj:
        line = line.strip
        line = line.replace(" ","")
        line_str += line
        
        print(line_str)


def main ():
    file_object = open_file('test.txt')
    process_file(file_object)
    file_object.close()
    