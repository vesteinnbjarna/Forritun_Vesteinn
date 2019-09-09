for i in range (10,100):
    divisor_counter = 0
    n = 0
    while i >= n:
        n += 1
        if i % n == 0:
            divisor_counter += 1
    
    if divisor_counter == 10:
        print (i)