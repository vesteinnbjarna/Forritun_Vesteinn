def fibo(n):
    n1 = 1
    n2 = 1
    count = 0

    if n == 1:
        print (n1)
    else: 
        while count < n:
            if n1 != 0:
                print (n1, end= ' ')
            fib = n1+n2
            n1 = n2
            n2 = fib
            count += 1


n = int(input("Input the length of Fibonacci sequence (n>=1): "))

fibo(n)