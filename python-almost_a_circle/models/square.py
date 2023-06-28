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
