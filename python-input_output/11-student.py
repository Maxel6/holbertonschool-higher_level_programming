#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        else:
            my_dict = {key: self.__dict__[key] for key in attrs
                       if key in self.__dict__}
            return my_dict

    def reload_from_json(self, json):
        for key in json:
            if key in self.__dict__:
                self.__dict__[key] = json[key]
