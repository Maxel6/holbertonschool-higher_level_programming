#!/usr/bin/python3
"""To JSON string"""
import json


def save_to_json_file(my_obj, filename):
    """returns the JSON representation of an object"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
