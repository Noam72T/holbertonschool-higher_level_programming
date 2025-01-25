#!/usr/bin/python3

"""
This module contains a function that indents text according to specific rules.
"""


def text_indentation(text):
    """
    Function that prints a text with two new lines after each
    of these characters:
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in '.?:':
            print(text[i], end="\n\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(text[i], end="")
            i += 1
