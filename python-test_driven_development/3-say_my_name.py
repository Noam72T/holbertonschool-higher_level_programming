#!/usr/bin/python3

"""
This module contains a function that
prints My name is <first name> <last name>.
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints the name in the format:
    'My name is <first_name> <last_name>'
    Raises TypeError if input is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the name without adding extra space after the last name
    print("My name is {} {}".format(first_name, last_name).rstrip())
