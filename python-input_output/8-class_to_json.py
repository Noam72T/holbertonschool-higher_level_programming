#!/usr/bin/python3
'''Class to JSON'''


def class_to_json(obj):
    """Return the dictionary description"""
    return obj.__dict__
