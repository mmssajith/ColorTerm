"""
Shapes module for ColorTerm - Draw shapes in the terminal with colors.
"""

from .base import Shape
from .box import Box
from .circle import Circle
from .diamond import Diamond
from .line import Line
from .rectangle import Rectangle
from .triangle import Triangle

__all__ = ["Shape", "Line", "Rectangle", "Circle", "Triangle", "Diamond", "Box"]
