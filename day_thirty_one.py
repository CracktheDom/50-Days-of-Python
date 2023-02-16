#!/usr/bin/env python3

from time import sleep


"""Write a function that has one parameter and takes a list of words
as an argument. The function returns the longest word from the
list. Name the function longest_word. The function should
return the longest word and the number of letters in that word.
For example, if you pass [‘Java, ‘JavaScript’, ‘Python’], your
function should return
[10, JavaScript] as the longest word.
"""


def longest_word(wordList: list) -> list:
    longest = max(wordList, key=len)
    return [len(longest), longest]


"""Extra Challenge: Create User
Write a function called create_user. This function asks the
user to enter their name, age, and password. The function
saves this information in a dictionary. For example, if the use
enters name as Peter, age - 18 and password - love. The
function should save the information as: {'name': 'Peter',
'age': 18, 'password': 'love'}
Once the information is saved. The function should print to the
user that - "User saved. Please login"
The function should then ask the user to re-enter their name
and password. If the name and password match with what is
saved in the dictionary, the function should return "Logged in
successfully". If the name and password do not match with
what is saved in the dictionary, the function should print
('Wrong password or user name. Please try again'. The
function should keep running until the user enters correct
logging details."""


def create_user():

    name = input("What is your name? ")
    age = input("What is your age? ")
    password = input("What is your password? ")
    userDict = {name: [age, password]}
    sleep(2)

    print(f"User saved. Please login")
    isLoggedIn = False

    while not isLoggedIn:
        query_name = input("Enter your username: ")
        query_password = input("Enter your password: ")
        sleep(2)

        if query_name in userDict and query_password == userDict[query_name][1]:
            isLoggedIn = True
            print(f"Logged in successfully")
        else:
            print(f"Wrong password or username. Please try again")


print(longest_word(['supercalifragilouseckpeialdous',
      'Java', 'Haskell', 'JavaScript', 'Python']))
create_user()
