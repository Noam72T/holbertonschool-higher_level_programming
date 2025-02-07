#!/usr/bin/python

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    It enforces the implementation of the 'area'
    and 'perimeter' methods in any subclass.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        Must be implemented by any subclass of Shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        Must be implemented by any subclass of Shape.
        """
        pass


class Circle(Shape):
    """
    Circle class that inherits from Shape.
    It represents a circle with a specified radius.
    """

    def __init__(self, radius):
        """
        Initializes the circle with a given radius.

        Parameters:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculates the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.
    It represents a rectangle with a specified width and height.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle with given width and height.

        Parameters:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape.

    This function relies on duck typing, meaning
    it calls the 'area' and 'perimeter' methods
    on the passed object without checking its type.

    Parameters:
        shape (Shape): An object that follows the Shape interface
        (i.e., has area and perimeter methods).
    """
    
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
