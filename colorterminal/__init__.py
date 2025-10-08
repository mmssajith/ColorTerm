"""
ColorTerm - A comprehensive library for colored terminal output using ANSI escape codes.

This library provides easy-to-use classes and functions for:
- Colored and styled text output
- Progress bars (static, animated, spinner, multi)
- Tables (basic, colored, grid layouts)
- Shape drawing (lines, rectangles, circles, triangles, diamonds, boxes)
"""

__version__ = "2.0.1"

__all__ = [
    # Core utilities
    "Colors",
    "Styles",
    "colorize",
    "stylize",
    # Class-based interfaces
    "Printer",
    "StylePrinter",
    "SemanticPrinter",
    # Progress bars
    "ProgressBar",
    "AnimatedProgressBar",
    "MultiProgressBar",
    "SpinnerProgressBar",
    # Tables and Grids
    "Table",
    "ColoredTable",
    "Grid",
    # Shape classes
    "Shape",
    "Line",
    "Rectangle",
    "Circle",
    "Triangle",
    "Diamond",
    "Box",
]


class Colors:
    """ANSI color codes for terminal output."""

    # Reset
    RESET = "\033[0m"

    # Regular colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Bright colors
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    # Background colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    # Bright background colors
    BG_BRIGHT_BLACK = "\033[100m"
    BG_BRIGHT_RED = "\033[101m"
    BG_BRIGHT_GREEN = "\033[102m"
    BG_BRIGHT_YELLOW = "\033[103m"
    BG_BRIGHT_BLUE = "\033[104m"
    BG_BRIGHT_MAGENTA = "\033[105m"
    BG_BRIGHT_CYAN = "\033[106m"
    BG_BRIGHT_WHITE = "\033[107m"


class Styles:
    """ANSI style codes for terminal output."""

    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    STRIKETHROUGH = "\033[9m"


def colorize(text, color_code):
    """Apply a color code to text and reset afterwards."""
    return f"{color_code}{text}{Colors.RESET}"


def stylize(text, *style_codes):
    """Apply one or more style codes to text."""
    styles = "".join(style_codes)
    return f"{styles}{text}{Colors.RESET}"


# Import class-based interfaces
from .printers import Printer, StylePrinter, SemanticPrinter

# Import progress bar classes
from .progress_bars import (
    ProgressBar,
    AnimatedProgressBar,
    MultiProgressBar,
    SpinnerProgressBar,
)

# Import table and grid classes
from .tables import Table, ColoredTable, Grid

# Import shape classes from shapes module
from .shapes import Shape, Line, Rectangle, Circle, Triangle, Diamond, Box
