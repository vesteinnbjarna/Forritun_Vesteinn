from operator import itemgetter

L = [['sarah', 'Jr', 30], ['rich', 'So', 10], ['bill', 'Jr', 20]]

print(L)

print('Sorted L:')
sorted(L)
print(sorted(L))

print ('Sorted L, key=itemgetter(1)')

print(sorted(L,key=itemgetter(1)))

print ('Sorted L, key=itemgetter(2)')

print(sorted(L,key=itemgetter(2)))

print ('Sorted L, key=itemgetter(1,2)')

print(sorted(L,key=itemgetter(1,2)))