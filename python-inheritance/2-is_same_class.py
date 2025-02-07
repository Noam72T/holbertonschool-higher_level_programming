#!/usr/bin/python3
"""Defines a class-checking function."""



def is_same_class(obj, a_class):
    """Checks if an object is an instance of a specific class."""
    """Returns True if obj is exactly an instance of a_class, else False."""
    if type(obj) == a_class:
        return True
    return False
