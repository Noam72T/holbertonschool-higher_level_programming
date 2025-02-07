#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

# Define the abstract class Shape


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass

# Circle class inheriting from Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Rectangle class inheriting from Shape


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# The shape_info function using duck typing


def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())


# Testing the classes and the shape_info function
if __name__ == "__main__":
    try:
        circle = Circle(5)
        rectangle = Rectangle(4, 6)
        shape_info(circle)
        shape_info(rectangle)
    except ValueError as e:
        print(f"Error: {e}")