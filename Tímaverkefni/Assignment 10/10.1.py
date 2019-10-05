import string

# Implement a function here
def clean_sentece(user_input):
    result = []
    user_input = user_input.replace(' ', '')
    for char in user_input:
        if char not in string.punctuation:
            result +=char
    return result



def get_unique_letters(clean_list):
    result = []
    for char in clean_list:
        for char in clean_list:
            if char not in result:
                result += char
    return result


# Main starts here
def main():
    sentence = input("Input a sentence: ")
    # Call the function here
    a_list = clean_sentece(sentence)
    unique_letters = get_unique_letters(a_list)


    print("Unique letters:", unique_letters)

main ()