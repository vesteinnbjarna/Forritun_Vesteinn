my_int = int(input('Give me an int >= 0: '))
# Fill in the missing code
my_bin =''

my_int2 = my_int

if my_int == 0:
    my_bin ='0'

while my_int2 > 0:
    my_bin = my_bin + str(my_int2%2)
    my_int2 = my_int2 //2

my_bin = my_bin[::-1]

print("The binary of", my_int, "is", my_bin)
