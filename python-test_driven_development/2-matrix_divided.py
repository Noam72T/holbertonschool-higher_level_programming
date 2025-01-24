#!/usr/bin/python3
"""Module for dividing all elements of a matrix."""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.
    
    Args:
        matrix (list of lists of int/float): Matrix to be divided.
        div (int/float): Number to divide the matrix by.
        
    Returns:
        list of lists of float: New matrix with each element divided.
    
    Raises:
        TypeError: If matrix elements are not lists of integers/floats.
        TypeError: If rows of matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    if not all(
        isinstance(row, list) and len(row) == row_len and
        all(isinstance(num, (int, float)) for num in row)
        for row in matrix
    ):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
