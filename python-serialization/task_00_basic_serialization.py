# task_00_basic_serialization.py
"""
Basic Serialization
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file and save it.

    Args:
        data: The Python dictionary to be serialized
        filename: The filename of the output JSON file
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file.

    Args:
        filename: The name of the JSON file to be read.

    Returns:
        A Python dictionary containing the deserialized data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
