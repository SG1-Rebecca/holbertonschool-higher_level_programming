#!/usr/bin/python3
"""
Module task_05_dragon
"""


class SwimMixin:
    """
    A Mixin class that provides swimming ability to a creature
    """
    def swim(self):
        """
        Print swimming action of the creature
        """
        print("The creature swims!")


class FlyMixin:
    """
    A Mixin class that provides flying ability to a creature
    """
    def fly(self):
        """
        Print flying action of the creature
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that inherits swimming and flying abilities from Mixins
    """
    def roar(self):
        """
        Print roaring action of the dragon
        """
        print("The dragon roars!")


if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
