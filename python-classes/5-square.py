#!/usr/bin/python3
"""Square"""


class Square:
    """init square with error"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size is 0:
            print()
        else:
            for y in range(0, self.__size):
                for x in range(0, self.__size):
                    print("#", end="")
                print()
