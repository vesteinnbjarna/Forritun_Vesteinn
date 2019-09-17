# is_prime function definition goes here
def is_prime(number):
    counter = 2
    answer = str(number) + " is a prime"
    while num > counter:  
        if number % counter == 0:
            answer = str(number)+" is not a prime"
        counter +=1

    return answer






num = int(input("Input an integer greater than 1: "))
result = is_prime(num)
print(result)
# Call the function here and print out the appropriate message