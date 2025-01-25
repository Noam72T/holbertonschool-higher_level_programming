#!/usr/bin/python3
"""
This module defines a function to print a string with two new lines
after each occurrence of '.', '?', and ':'.
"""


def text_indentation(text):
    """
    This function takes a string as input and prints it, replacing punctuation marks 
    ".", "?", and ":" with a new line after each of them.

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        # Print characters one by one
        print(text[i], end="")
        
        # Check if current character is one of the specified punctuation marks
        if text[i] in ".?:":
            print("\n")  # Print two new lines after punctuation
            i += 1  # Skip any following spaces
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            i += 1
