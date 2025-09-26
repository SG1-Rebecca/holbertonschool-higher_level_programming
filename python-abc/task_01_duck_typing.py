#!/usr/bin/python3
"""Module defining an abstract  """


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape
        """
        pass


class Circle(Shape):
    """
    Class representing a circle
    """
    def __init__(self, radius):
        """
        Initialize a circle using the radius
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle
        """
        return math.pi * self.radius * self.radius

    def perimeter(self):
        """
        Calculate the perimeter of the circle
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class representing a rectangle
    """
    def __init__(self, width, height):
        """
        Initialize a rectangle using the width and the height
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter using duck typing
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
