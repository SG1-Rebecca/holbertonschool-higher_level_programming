#!/usr/bin/python3
"""
Module BaseGeometry
"""


class BaseGeometry:
    """
    A BaseGeometry class
    """
    def area(self):
        """
        Raises an Exception with the message.
        """
        raise Exception("area() is not implemented")

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
