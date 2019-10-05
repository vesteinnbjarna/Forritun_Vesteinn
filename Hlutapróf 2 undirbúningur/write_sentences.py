def open_file(filename):
    file_obj = open(filename, 'r')
    return file_obj


def write_sentences(word_file):
    sent_file = open('sentences.txt','w')
    sentence = ''
    for word in word_file: 
        if word == '.': 
            word = word.strip()
            sentence = sentence.strip() + "."
            sent_file.write(sentence + "\n")
            print(sentence)
            sentence = ''
        elif word == ' ':
            continue
        elif word == ',':
            sentence = sentence.strip() + ','
        else:
            sentence = sentence + word + ' '

def main():
    filename = input('Enter filename: ')
    file_object = open_file(filename)
    write_sentences(file_object)
    file_object.close()