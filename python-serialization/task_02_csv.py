# task_02_csv.py
"""
Converting CSV Data to JSON Format
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV data to a JSON file.

    Args:
        csv_filename: The CSV file to convert

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
