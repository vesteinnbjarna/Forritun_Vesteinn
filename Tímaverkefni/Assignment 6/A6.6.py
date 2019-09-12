name = input("Input a name: ")


last, first = name.split()

first_transformed = first[0]
first_transformed = first_transformed.capitalize()
last_transformed = last.capitalize()
last_transformed = last_transformed[:-1]

print (first_transformed + '. ' + last_transformed)