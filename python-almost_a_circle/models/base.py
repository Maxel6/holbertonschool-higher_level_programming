#!/usr/bin/python3
"""Base class"""


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__nb_object += 1
            self.id = id
