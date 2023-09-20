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
    """
    Function to save email addresses to a CSV file.

    This function allows the user to input email addresses, one at a time, and
    appends them to a CSV file named 'emails.csv'. To stop entering email
    addresses, the user can type 'done'.

    Args:
        None

    Returns:
        None

    Example:
        To use this function, call it from your Python code:

        >>> save_emails()

        This will prompt the user to input email addresses until they type
        'done'. The entered email addresses will be saved in 'emails.csv' with
        each email on a new line.

    """
    with open("./emails.csv", "a") as file_object:
        is_done_inputting_email = False
        print("Enter 'done' if you are finished entering email addresses\n")
        while not is_done_inputting_email:
            email = input("Enter email address:  ")
            if email == "done":
                is_done_inputting_email = True
            else:
                file_object.write(f"{email}\n")


def open_emails():
    """
    Open the 'emails.csv' file in read mode.

    This function opens the 'emails.csv' file for reading and returns a file
    object that can be used to read the contents of the file.

    Returns:
        None

    Raises:
        FileNotFoundError: If the 'emails.csv' file does not exist.

    Example:
        file_obj = open_emails()
        contents = file_obj.read()
        file_obj.close()
    """
    try:
        with open("./emails.csv", "r") as fileObj:
            # Read the contents of the file
            # (this line doesn't store or return the data)
            fileObj.read()
    except FileNotFoundError:
        raise FileNotFoundError("The 'emails.csv' file does not exist.")


save_emails()
open_emails()
