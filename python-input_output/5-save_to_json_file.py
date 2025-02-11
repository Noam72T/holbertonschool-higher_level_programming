#!/usr/bin/python3
'''Save Object to a file'''
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
