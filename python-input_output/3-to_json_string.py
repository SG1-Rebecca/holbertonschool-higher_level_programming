#!/usr/bin/python3
import json
"""
Module to convert a Python object to a JSON string.
"""


def to_json_string(my_obj):
    """
    Convert Python object to JSON string.

    Args:
        my_obj: The Python object to convert.

    Return:
        string: The JSON representation of an object.
    """
    s = json.dumps(my_obj)
    return s
