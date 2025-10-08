"""
Box shape using Unicode box-drawing characters for professional-looking boxes.
"""

from .. import Colors, colorize
from .base import Shape


class Box(Shape):
    """Draw a box using Unicode box-drawing characters."""

    # Box drawing character sets
    STYLES = {
        "light": {"tl": "┌", "tr": "┐", "bl": "└", "br": "┘", "h": "─", "v": "│"},
        "heavy": {"tl": "┏", "tr": "┓", "bl": "┗", "br": "┛", "h": "━", "v": "┃"},
        "double": {"tl": "╔", "tr": "╗", "bl": "╚", "br": "╝", "h": "═", "v": "║"},
        "rounded": {"tl": "╭", "tr": "╮", "bl": "╰", "br": "╯", "h": "─", "v": "│"},
        "dashed": {"tl": "┌", "tr": "┐", "bl": "└", "br": "┘", "h": "╌", "v": "╎"},
    }

    def __init__(
        self, width, height, style="light", color_code=Colors.WHITE, title=None
    ):
        """
        Initialize a box with box-drawing characters.

        Args:
            width: Width of the box (interior width)
            height: Height of the box (interior height)
            style: Box style - 'light', 'heavy', 'double', 'rounded', or 'dashed'
            color_code: ANSI color code for the box
            title: Optional title to display in the top border
        """
        super().__init__(color_code, fill_char="")
        self.width = width
        self.height = height
        self.style = style.lower()
        self.title = title

        if self.style not in self.STYLES:
            raise ValueError(f"Style must be one of: {', '.join(self.STYLES.keys())}")

        self.chars = self.STYLES[self.style]

    def draw(self):
        """Draw the box."""
        # Top border with optional title
        if self.title:
            title_text = f" {self.title} "
            remaining = self.width - len(title_text)
            left_border = self.chars["h"] * (remaining // 2)
            right_border = self.chars["h"] * (remaining - len(left_border))
            top_line = f"{self.chars['tl']}{left_border}{title_text}{right_border}{self.chars['tr']}"
        else:
            top_line = (
                f"{self.chars['tl']}{self.chars['h'] * self.width}{self.chars['tr']}"
            )

        print(colorize(top_line, self.color_code))

        # Middle rows
        for _ in range(self.height):
            middle_line = f"{self.chars['v']}{' ' * self.width}{self.chars['v']}"
            print(colorize(middle_line, self.color_code))

        # Bottom border
        bottom_line = (
            f"{self.chars['bl']}{self.chars['h'] * self.width}{self.chars['br']}"
        )
        print(colorize(bottom_line, self.color_code))
