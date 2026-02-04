#!/usr/bin/python3
"""
Module task_01_duck_typing
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    An abstract base class representing a shape
    """
    @abstractmethod
    def area(self):
        """
        An abstract method that should be implemented by subclasses
        to return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        An abstract method that should be implemented by subclasses
        to return the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    A subclass of Shape representing a circle
    """
    def __init__(self, radius):
        """
        Initializes a Circle instance with radius
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculates the perimeter of the circle
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Docstring for Rectangle
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of the given shape
    by duck typing.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
