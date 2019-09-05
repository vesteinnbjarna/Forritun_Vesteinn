# King’s Island needs a program for its admission booths. When visitors to the park 
# come up to the booth to purchase their tickets, the worker uses this program to figure out
# how much to charge them.

# Each ticket cost $30. Senior citizens (age >= 65) are given a 50% discount. 
# Children under (or equal to) the age of 5 get a free admission.
# Write a program that prompts for the visitor's age and computes and 
# prints the ticket price (which should be a float).

ticket_price = 35.0

age = float(input('Enter your age: '))

if age >= 65:
    ticket_price = ticket_price * 0.5
    

elif age <= 5:
    ticket_price = 0

else: 
    ticket_price = ticket_price

print ('Ticket price:', ticket_price)
    
