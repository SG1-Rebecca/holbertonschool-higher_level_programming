#!/usr/bin/python3
"""
Module with multiple inheritance: Fish, Bird and FlyingFish classes
"""


class Fish:
    """
    A class representing a Fish
    """
    def swim(self):
        """
        Print the fish action
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print the fish habitat
        """
        print("The fish lives in water")


class Bird:
    """
    A class representing a Bird
    """
    def fly(self):
        """
        Print the bird action
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print the bird habitat
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A FlyingFish class that inherits from both Fish and Bird class
    """
    def fly(self):
        """
        Override the fly method with unique flying fish behavior
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Override the swim method with unique flying fish behavior
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Override the habitat method with unique flying fish habitat
        """
        print("The flying fish lives both in water and the sky!")
