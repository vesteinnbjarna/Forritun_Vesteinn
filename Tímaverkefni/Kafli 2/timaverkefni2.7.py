age = int(input("Input age: ")) # Do not change this line

# Fill in the missing code below
ticket_price = float(30.0)

if age >= 65:
    ticket_price = 0.5 * 30.0
elif age <= 5:
    ticket_price = 0.0
else:
    ticket_price = 30.0

print(ticket_price)
