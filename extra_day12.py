#!/usr/bin/env python3

from datetime import datetime, timedelta

"""Write a function called age_in_minutes that tells a user how
old they are in minutes. Your code should ask the user to
enter their year of birth, and it should return their age in
minutes (by subtracting their year of birth to the current year).
Here are things to look out for:
a. The user can only input a 4-digit year of birth. For
example, 1930 is a valid year. However, entering any
number longer or less than 4 digits long should render
input invalid. Notify the user to input a four digits
number.
b. If a user enters a year before 1900, your code should
tell the user that input is invalid. If the user enters the
year after the current year, the code should tell the user,
to input a valid year.
The code should run until the user inputs a valid year.
Your function should return the user's age in minutes. For
example, if someone enters 1930, as their year of birth your
function should return:"""

def age_in_minutes() -> str:
	valid_input = False
	while not valid_input:
		birthyear = int(input("What is the year of your birth? "))
		if birthyear < 1900:
			valid_input = False
			print(f'Input a number greater than 1899')
		elif birthyear > datetime.today().year:
			valid_input = False
			print(f'Input a four digit number')
		else:
			valid_input = True
			delta = timedelta(days=(datetime.today().year - birthyear) * 365)
			return f"You are {delta.total_seconds() / 60:,.0f} minutes old."

print(age_in_minutes())

