# Your function definition goes here
def upper_lower(user_str):
    lower = 0
    upper = 0
    for letter in user_str:
        if (letter.islower()):
            lower += 1
            
        elif(letter.isupper()):
            upper += 1
    
    return  upper, lower

user_input = input("Enter a string: ")

# Call the function here
answer = upper_lower(user_input)   
upper = answer[0]
lower = answer[-1]

print("Upper case count: ", upper)
print("Lower case count: ", lower)