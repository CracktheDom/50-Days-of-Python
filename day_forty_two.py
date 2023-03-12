#!/usr/bin/env python3

from textblob import Word
import winsound


"""Write a function called spelling_checker. This code asks the
user to input a word and if a user inputs a wrong spelling it
should suggest the correct spelling by asking the user if they
meant to type that word. If the user says no, it should ask the
user to enter the word again. If the user says yes, it should
return the correct word. If the word entered by the user is
correctly spelled the function should return the correct word.
Use the module textblob."""


def spelling_checker():
    while True:
        userInput = input("Enter a word to check its spelling: ")
        wordObj = Word(userInput)

        if wordObj.spellcheck()[0][0] == userInput:
            print(f"{userInput} is spelled correctly")
            return userInput
        else:
            suggestion = wordObj.spellcheck()[0][0]
            choice = input(f"Do you mean {suggestion}? {y/n}")
            if choice.lower() == 'y':
                return suggestion


"""
Extra Challenge: Create an Alarm clock
Create a function called alarm that sets an alarm clock for the
user. The function should ask the user to enter time they want
the alarm to go off. The user should enter the hour and
minute. The function should then print out the time when the
alarm will go off. When its alarm time, the code should let off a
sound. Use the winsound module for sound."""


def alarm():
    pass
    # TODO: all of it


word = spelling_checker()
