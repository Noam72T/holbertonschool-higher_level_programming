#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())


if __name__ == "__main__":
    circle = Circle(5)
    print("Circle Info:")
    shape_info(circle)

    print("\nRectangle Info:")
    rectangle = Rectangle(3, 4)
    shape_info(rectangle)