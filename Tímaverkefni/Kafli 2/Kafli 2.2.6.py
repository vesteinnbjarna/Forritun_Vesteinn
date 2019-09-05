int_str = input("Please give me an integer: ")
first_int = int(int_str)
int_str = input('Please give me a second integer: ')
second_int = int(int_str)

tens_count = 0
loop_count = 0

while first_int > 10 and second_int < 20:
    if first_int == 10 or second_int == 10:
        tens_count += 1
    first_int -=5
    second_int +=5
    loop_count += 1

print('tens_count: ', tens_count)
print('loop_count: ', loop_count)
print('first_int: ', first_int)
print('second_int: ',second_int)
                
