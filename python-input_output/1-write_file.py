#!/usr/bin/python3
"""
Module 1-write_file
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file and return the number of characters written

    Args:
        filename (str): The name of the file to write to
        text (str): The text to write to the file

    Returns:
        int: The number of characters written to the file
    """
    if filename:
        with open(filename, "w", encoding="utf-8") as write_file:
            return write_file.write(text)
