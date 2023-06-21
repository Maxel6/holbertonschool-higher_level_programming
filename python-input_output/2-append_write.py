#!/usr/bin/python3
"""Write file"""


def append_write(filename="", text=""):
    """function that append a text file (UTF8) return the number of \
        characters written"""
    with open(filename, "a") as file:
        return file.write(text)
