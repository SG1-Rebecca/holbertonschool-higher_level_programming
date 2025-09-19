#!/usr/bin/python3
"""
Square module

This module define a Square class

"""


class Square:
    """
    A class that define a square.

    Attributes:
            _size: The size of the square.
            _position: Tuple of 2 positive integers.

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square instance.

        Args:
            size (int): size of the square. Default is 0.
            position (tuple): Tuple of 2 positive integers. Default is (0, 0)

        Raises:
            TypeError if size is not an integer.
            ValueError if size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter of the size of the square

        Return:
            int: The size of the square
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

    @property
    def position(self):
        """
        Getter of the position of the square.

        Return:
            tuple:

        """
        return self._position

    @position.setter
    def position(self, value):
        """
        Setter of the position of the square.

        Args:
            value: Tuple of 2 positive integers.

        Raises:
            TypeError if value is not a tuple of 2 positive integers.

        """
        horizontal, vertical = value

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(horizontal, int) or not isinstance(vertical, int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if horizontal < 0 and vertical < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self._position = value

    def area(self):
        """
        Calculate the area of the square

        Return:
            The current square area

        """
        return self._size ** 2

    def my_print(self):
        """
        Print the square using '#' with it position

        Return:
            Print '#', otherwise print an empty line if size is 0.

        """
        if self._size == 0:
            print("")
        else:
            for cols in range(self._position[1]):
                print("")

            for row in range(self._size):
                print(" " * self._position[0] + "#" * self._size)
