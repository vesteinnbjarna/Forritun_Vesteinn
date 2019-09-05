low = int(input('Enter a lower number: '))
high = int(input('Enter a higher number: '))

counter = 0
sum_three_five = 0

for i in range(low, high):
    if i % 3 == 0 or i % 5 == 0:
        sum_three_five += i
    counter += 1
    if counter == high -1:
        print(sum_three_five)