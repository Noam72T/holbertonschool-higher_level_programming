#!/usr/bin/python3
"""
This module defines a function to print a string with two new lines
after each occurrence of '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input string to be processed and printed.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        char = text[i]
        # Add the current character to the result
        print(char, end="")

        # If the character is one of '.', '?', or ':', print two newlines
        if char in ".?:":
            print("\n")
            # Skip any additional spaces after the punctuation mark
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
