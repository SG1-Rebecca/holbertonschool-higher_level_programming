# task_01_pickle.py
"""
Module serialize and deserialize custom Python objects using the pickle module.
"""
import pickle


class CustomObject:
    """
    A Custom Python class
    Attributes:
            name (str): The name of the person
            age (int): The age of the person
            is_student (bool): If or Not the person is a student
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the object’s attributes with the following format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save it to the provided filename.

        Args:
            filename: The name of the file to save the serialized object.

        Returns:
            None if non-existent or malformed files.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (IOError, FileNotFoundError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize the object from the provided filename.

        Args:
            filename: The filename containing the serialized object.

        Returns:
            An instance of the CustomObject from the provided filename.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (IOError, FileNotFoundError, pickle.UnpicklingError):
            return None
