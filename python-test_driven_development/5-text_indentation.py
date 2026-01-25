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
    idx = 0

    while idx < len(text):
        print(text[idx], end="")

        if text[idx] in separators:
            print("\n")
            idx += 1

            while idx < len(text) and text[idx] == " ":
                idx += 1
            continue

        idx += 1
