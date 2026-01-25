#!/usr/bin/python3
"""
Module 5-text_indentation
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text (str): The text to be indented
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    line = ""

    for char in text:
        line += char

        if char in separators:
            print(line.strip())
            print()
            line = ""

    if line.strip():
        print(line.strip())
