#!/usr/bin/python3
"""
Module 8-class_to_json
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj: The object to be converted to a dictionary

    Returns:
        A dictionary representation of the object
    """
    return obj.__dict__
