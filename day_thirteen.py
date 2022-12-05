#!/usr/bin/env python3

"""Write a function called your_vat. The function takes no
parameter. The function asks the user to input the price of an
item and VAT (vat should be a percentage). The function should
return the price of the item plus VAT. If the price is 220 and,
VAT is 15% your code should return a vat inclusive price of 253.
Make sure that your code can handle ValueError. Ensure the
code runs until valid numbers are entered. (hint: Your code
should include a while loop)."""

# TODO: much to do

def isValidInput():
	pass

def your_vat() -> float:
	valid_price = False
	valid_vat = False
	price = input("What is the price of the item? ")
	
	while not valid_price:
		if not price.isnumeric():
			valid_price = False
			price = input("Please input valid number\nWhat is the price of the item? ")
		else:
			valid_price = True
			price = float(price)

	vat = input("What is the VAT? ")
	while not valid_vat:
		if not vat.isnumeric():
			valid_vat = False
			vat = input('Please input a positive number\nWhat is the V.A.T.? ')
		else:
			valid_vat = True
			vat = float(vat)
	return(price * (1 + vat / 100))

print(your_vat())