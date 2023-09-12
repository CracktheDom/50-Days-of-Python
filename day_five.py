#!/usr/bin/env python3

"""Create a function called my_discount. The function takes no
arguments but asks the user to input the price and the
discount (percentage) of the product. Once the user inputs the
price and discount, it calculates the price after the discount.
The function should return the price after the discount. For
example, if the user enters 150 as price and 15% as the discount,
your function should return 127.5."""


def my_discount():
    """
    Calculate the discounted price of a product.

    This function takes user input for the original price of a product in USD
    and the percentage discount, then calculates the discounted price by
    applying the discount to the original price.

    Returns:
        float: The discounted price rounded to 2 decimal places.
    """
    # Prompt the user for the original price in USD
    price = float(input("What is the price in USD? "))

    # Prompt the user for the percentage discount
    discount = float(input("What is the percent discount? "))

    # Calculate the discounted price and round it to 2 decimal places
    discounted_price = round(price * (1 - discount / 100), 2)

    return discounted_price


print(my_discount())
