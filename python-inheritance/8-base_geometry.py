#!/usr/bin/python3
"""Rectangle"""


class Rectangle():
    """Rectangle"""

    def __init__(self, width, height):
        Rectangle.integer_validator(self, "width", width)
        Rectangle.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
