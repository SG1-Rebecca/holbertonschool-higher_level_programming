#!/usr/bin/python3
"""
Module 3-is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a class
    or an instance of a class that inherited from.

    Args:
        obj: The object to check.
        a_class: The class to compare.

    Returns:
        True if obj is an instance of a_class or an instance of
        a class that inherited from a_class, False otherwise.
    """
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    return False
