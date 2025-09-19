#!/usr/bin/python3
"""
Rectangle module

This module define a Rectangle class.
"""


class Rectangle:
    """
    A class that defines a rectangle.

    Attributes:
            _width: The width of the rectangle.
            _height: The height of the rectangle.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance

        Args:
            width: The width of the rectangle. Default is 0.
            height: The height of the rectangle. Default is 0.
        """
        self._width = width
        self._height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter of the width of the rectangle.

        Return:
            The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Setter of the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError if width is not an integer.
            ValueError if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Getter of the height of the rectangle.

        Return:
            The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Setter of the height of the rectangle.

        Args:
            value (int): The new height value

        Raises:
            TypeError if height is not an integer.
            ValueError if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Return:
            The rectangle area
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Return:
            The perimeter of the rectangle.
            If width or height is equal to 0, perimeter is 0
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        """
        String representation of the rectangle using the character '#'.

        Return:
            str: Empty string if width or height is 0.
            str: Rectangle using the character '#'.

        """
        if self._width == 0 or self._height == 0:
            return ""

        rectangle_rows = []
        for row in range(self._height):
            rectangle_rows.append("#" * self._width)
        return "\n".join(rectangle_rows)

    def __repr__(self):
        """
        Official string representation to recreate the rectangle.

        Return:
            str: String representation of the rectangle.
        """
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """
        Print message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
