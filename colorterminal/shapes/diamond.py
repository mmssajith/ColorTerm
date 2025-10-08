"""
Diamond shape for drawing diamonds in the terminal.
"""

from .. import Colors, colorize
from .base import Shape


class Diamond(Shape):
    """Draw a diamond (rotated square) in the terminal."""

    def __init__(
        self, size, filled=True, color_code=Colors.WHITE, fill_char="█", border_char="*"
    ):
        """
        Initialize a diamond.

        Args:
            size: Size of the diamond (half-height from center to top/bottom)
            filled: If True, fill the diamond; if False, draw only border
            color_code: ANSI color code for the diamond
            fill_char: Character to use for filling
            border_char: Character to use for borders (when not filled)
        """
        super().__init__(color_code, fill_char)
        self.size = size
        self.filled = filled
        self.border_char = border_char

    def draw(self):
        """Draw the diamond."""
        # Upper half (including middle)
        for i in range(self.size):
            spaces = " " * (self.size - i - 1)
            width = 2 * i + 1

            if self.filled:
                chars = self.fill_char * width
            else:
                if width == 1:
                    chars = self.border_char
                else:
                    chars = self.border_char + " " * (width - 2) + self.border_char

            print(colorize(spaces + chars, self.color_code))

        # Lower half
        for i in range(self.size - 2, -1, -1):
            spaces = " " * (self.size - i - 1)
            width = 2 * i + 1

            if self.filled:
                chars = self.fill_char * width
            else:
                if width == 1:
                    chars = self.border_char
                else:
                    chars = self.border_char + " " * (width - 2) + self.border_char

            print(colorize(spaces + chars, self.color_code))
