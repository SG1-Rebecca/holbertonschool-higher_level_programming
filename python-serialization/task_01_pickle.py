# task_01_pickle.py
"""
Pickling Custom Classes
"""
import pickle


class CustomObject:
    """
    A custom class that can be serialized and deserialized using pickle.
    """
    def __init__(self, name, age, is_student):
        """
        Initializes the CustomObject with the provided attributes.
        Args:
            name: The name of the object
            age: The age of the object
            is_student: A boolean indicating if the object is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print out the object's attributes with the following format
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object to a file.

        Args:
            filename: The name of the file to save the serialized object.

        Returns:
            None if non-existent or malformed files are encountered,
            otherwise the serialized object is saved to the specified file.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        Args:
            filename: The name of the file to read the object from.

        Returns:
            The deserialized object if successful, otherwise None.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
