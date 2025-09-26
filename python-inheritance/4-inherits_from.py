#!/usr/bin/python3
"""
Module
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited directly
    or indirectly from the specified class

    Args:
        obj: Object to check
        a_class: The class to compare

    Returns:
        bool: True if the object is an instance of a class that inherits
        from a_class, otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False