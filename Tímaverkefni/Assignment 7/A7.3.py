# The function definition goes here
def is_num_in_range(number):
    if number > 1 and number < 555:
        answer = str(number) + " is in range."
    else:
        answer = str(number) + " is outside the range!"
    
    return answer



num = int(input("Enter a number: "))

result = is_num_in_range(num)

print (result)

# You call the function here