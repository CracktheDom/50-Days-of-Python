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


def password_validator():
    """
    Validates a user-entered password to ensure it meets certain criteria.

    This function checks that a password meets the following requirements:
    - It must be at least 8 characters long.
    - It must contain at least one lowercase letter.
    - It must contain at least one uppercase letter.
    - It must contain at least one digit.

    If the password does not meet these requirements, the user will be prompted
    to enter a new password until a valid one is provided.

    Returns:
        None

    """
    # Initialize flags to track whether the password meets criteria.
    has_lower = False
    has_digit = False
    has_upper = False

    # Initialize the boolean variable to avoid an infinite while loop.
    is_valid_password: bool = has_lower and has_upper and has_digit

    # Continue prompting the user until a valid password is provided.
    while not is_valid_password:
        response: str = input("Enter your password: ")
        has_sufficient_password_length: bool = len(response) >= 8

        # Check if the password meets the length requirement.
        if has_sufficient_password_length:
            # Check if the password contains at least one lowercase letter.
            has_lower = any(char.islower() for char in response)
            if not has_lower:
                print("Password must contain at least one lowercase letter")

            # Check if the password contains at least one uppercase letter.
            has_upper = any(char.isupper() for char in response)
            if not has_upper:
                print("Password must contain at least one uppercase letter")

            # Check if the password contains at least one digit.
            has_digit = any(char.isdigit() for char in response)
            if not has_digit:
                has_digit = False
                print("Password must contain at least one digit")
        else:
            print("Password must be 8 characters or more.")

        # Update the validity flag based on all criteria.
        is_valid_password = (
            has_digit and has_upper and has_lower and has_sufficient_password_length
        )

    # Print the entered password (for demonstration purposes).
    print(response)


"""Extra Challenge: Valid Email
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

emails = ["ben@mail.com", "john@mail.cm", "kenny@gmail.com", "@list.com"]


def email_validator(email_list: list[str]) -> str | list[str]:
    """
    Validate a list of email addresses.

    Args:
        email_list (list[str]): A list of email addresses to be validated.

    Returns:
        Union[str, list[str]]: Returns a message or a list of valid email
            addresses. If all emails are invalid, it returns "all emails are
            invalid." Otherwise, it returns a list of valid email addresses.

    Example:
        >>> email_validator(["john@example.com", "jane@openai"])
        ['john@example.com']
        >>> email_validator(["invalid", "@invalid.com"])
        'all emails are invalid'
    """
    valid_email_list: list[str] = [
        email_address
        for email_address in email_list
        if email_address[0] != "@"  # Check if email doesn't start with "@"
        and email_address.count("@") == 1  # Check if there's exactly one "@" symbol
        and email_address.endswith(".com")  # Check if email ends with ".com"
    ]
    return "all emails are invalid" if not valid_email_list else valid_email_list


print(email_validator(emails))
password_validator()
