#!/usr/bin/python3
"""
Rectangle module

This module define a Rectangle class.
"""


class Rectangle:
    """
    A class that defines a rectangle.

    Attributes:
            _width:
            _height:
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance

        Args:
            width: The width of the rectangle. Default is 0.
            height: The height of the rectangle. Default is 0.
        """
        self._width = width
        self._height = height
