#!/usr/bin/python3
"""
Module 11-student
"""


class Student:
    """
    Defines a Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        # If attrs is a list of strings
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            new_dict = {}
            for key in attrs:
                if hasattr(self, key):
                    new_dict[key] = getattr(self, key)
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance

        Args:
            json (dict): A dictionary containing the attributes to replace
        """
        for key, value in json.items():
            setattr(self, key, value)
