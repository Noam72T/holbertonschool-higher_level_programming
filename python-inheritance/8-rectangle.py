#!/usr/bin/python3
"""Defines a module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class, inheritance of BaseGeometry"""

    def __init__(self, width, height):
        """__init__ - initialize the Rectangle class

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
