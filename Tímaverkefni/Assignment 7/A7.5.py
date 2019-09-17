
import string
# palindrome function definition goes here



def is_palindrom (imported_string):

    original_str = imported_string
    modified_str = original_str.lower()
    bad_chars = string.whitespace + string.punctuation

    for char in modified_str:
        if char in bad_chars:
            modified_str = modified_str.replace(char,'')
    
    if modified_str == modified_str [::-1]:
        answer = '"' + original_str + '"'+ " is a palindrome." 

    else:
        answer = '"' + original_str + '"' " is not a palindrome." 
    
    return answer
in_str = input("Enter a string: ")

result = is_palindrom(in_str)

print(result)

# call the function and print out the appropriate message