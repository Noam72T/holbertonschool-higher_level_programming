#!/usr/bin/python3
"""
This module contains the function `matrix_divided`.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of list of int/float): A list of lists containing integers
            or floats, representing the matrix to divide.
        div (int/float): The divisor, which must be a non-zero number.

    Returns:
        list of list of float: A new matrix with all elements divided by `div`,
            rounded to 2 decimal places.

    Raises:
        TypeError: If `matrix` is not a list of lists of integers or floats,
            if rows of the matrix are not of the same size, or if `div` is
            not a number.
        ZeroDivisionError: If `div` is 0.
    """
    # Validate that `matrix` is a list of lists of integers or floats
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Check for empty matrix or empty sublists
    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Ensure all elements in the matrix are integers or floats
    if not all(all(isinstance(el, (int, float)) for el in row) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Ensure all rows in the matrix are of the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate that `div` is an integer or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and round the results
    return [[round(el / div, 2) for el in row] for row in matrix]
