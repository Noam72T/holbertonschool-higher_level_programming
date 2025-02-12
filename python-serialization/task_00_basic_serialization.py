#!/usr/bin/python3
'''Basic Serialization'''
import json


def serialize_and_save_to_file(data, filename):
    """Serialize an dictionary python """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load a json file and deserialize it """
    with open(filename, 'r') as file:
    	return json.load(file)
