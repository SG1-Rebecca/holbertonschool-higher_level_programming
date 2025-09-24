#!/usr/bin/python3
"""
Module function lookup
"""


def lookup(obj):
    """
    Method that returns the list of available
    attributes and methods of an object

    Args:
        obj: object to look

    Returns:
        list: A list of available attributes and methods of an object
    """
    return dir(obj)
