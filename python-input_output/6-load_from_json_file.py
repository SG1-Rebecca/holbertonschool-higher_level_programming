#!/usr/bin/python3
"""
Module 6-load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    Create an Object from a JSON file

    Args:
        filename (str): The name of the file to load the object from

    Returns:
        The object loaded from the JSON file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
