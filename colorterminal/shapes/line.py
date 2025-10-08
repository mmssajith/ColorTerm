"""
Line shape for drawing horizontal and vertical lines in the terminal.
"""

from .. import Colors, colorize
from .base import Shape


class Line(Shape):
    """Draw a horizontal or vertical line in the terminal."""

    def __init__(
        self, length, orientation="horizontal", color_code=Colors.WHITE, fill_char="█"
    ):
        """
        Initialize a line.

        Args:
            length: Length of the line in characters
            orientation: 'horizontal' or 'vertical'
            color_code: ANSI color code for the line
            fill_char: Character to use for drawing
        """
        super().__init__(color_code, fill_char)
        self.length = length
        self.orientation = orientation.lower()

    def draw(self):
        """Draw the line."""
        if self.orientation == "horizontal":
            print(colorize(self.fill_char * self.length, self.color_code))
        elif self.orientation == "vertical":
            for _ in range(self.length):
                print(colorize(self.fill_char, self.color_code))
        else:
            raise ValueError("Orientation must be 'horizontal' or 'vertical'")
