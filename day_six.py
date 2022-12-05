#!/usr/bin/env python3

# written by CrackThaDom on 11/25/22

"""Write a function called user_name that generates a username
from the user’s email. The code should ask the user to input an
email and the code should return everything before the @ sign
as their user name. For example, if someone enters
ben@gmail.com, the code should return ben as their user
name."""

def user_name() -> str:
	email = input(f'What is your email address? ')
	return email[:email.find("@")]

print(user_name())