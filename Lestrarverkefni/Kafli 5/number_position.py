def get_digit(number, position):
    """Return digit in position in number counting from right"""
    return number // (10**position)%10

number = int(input("Enter a number: "))
position = int(input("Enter its position: "))

num_pos = get_digit(number, position)

print(num_pos)