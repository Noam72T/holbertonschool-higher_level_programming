#!/usr/bin/python3
import json

def from_json_string(my_str):
    """Returns an object representing a JSON string"""
    return json.loads(my_str)