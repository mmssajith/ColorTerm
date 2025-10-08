"""
Shapes module for ColorTerm - Draw shapes in the terminal with colors.
"""

from .base import Shape
from .line import Line
from .rectangle import Rectangle
from .circle import Circle
from .triangle import Triangle
from .diamond import Diamond
from .box import Box

__all__ = ["Shape", "Line", "Rectangle", "Circle", "Triangle", "Diamond", "Box"]
