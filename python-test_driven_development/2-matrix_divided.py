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

    # Validation de `div`
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Validation de `matrix`
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(
        isinstance(nb, (int, float)) for row in matrix for nb in row
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Vérification de la taille des lignes
    row_length = len(matrix[0])  # Longueur de la première ligne
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Calcul de la nouvelle matrice
    return [
        [round(nb / div, 2) for nb in row] for row in matrix
    ]
