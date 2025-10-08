"""
Circle shape for drawing circles in the terminal.
"""

from .. import Colors, colorize
from .base import Shape


class Circle(Shape):
    """Draw a circle in the terminal using ASCII art."""

    def __init__(
        self,
        radius,
        filled=True,
        color_code=Colors.WHITE,
        fill_char="█",
        border_char="*",
    ):
        """
        Initialize a circle.

        Args:
            radius: Radius of the circle in characters
            filled: If True, fill the circle; if False, draw only border
            color_code: ANSI color code for the circle
            fill_char: Character to use for filling
            border_char: Character to use for borders (when not filled)
        """
        super().__init__(color_code, fill_char)
        self.radius = radius
        self.filled = filled
        self.border_char = border_char

    def draw(self):
        """Draw the circle using the midpoint circle algorithm."""
        # Draw circle using distance formula
        for y in range(-self.radius, self.radius + 1):
            line = ""
            for x in range(-self.radius * 2, self.radius * 2 + 1):
                # Adjust x coordinate for aspect ratio (characters are taller than wide)
                distance = ((x / 2) ** 2 + y**2) ** 0.5

                if self.filled:
                    # Fill everything inside the circle
                    if distance <= self.radius:
                        line += self.fill_char
                    else:
                        line += " "
                else:
                    # Draw only the border
                    if abs(distance - self.radius) < 0.5:
                        line += self.border_char
                    else:
                        line += " "

            # Only print non-empty lines
            if line.strip():
                print(colorize(line, self.color_code))
