"""
Base Shape class for all terminal shapes.
"""

from .. import Colors


class Shape:
    """Base class for drawing shapes in the terminal."""

    def __init__(self, color_code=Colors.WHITE, fill_char="█"):
        """
        Initialize a shape.

        Args:
            color_code: ANSI color code for the shape
            fill_char: Character to use for drawing the shape
        """
        self.color_code = color_code
        self.fill_char = fill_char

    def draw(self):
        """Draw the shape. To be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement draw()")
