#!/usr/bin/python3
"""
Module to demonstrate Mixing Classes
"""


class SwimMixin:
    """
    A Mixin class providing a swimming capability
    """
    def swim(self):
        """
        Print the creature behavior
        """
        print("The creature swims!")


class FlyMixin:
    """
    A Mixin class providing a flying capability
    """
    def fly(self):
        """
        Print the creature behavior
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that inherits from both SwimMixin and FlyMixin
    """
    def roar(self):
        """
        Print dragon behavior
        """
        print("The dragon roars!")


if __name__ == "__main__":

    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
