#!/usr/bin/python3
"""
Module 3-say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    Print My name is <first name> <last name>.

    Args:
        first_name: The first name
        last_name: The last name

    Return:
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
