#!/usr/bin/python3
"""
Module 6-base_geometry
"""


class BaseGeometry:
    """
    A class BaseGeometry with a public instance method area
    """
    def area(self):
        """
        Raises an Exception with a message.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value as a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
