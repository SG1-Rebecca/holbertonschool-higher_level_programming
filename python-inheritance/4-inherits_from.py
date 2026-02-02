#!/usr/bin/python3
"""
Module 4-inherits_from
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a_class's subclass
    but not an instance of a_class itself.

    Args:
        obj: The object to check.
        a_class: The class to compare.

    Returns:
        True if obj is an instance of a subclass of a_class, False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
