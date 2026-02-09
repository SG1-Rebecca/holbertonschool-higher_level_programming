#!/usr/bin/python3
"""
Module 4-from_json_string
"""
import json


def from_json_string(my_str):
    """
    Return an object represented by a JSON string

    Args:
        my_str (str): A string representing a JSON object

    Returns:
        The Python object represented by the JSON string
    """
    return json.loads(my_str)
