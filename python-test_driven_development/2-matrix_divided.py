#!/usr/bin/python3
"""
Ce module contient la fonction matrix_divided.
"""


def matrix_divided(matrix, div):
    """
    Divise tous les éléments d'une matrice par un nombre
    et arrondit à 2 décimales.

    Arguments :
        matrix : Liste de listes contenant des entiers ou des flottants.
        div : Nombre utilisé pour diviser les éléments de la matrice
              (entier ou flottant).

    Retourne :
        Nouvelle matrice avec les éléments divisés par div,
        arrondis à 2 décimales.

    Exceptions :
        TypeError : Si matrix n'est pas une liste de listes de nombres,
                    si les lignes n'ont pas la même taille,
                    ou si div n'est pas un nombre.
        ZeroDivisionError : Si div est égal à 0.
    """
    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check for empty matrix or empty sublists
    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all elements in the matrix are integers or floats
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
