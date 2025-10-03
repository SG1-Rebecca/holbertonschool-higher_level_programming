# task_00_basic_serialization.py
"""
Module to serialize and deserialize data using JSON format
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file and save it to a file

    Args:
        data: The Python dictionary to be serialized
        filename: The filename of the output JSON file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load data and deserialize the JSON file to recreate the Python Dictionary.

    Args:
        filename: The name of the JSON file to be read.

    Returns:
        A Python Dictionary with the deserialized JSON data from the file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
