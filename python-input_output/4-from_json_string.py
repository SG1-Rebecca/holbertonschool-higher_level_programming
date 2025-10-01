#!/usr/bin/python3
"""
Module to convert a JSON string to Python object
"""
import json


def from_json_string(my_str):
    """
    Convert a JSON string to Python object

    Args:
        my_str:
            The JSON string to convert

    Returns:
        object: The object represented by the JSON string
    """
    o = json.loads(my_str)
    return o
