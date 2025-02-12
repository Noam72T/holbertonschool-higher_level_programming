#!/usr/bin/python3
'''Add item to JSON file'''
from os import path
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""Save to JSON file"""
filename = 'add_item.json'

if path.exists(filename):
    obj_json_file = load_from_json_file(filename)
else:
    obj_json_file = []

obj_json_file.extend(argv[1:])

save_to_json_file(obj_json_file, filename)
