# Prime number checker

num = int(input('Enter a number: '))
factor = 1

while factor <= num:
    factor += 1
    if num % factor == 0 and factor < num:
       print(False)
       break

    if num == factor:
        print (True) 
        
    
    