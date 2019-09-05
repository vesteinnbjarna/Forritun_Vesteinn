top_num = int(input("Upper number for the range: ")) # Do not change this line

perfect_num = 0
sum_num = 0
for i in range (1,top_num):
    if i % 2 == 0:
        sum_num += i
        if sum_num == i:
            print (i)






