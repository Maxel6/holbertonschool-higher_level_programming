#!/usr/bin/python3
"""load_from_json_file"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a json file"""
    with open(filename, "w") as file:
        return json.load(file)
