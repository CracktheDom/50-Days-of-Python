#!/usr/bin/env python3

import random

"""Write a function called guess_a_number. The function
should ask a user to guess a randomly generated number. If the
user guesses a higher number, the code should tell them that the
guess is too high, if the user guesses low, the code should tell
them that their guess is too low. The user should get a maximum
of three guesses. When the user guesses right, the code should
declare them a winner. After three wrong guesses, the code
should declare them a loser."""


def guess_a_number():
    count = 1
    random_num = random.randint(1, 50)
    does_guess_match = False
    guess = int(input("Guess a number between 1 and 50: "))
    while count < 3 and not does_guess_match:
        if guess < random_num:
            guess = int(input("Your guess was too low.\nGuess again: "))
            count += 1
        elif guess > random_num:
            guess = int(input("Your guess was too high.\nGuess again: "))
            count += 1
        else:
            print("Winner!!")
            does_guess_match = True

    if not does_guess_match:
        print(f"you lost\nthe number was {random_num}")


"""
Extra Challenge: Find Missing Numbers
list = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17,
18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
Write a function called missing_numbers that takes a list of
sequence of numbers and finds the missing numbers in the
sequence. The list above should return:
[4, 8, 10, 13, 16, 29, 30]"""


def missing_numbers(seq_list: list) -> list:
    missing = [num for num in range(
        min(seq_list), max(seq_list) + 1) if num not in seq_list]
    return missing


guess_a_number()
print(missing_numbers([1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17,
                       18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]))
