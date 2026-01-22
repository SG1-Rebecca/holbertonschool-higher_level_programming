#!/usr/bin/python3
"""
Module 0-add_integer
"""


def add_integer(a, b=98):
    """
    Function that adds two integers.

    Args:
        a: first integer
        b: second integer

    Return:
        int: The sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
