#!/usr/bin/python3
'''Convert to XML'''
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize this object"""
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception as e:
        print(f"Serialization Error: {e}")
        return False


def deserialize_from_xml(filename):
    """Deserialize this object"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        return {child.tag: child.text for child in root}
    except FileNotFoundError:
        print("Error: XML file not found.")
        return None
    except Exception as e:
        print(f"Deserialization Error: {e}")
        return None
