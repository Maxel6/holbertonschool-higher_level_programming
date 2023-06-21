#!/usr/bin/python3
"""Write file"""


def write_file(filename="", text=""):
    """function that write a text file (UTF8) return the number of \
        characters written"""
    with open(filename, "w") as file:
        return file.write(text)
