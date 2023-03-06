#!/usr/bin/env python3

import re

"""Write a function called password_validator. The function
asks the user to enter a password. A valid password should have
at least one upper letter, one lower letter, and one
number. It should not be less than 8 characters long. When
the user enters a password, the function should check if the
password is valid. If the password is valid, the function should
return the valid password. If the password is not valid, the
function should tell the users the errors in the password and
prompt the user to enter another password. The code should
only stop once the user enters a valid password. (use while loop)."""


def pasword_validator():
    hasLower = False
    hasDigit = False
    hasUpper = False

    while not isValidPassword:
        response = input("Enter your password: ")
        password_length = len(password)

        if password_length >= 8:
            # check if string has at least one lowercase letter
            if any(char.islower() for char in response):
                hasLower = True
            else:
                print("Password must contain at least one lowercase letter")

            # check if string has at least one uppercase letter
            if any(char.isupper() for char in response):
                hasUpper = True
            else:
                print("Password must contain at least one uppercase letter")

            # check if string has at least one digit
            if any(char.isdigit() for char in response):
                hasDigit = True
            else:
                print("Password must contain at least one digit")
        else:
            print("Password must be 8 characters or more.")

        if hasDigit and hasUpper and hasLower and password_length >= 8:
            isValidPassword = True
            return response


"""Extra Challenge: Valid Email
emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com' ]
Write a function called email_validator that takes a list of
emails and checks if the emails are valid. The function returns a
list of only valid emails. A valid email address will have the
following - @ symbol (if the @ sign is at the beginning of the
name, the email is invalid. If there are more than one @signs,
the email is invalid. All valid emails must have a dot com at the
end (.com), if not, the email is invalid. For example, the list of
emails above should output the following as valid emails:
['ben@mail.com', 'kenny@gmail.com']
If no emails in the list are valid, the function should return 'all emails are
invalid'"""
