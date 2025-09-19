#!/usr/bin/python3
"""
Square module

This module define a Square class

"""


class Square:
    """
    A class that define a square.

    Attributes:
            __size: The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new square instance.

        Args:
            size (int): size of the square. Default is 0.

        Raises:
            TypeError if size is not an integer.
            ValueError if size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

    @property
    def size(self):
        """
        Getter of the size of the square

        Return:
            The size of the square

        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Setter of the size of the square

        Args:
            value (int):

        Raises:
            TypeError if value is not an integer.
            ValueError if value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        Calculates the area of the square

        Return:
            The current square area
        """
        return self._size ** 2
