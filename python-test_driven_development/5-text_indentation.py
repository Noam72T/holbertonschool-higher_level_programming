#!/usr/bin/python3

"""
This module contains a function that indents text according to specific rules.
"""

def text_indentation(text):
    """
    Function that prints a text with two new lines
    after each of these characters:
    `.`, `?`, `:`.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        # Remove extra spaces before punctuation marks
        if text[i] in '.?:':
            # Print punctuation followed by two new lines
            print(text[i], end="\n\n")
            i += 1
            # Skip all spaces after the punctuation mark
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            # Print the current character if it's not punctuation
            print(text[i], end="")
            i += 1
