#!/usr/bin/python3
"""
Module BaseGeometry
"""


class BaseGeometry:
    """
    A BaseGeometry class
    """

    def integer_validator(self, name, value):
        """
        Method that validate a positive integer

        Args:
            name: name of the property to validate
            value: value to check

        Raises:
            TypeError is value not an integer.
            ValueError is value is less or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A Rectangle class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initializes a new rectangle instantiation

        Args:
            width: width of the rectangle
            height: height of the rectangle

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return string representation of Rectangle in format
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
