#!/usr/bin/python3
from abc import ABC, abstractmethod
"""Module defining an abstract Animal class and its subclasses """


class Animal(ABC):
    @abstractmethod
    def sound(self):
        """
        Return the sound made by the animal
        """
        pass


class Dog(Animal):
    """
    Subclass representing a Dog that inherits from the Animal class
    """
    def sound(self):
        """
        Return the sound made by a dog
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass representing a Cat that inherits from the Animal class
    """
    def sound(self):
        """
        Return the sound made by a cat
        """
        return "Meow"
