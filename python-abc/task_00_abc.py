#!/usr/bin/python3
"""
Module task_00_abc
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    An abstract base class representing an animal
    """
    @abstractmethod
    def sound(self):
        """
        Returns the sound made by the animal
        """
        pass


class Dog(Animal):
    """
    A subclass of Animal representing a dog
    """
    def sound(self):
        """
        Returns the sound of the dog
        """
        return "bark"


class Cat(Animal):
    """
    A subclass of Animal representing a cat
    """
    def sound(self):
        """
        Returns the sound of the cat
        """
        return "Meow"
