#!/usr/bin/python3
"""
Module 6-square
"""


class Square:
    """
    A class that defines a square.

    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.Default is 0.
            position (tuple): The position of the square. Default is (0, 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): The new size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Getter for position

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position

        Args:
            value (tuple): The new position of the square.
        """
        horizontal, vertical = value

        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(horizontal, int)
            or not isinstance(vertical, int)
            or horizontal < 0 or vertical < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
