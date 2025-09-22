#!/usr/bin/python3
"""
Module function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class

    Args:
        obj: The object to check
        a_class: The specified class to compare

    Returns:
        bool: True if the object is an instance,
        or if the object is an instance of a class inherited from the specified class.
        Otherwise, False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
