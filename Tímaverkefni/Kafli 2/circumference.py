# calculate the area and circumference of a circle from its radius
# Step 1: prompt for a radiurs
# Step 2: apply the area formula
# Step 3: Print out the results

import math

radius_str = input("Sláðu inn radíus hringsins: ")
radius_int = int(radius_str)

circumference = 2 * math.pi * radius_int
area = math.pi * (radius_int ** 2)


print ("Ummál hringsins er:" , circumference, \
       ", and the area is:", area)
