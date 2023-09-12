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
    """
    Calculate the total price of an item including VAT.

    This function prompts the user to input the price of an item and the VAT
     rate, and then calculates the total price including VAT.

    Returns:
        float: The total price including VAT.
    """
    isValidPrice = False
    isValidVAT = False

    while not isValidPrice:
        price = float(input("Please input price for item: "))
        print()  # Print blank line
        if not isinstance(price, float) or float(price) < 0:
            isValidPrice = False
            print("Input for price must be positive number")
        else:
            isValidPrice = True
            price = float(price)

    while not isValidVAT:
        vat = float(input("Please input a value for the V.A.T.? "))
        if not isinstance(vat, float) or float(vat) < 0:
            isValidVAT = False
            print("Input for V.A.T. must be positive number")
        else:
            isValidVAT = True
    return price * (1 + vat / 100)


print(your_vat())
