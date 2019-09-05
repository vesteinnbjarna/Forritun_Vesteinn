import math
x_1 = int(input('Enter the first x coordinate: '))
y_1 = int(input('Enter the first y coordinate: '))
x_2 = int(input('Enter the second x coordinate: '))
y_2 = int(input('Enter the second y coordinate: '))

euclidean_distance = math.sqrt((y_1-x_1)**2 +(y_2-x_2)**2)

print ('The distance between the two point is: ',euclidean_distance)
