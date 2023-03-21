#!/usr/bin/python3
import json

"""
Write a function called save_json. This function takes a
dictionary below as an argument and saves it on a file in JSON
format.
Write another function called read_json that opens the file
that you just saved and reads its content."""

names = {'name': 'Carol', 'sex': 'female', 'age': 55}


def save_json(names: dict):
    json_object = json.dumps(names, indent=3)

    with open("./saved_file.json", "w") as jf:
        jf.write(json_object)


def read_json(json_file):
    with open(json_file, "r") as file_object:
        file_object.read()


save_json(names)
