#!/usr/bin/env python3

"""Create a function called save_emails. This function takes no
arguments but asks the user to input email, and it saves the
emails in a CSV file. The user can input as many emails as they
want. Once they hit ‘done’ the function saves the emails and
closes the file. Create another function called open_emails.
This function opens and reads the content of the CSV file. Each
email must be in its line. Here is an example of how the emails
must be saved:
jj@gmail.com
kate@yahoo.com
and not like this:
jj@gmail.comkate@yahoo.com"""


def save_emails():
	with open("./emails.csv", "a") as fileObj:
		isDone = False
		print("Enter 'done' if you are finished entering email addresses\n")
		while not isDone:
			email = input("Enter email address:  ")
			if email == 'done':
				isDone = True
			else:
				fileObj.write(f"{email}\n")


def open_emails():
	with open("./emails.csv", "r") as fileObj:
		fileObj.read()
		return fileObj


save_emails()
open_emails()