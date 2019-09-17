# find_min function definition goes here
def mininum(num1, num2):
    if num1 > num2:
        result = num2
    else:
        result = num1
    return result



first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
minimum = mininum(first, second)
# Call the function here
print("Minimum: ", minimum)