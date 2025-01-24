#!/usr/bin/python3
"""
This module defines a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The divisor, must be a non-zero integer or float.

    Returns:
        list: A new matrix with all elements divided by div, rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   if rows of the matrix are not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(all(isinstance(el, (int, float)) for el in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div and round to 2 decimal places
    return [[round(el / div, 2) for el in row] for row in matrix]
