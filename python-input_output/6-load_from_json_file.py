#!/usr/bin/python3
'''From JSON load the file'''
import json


def load_from_json_file(filename):
    """Open and read the JSON file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
