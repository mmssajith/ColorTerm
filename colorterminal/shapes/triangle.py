"""
Triangle shape for drawing triangles in the terminal.
"""

from .base import Shape
from .. import Colors, colorize


class Triangle(Shape):
    """Draw a triangle in the terminal."""

    def __init__(
        self,
        height,
        filled=True,
        orientation="up",
        color_code=Colors.WHITE,
        fill_char="█",
        border_char="*",
    ):
        """
        Initialize a triangle.

        Args:
            height: Height of the triangle in characters
            filled: If True, fill the triangle; if False, draw only border
            orientation: 'up', 'down', 'left', or 'right'
            color_code: ANSI color code for the triangle
            fill_char: Character to use for filling
            border_char: Character to use for borders (when not filled)
        """
        super().__init__(color_code, fill_char)
        self.height = height
        self.filled = filled
        self.orientation = orientation.lower()
        self.border_char = border_char

    def draw(self):
        """Draw the triangle."""
        if self.orientation == "up":
            self._draw_up()
        elif self.orientation == "down":
            self._draw_down()
        elif self.orientation == "left":
            self._draw_left()
        elif self.orientation == "right":
            self._draw_right()
        else:
            raise ValueError("Orientation must be 'up', 'down', 'left', or 'right'")

    def _draw_up(self):
        """Draw an upward-pointing triangle."""
        for i in range(self.height):
            spaces = " " * (self.height - i - 1)

            if self.filled:
                # Filled triangle
                chars = self.fill_char * (2 * i + 1)
            else:
                # Bordered triangle
                if i == 0:
                    # Top point
                    chars = self.border_char
                elif i == self.height - 1:
                    # Bottom edge
                    chars = self.border_char * (2 * i + 1)
                else:
                    # Sides only
                    chars = self.border_char + " " * (2 * i - 1) + self.border_char

            print(colorize(spaces + chars, self.color_code))

    def _draw_down(self):
        """Draw a downward-pointing triangle."""
        for i in range(self.height):
            spaces = " " * i
            width = 2 * (self.height - i) - 1

            if self.filled:
                # Filled triangle
                chars = self.fill_char * width
            else:
                # Bordered triangle
                if i == 0:
                    # Top edge
                    chars = self.border_char * width
                elif i == self.height - 1:
                    # Bottom point
                    chars = self.border_char
                else:
                    # Sides only
                    chars = self.border_char + " " * (width - 2) + self.border_char

            print(colorize(spaces + chars, self.color_code))

    def _draw_left(self):
        """Draw a left-pointing triangle."""
        for i in range(self.height):
            if i <= self.height // 2:
                # Expanding part
                width = i + 1
            else:
                # Contracting part
                width = self.height - i

            if self.filled:
                chars = self.fill_char * width
            else:
                if width == 1:
                    chars = self.border_char
                else:
                    chars = self.border_char + " " * (width - 2) + self.border_char

            print(colorize(chars, self.color_code))

    def _draw_right(self):
        """Draw a right-pointing triangle."""
        for i in range(self.height):
            if i <= self.height // 2:
                # Expanding part
                width = i + 1
            else:
                # Contracting part
                width = self.height - i

            spaces = " " * (self.height // 2 + 1 - width)

            if self.filled:
                chars = self.fill_char * width
            else:
                if width == 1:
                    chars = self.border_char
                else:
                    chars = self.border_char + " " * (width - 2) + self.border_char

            print(colorize(spaces + chars, self.color_code))
