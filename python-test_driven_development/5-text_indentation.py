#!/usr/bin/python3
"""
This module defines a function for printing text with specific formatting.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input text to be formatted and printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize a variable to store the result
    result = ""
    i = 0
    while i < len(text):
        char = text[i]
        result += char

        # Check if the character requires two new lines
        if char in ".:?":
            result += "\n\n"
            # Skip any extra spaces after punctuation
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    # Strip spaces from the beginning and end of each line
    lines = [line.strip() for line in result.splitlines()]
    final_result = "\n".join(lines)

    print(final_result)
