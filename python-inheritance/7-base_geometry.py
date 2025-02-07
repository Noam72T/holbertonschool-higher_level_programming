#!/usr/bin/python3
"""Module - 7-base_geometry"""


class BaseGeometry:
    """Base Geometry class"""

    Def area(self):
        """Not Implémented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """functionn fir int validator"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
