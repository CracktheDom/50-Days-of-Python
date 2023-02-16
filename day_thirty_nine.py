#!/usr/bin/env python3

import string
import random

"""Create a function called generate_password that generates any
length of password for the user. The password should have a
random mix of upper letters, lower letters, numbers, and
punctuation symbols. The function should ask the user how
strong they want the password to be. The user should pick from -
weak, strong, and very strong. If the user picks weak, the
function should generate a 5-character long password. If the user
picks strong, generate an 8-character password and if they pick
very strong, generate a 12-character password."""


def generate_password():
    source = string.ascii_letters + string.digits + string.punctuation
    password_strength = input(
        "What type of password would you like,\nweak\nstrong\nor very strong: ")
    if password_strength == 'weak':
        random_password = ''.join(random.choices(source, k=5))
    elif password_strength == 'strong':
        random_password = ''.join(random.choices(source, k=8))
    elif password_strength == 'very strong':
        random_password = ''.join(random.choices(source, k=12))

    return random_password


print(generate_password())
