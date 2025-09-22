#!/usr/bin/python3
"""
Module function is_same_class
"""


def is_same_class(obj, a_class):
    """
    Check if the object is an instance of the specified class

    Args:
        obj: The object to check
        a_class: The specified class to compare

    Return:
        True if the object is an instance of the specified class,
        otherwise False.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
