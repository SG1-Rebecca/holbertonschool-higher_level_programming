#!/usr/bin/python3
"""
Module 5-text_indentation
"""


def text_indentation(text):
    """
    Docstring for text_indentation
    
    text: Description
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    spec_char = ['.', '?', ':']

    for char in text:
        if char in spec_char:
            print(char, end="")
            print("\n")
        else:
            print(char, end="")
