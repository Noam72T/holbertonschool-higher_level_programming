#!/usr/bin/python3
"""
This module provides a function to format text with specific indentation rules.
"""


def text_indentation(text):
    """
    Indente un texte en fonction des caractères de ponctuation suivants : .,
    ?, et :. Si le texte n'est pas une chaîne de caractères, une exception
    TypeError est levée.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 1

    for letter in text:
        if flag == 1:
            if letter == ' ':
                continue
            else:

                flag = 0

        print(letter, end="")

        if letter in ".?:":
            print("\n")
            flag = 1
