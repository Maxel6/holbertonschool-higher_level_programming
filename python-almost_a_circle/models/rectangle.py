#!/usr/bin/python3
"""Import bass class from base.py"""
from models.base import Base

"""First rectangle"""


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """A constructor method for the Rectangle class

        Args:
            width (int): the width of the Rectangle
            height (int): the height of the Rectangle
            x (int): the x position of the Recangle
            y (int): the y position of the Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Returns a string representation of the Rectangle object."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return h * w"""
        return self.height * self.width

    def display(self):
        """print the rectangle in # symbol handle x,y"""
        print("\n" * self.y, end="")
        for h in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) is not 0:
            for index, arg in enumerate(args):
                if index is 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg

                elif index is 1:
                    self.width = arg

                elif index is 2:
                    self.height = arg

                elif index is 3:
                    self.x = arg

                elif index is 4:
                    self.y = arg

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value

                elif key == "width":
                    self.width = value

                elif key == "height":
                    self.height = value

                elif key == "x":
                    self.x = value

                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        return self.__dict__