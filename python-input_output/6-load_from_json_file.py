#!/usr/bin/python3
import json
"""
Module to load an object from a JSON file.
"""


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (any): The JSON file to read.

    Returns:
        object: The object represented by the JSON file.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
