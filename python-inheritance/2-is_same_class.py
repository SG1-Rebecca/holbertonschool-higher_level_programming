#!/usr/bin/python3
"""
Module 2-is_same_class
"""


def is_same_class(obj, a_class):
    """
    Function that checks if an object is exactly
    an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare.

    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    return True if type(obj) is a_class else False
