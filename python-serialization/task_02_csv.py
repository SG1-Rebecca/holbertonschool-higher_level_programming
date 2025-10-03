# task_02_csv.py
"""
Module to convert data between CSV and JSON formats.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file.

    Args:
        csv_filename: The CSV file to converts

    Returns:
        True if the conversion was successful, otherwise False.
    """
    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            read_csv = csv.DictReader(csv_file)
            data = list(read_csv)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        return False
