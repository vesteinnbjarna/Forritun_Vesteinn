def evens(n):
    evens_list = []
    #to get "n" numbers starting at 1, range must go to "n+1"
    for i in range (1,n+1):
        evens_list.append(2*i)
    return evens_list

starting_point = int(input('Enter a integer: '))
print(evens(starting_point))