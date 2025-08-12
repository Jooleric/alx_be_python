# polymorphism_demo.py
import math
from typing import Protocol

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    """Rectangle with length and width."""
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        """Area of a rectangle: length * width"""
        return self.length * self.width


class Circle(Shape):
    """Circle with a radius."""
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """Area of a circle: pi * radius^2"""
        return math.pi * (self.radius ** 2)
