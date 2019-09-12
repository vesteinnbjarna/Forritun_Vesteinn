m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

if m > n:
    smaller = n
else:
    smaller = m
gcd = 0
for i in range (1, smaller+1):
    if((m % i == 0) and (n % i == 0)) and i > 1:
        if i > gcd:
            gcd = i
    
print (gcd)
        