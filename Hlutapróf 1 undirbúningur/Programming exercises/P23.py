low = int(input('Enter a lower number: '))
high = int(input('Enter a higher number: '))

counter = 0
sum_odds = 0

for i in range(low, high):
    if i % 2 != 0:
        sum_odds += i
    counter += 1
    if counter == high -1:
        print(sum_odds)