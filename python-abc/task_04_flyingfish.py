#!/usr/bin/python3
"""
Docstring for task_04_flyingfish
"""


class Fish:
    """
    A class representing a Fish
    """
    def swim(self):
        """
        Print swimming action of the fish
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print habitat of the fish
        """
        print("The fish lives in water")


class Bird:
    """
    A class representing a Bird
    """
    def fly(self):
        """
        Print flying action of the bird
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print habitat of the bird
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Docstring for FlyingFish
    """
    def fly(self):
        """
        Override the fly method to indicate flying fish behavior
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Override the swim method to indicate swimming behavior
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Override the habitat method to indicate dual habitat
        """
        print("The flying fish lives both in water and the sky!")
