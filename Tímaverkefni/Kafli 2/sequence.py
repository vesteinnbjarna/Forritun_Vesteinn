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



m_first = 1
m_second = 2
m_third = 3 
m_sum = 0

n = int(input("Enter the length of the sequence: ")) # Do not change this line 


for i in range (1, n+1):
    if i == 1:
        print (1)
    if i == 2:
        print (2)
    if i == 3:
        print(3)
    
    if i > 3:
        m_sum = m_first + m_second + m_third
        print (m_sum)
        m_first = m_second
        m_second = m_third
        m_third = m_sum

        

    
    
