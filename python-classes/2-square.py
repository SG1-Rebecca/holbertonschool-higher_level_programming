#!/usr/bin/python3
"""
Square module

This module define a Square class

"""


class Square:
    """
    A class that defines a square.

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

        self.__size = size
