#!/usr/bin/python3
"""
Module Rectalngle
Defines a class rectangle
"""


class Rectangle:
    # Public class attributes
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        # Private instance attributes
        self.__width = 0
        self.__height = 0
        # Increment the number of instances when a new object is created
        Rectangle.number_of_instances += 1
        # Use the setter to initialize width and height
        self.width = width
        self.height = height

    # Getter and setter for width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # Getter and setter for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Public instance method: area
    def area(self):
        return self.__width * self.__height

    # Public instance method: perimeter
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    # String representation of the rectangle
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width] * self.__height)

    # String representation for eval()
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    # Destructor to print message when instance is deleted
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")

    # Static method to compare areas of two rectangles
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    # Class method to create a square
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
