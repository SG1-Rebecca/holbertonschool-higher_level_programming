# task_03_xml.py
"""
Serializing and Deserializing with XML
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the XML file to write to.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)

    try:
        with open(filename, "wb") as xml_file:
            tree.write(xml_file, encoding="utf-8", xml_declaration=False)
    except Exception:
        return None


def deserialize_from_xml(filename):
    """
    Deserializes an XML file back into a dictionary.

    Args:
        filename (str): The name of the XML file to read from.

    Returns:
        dict: The deserialized dictionary, or None if an error occurs.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        return {child.tag: child.text for child in root}
    except Exception:
        return None
