#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Read a file using with"""
    with open(filename) as fichier:
        contenu = fichier.read()
        print(contenu)
