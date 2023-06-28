#!/usr/bin/python3
"""Import rectangle class from rectangle.py"""
from models.rectangle import Rectangle

""" And now, the Square!"""


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """A constructor method for the Square class
        Args:
        size (int): the size of the Square
        x (int): the x position of the Square
        y (int): the y position of the Square
        id (int): the identity of the new Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the print() and str() representation of a Square."""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """Getter for the size attribute of a Square instance"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute of a Square instance

        Args:
            value (int): Positive integer. Defines the size of a square

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to zero
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
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
                    self.height = arg

                elif index is 2:
                    self.x = arg

                elif index is 3:
                    self.y = arg

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value

                elif key == "size":
                    self.width = value
                    self.height = value

                elif key == "x":
                    self.x = value

                elif key == "y":
                    self.y = value
    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        repr_dict = {}
        for key, value in self.__dict__.items():
            if key == "id":
                repr_dict["id"] = value
            elif key == "_Rectangle__height":
                repr_dict["size"] = value
            elif key == "_Rectangle__x":
                repr_dict["x"] = value
            elif key == "_Rectangle__y":
                repr_dict["y"] = value
        return repr_dict
