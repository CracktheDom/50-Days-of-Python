#!/usr/bin/env python3

"""Write a function called same_in_reverse that takes a string
and checks if the string reads the same in reverse. If it is the
same, the code should return True if not, it should return False.
For example, 'dad' should return True, because it reads the
same in reverse."""


def same_in_reverse(string: str) -> bool:
    return string == string[::-1]


"""Write a function called your_age. This function asks a student
to enter their name and then it returns their age. For example, if
a user enters Peter as their name, your function should return,
'Hi, Peter, you are 27 years old. This function reads data
from the database (dictionary below). If the name is not in the
dictionary, your code should tell the user that their name is not
in the dictionary, and ask them for their age. Your code should
then add the name and age to the dictionary of names_age
below. Once added your code should return to the user 'Hi,
(added name), you are (added age) years old'. Remember
to convert the input from user to lowercase letters"""


def your_age():
    name = input("What is your name? ").lower()

    if name not in names_age.keys():
        print(f"Your name, {name}, is not in the dictionary.")
        age = input("What is your age? ")
        names_age[name] = age
        return (f"Hi, {name}, you are {names_age[name]} years old.")
    else:
        return (f"Hi, {name}, you are {names_age[name]} years old.")


names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}


print(same_in_reverse('civic'))
print(same_in_reverse('pop'))
print(same_in_reverse("deified"))
print(same_in_reverse("nurses run"))
print(same_in_reverse("tenet"))
print(same_in_reverse("level"))

print(your_age())
print(your_age())
