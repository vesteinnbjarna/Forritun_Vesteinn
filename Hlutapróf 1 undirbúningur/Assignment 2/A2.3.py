# Write a program that reads in 3 integers and prints out the maximum of the three. 

int_1 = int(input('Enter a integer: '))
int_2 = int(input('Enter a integer: '))
int_3 = int(input('Enter a integer: '))

if int_1 >= int_2 and int_1 >= int_3:
    highest_int = int_1

elif int_2 >= int_1 and int_2 >= int_3:
    highest_int = int_2

else:
    highest_int = int_3

print ('The highest number was: ',highest_int)