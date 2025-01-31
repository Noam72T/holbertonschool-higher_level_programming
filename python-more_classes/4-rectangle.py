#!/usr/bin/python3
"""
Module Rectalngle
Defines a class rectangle
"""


class Rectangle:
    """Defines a rectangle."""
    
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance."""
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Retrieve the width."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Retrieve the height."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height
    
    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """Return a string representation of the rectangle with '#' characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])
    
    def __repr__(self):
        """Return a string representation of the rectangle to recreate a new instance."""
        return f"Rectangle({self.__width}, {self.__height})"
