#!/usr/bin/python3
import json
"""
Module to save an object to a JSON file
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation

    Args:
        my_obj (any): The object to serialize
        filename (any): The name of the file to save using JSON representation
    """
    if isinstance(my_obj, set):
        my_obj = list(my_obj)
    with open(filename, 'w', encoding="UTF8") as f:
        json.dump(my_obj, f)
