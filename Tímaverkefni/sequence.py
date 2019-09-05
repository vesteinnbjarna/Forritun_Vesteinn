# Design an algorithm that generates the first n numbers in the following sequence:; 
# 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
# Make sure that you write up the algorithm before starting to code.
# Then implement the algorithm in Python. Put your algorihmic
# description as a comment in the program file.

# Runan er 1, 2, 3, 6, 11, 20, 37
# M.ö.o. þá er útkoma stærri tölunar alltaf summa tveggja talnanna á undan
# Markmiðið er þá að búa til þrjár breytur: 
# smaller_int, bigger_int og sum_int
# Þar sem smaller_int er alltaf fyrri minni talan og bigger_int 
# sú seinni og sum_int er summa þeirra
# Síðan er þarf notandinn alltaf að slá inn hversu margar tölur hann vill prenta út
#


n = int(input("Enter the length of the sequence: ")) # Do not change this line