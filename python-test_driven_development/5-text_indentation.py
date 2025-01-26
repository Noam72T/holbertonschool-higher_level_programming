#!/usr/bin/python3
"""
This module provides a function to format text with specific indentation rules.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?', and ':'.

    Args:
        text (str): The input text to be formatted.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None: Prints the formatted text.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            # Skip spaces after punctuation
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    # Print the formatted result, removing trailing spaces in lines
    print("\n".join(line.strip() for line in result.split("\n")))
