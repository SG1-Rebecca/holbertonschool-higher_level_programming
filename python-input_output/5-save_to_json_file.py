#!/usr/bin/python3
"""
Module 5-save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation

    Args:
        my_obj: The object to save to the file
        filename (str): The name of the file to save the object to
    """
    with open(filename, "w", encoding="utf-8") as so_file:
        return json.dump(my_obj, so_file)
