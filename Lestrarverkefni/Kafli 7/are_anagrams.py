# Anagram test

def are_anagram(word1, word2):
    '''Return true if words are anagrams'''

    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)
    return word1_sorted == word2_sorted




def main():
    
    valid_input_bool = False
    while not valid_input_bool:
        try:
            two_words = input('Enter two words seperated by space: ')
            word1,word2 = two_words.split()
            valid_input_bool = True

        except ValueError:
            print ("Bad Input")

    if are_anagram(word1,word2):
        print("The words {} and {} are anagrams.".format(word1, word2))
    else:
        print("The words {} and {} are not anagrams.".format(word1, word2))


main()