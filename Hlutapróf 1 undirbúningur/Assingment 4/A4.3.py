# If a chessboard were to have wheat placed upon each square such 
# that one grain were placed on the first square, two on the second, 
# four on the third, and so on (doubling the number of grains on 
# each subsequent square), how many grains of wheat would be on the 
# chessboard at the finish?

# Write a Python program using a for loop that 
# calculates and prints out this number of grains.

summa = 1

for i in range(1,65):
    summa *=2

    if i == 64:
        print (summa-1)