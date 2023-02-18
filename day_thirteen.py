#!/usr/bin/env python3

"""Write a function called your_vat. The function takes no
parameter. The function asks the user to input the price of an
item and VAT (vat should be a percentage). The function should
return the price of the item plus VAT. If the price is 220 and,
VAT is 15% your code should return a vat inclusive price of 253.
Make sure that your code can handle ValueError. Ensure the
code runs until valid numbers are entered. (hint: Your code
should include a while loop)."""


def your_vat() -> float:
    isValidPrice = False
    isValidVAT = False
    price = input("What is the price of the item? ")
    vat = input("What is the VAT? ")

    while not isValidPrice and not isValidVAT:
        if not price.isnumeric():
            isValidPrice = False
            price = input(
                "Please input valid number\nWhat is the price of the item? ")
        else:
            isValidPrice = True
            price = float(price)

        if not vat.isnumeric():
            isValidVAT = False
            vat = input('Please input a positive number\nWhat is the V.A.T.? ')
        else:
            isValidVAT = True
            vat = float(vat)
    return (price * (1 + vat / 100))


print(your_vat())
