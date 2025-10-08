"""
Rectangle shape for drawing rectangles in the terminal.
"""

from .base import Shape
from .. import Colors, colorize


class Rectangle(Shape):
    """Draw a rectangle in the terminal."""

    def __init__(
        self,
        width,
        height,
        filled=True,
        color_code=Colors.WHITE,
        fill_char="█",
        border_char="█",
    ):
        """
        Initialize a rectangle.

        Args:
            width: Width of the rectangle in characters
            height: Height of the rectangle in characters
            filled: If True, fill the rectangle; if False, draw only border
            color_code: ANSI color code for the rectangle
            fill_char: Character to use for filling
            border_char: Character to use for borders (when not filled)
        """
        super().__init__(color_code, fill_char)
        self.width = width
        self.height = height
        self.filled = filled
        self.border_char = border_char

    def draw(self):
        """Draw the rectangle."""
        if self.filled:
            # Draw filled rectangle
            for _ in range(self.height):
                print(colorize(self.fill_char * self.width, self.color_code))
        else:
            # Draw border only
            # Top border
            print(colorize(self.border_char * self.width, self.color_code))

            # Middle rows (if height > 2)
            for _ in range(max(0, self.height - 2)):
                print(
                    colorize(
                        self.border_char + " " * (self.width - 2) + self.border_char,
                        self.color_code,
                    )
                )

            # Bottom border (if height > 1)
            if self.height > 1:
                print(colorize(self.border_char * self.width, self.color_code))
