#!/usr/bin/env python3
import json

"""
Write a function called save_json. This function takes a
dictionary below as an argument and saves it on a file in JSON
format.
Write another function called read_json that opens the file
that you just saved and reads its content."""

names = {"name": "Carol", "sex": "female", "age": 55}


def save_json(names: dict[str, str | int]):
    """
    Save a dictionary as JSON to a file with proper formatting.

    Args:
        names (dict[str, str|int]): A dictionary containing string keys and
        values that can be strings or integers.

    Returns:
        None

    Saves the input dictionary as a JSON object to a file named
    'saved_file.json' with an indentation level of 3 spaces for better
    readability.
    """
    json_object = json.dumps(names, indent=3)

    with open("./saved_file.json", "w") as json_file_object:
        json_file_object.write(json_object)


def read_json(json_file):
    """
    Read the contents of a JSON file.

    Args:
        json_file (str): The path to the JSON file to be read.

    Returns:
        str: The contents of the JSON file as a string.

    Opens the specified JSON file in read mode and returns its contents as a
    string.
    """
    with open(json_file, "r") as file_object:
        return file_object.read()


save_json(names)
