
for i in range (10,100):
    num_1 = i // 10
    num_2 = i % 10
    sum_of_uniq_num_pwr_2 = (num_1+num_2)**2

    if sum_of_uniq_num_pwr_2 == i:
        print (i)
    