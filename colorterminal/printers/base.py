"""
Base Printer class for colored text output.
"""

from .. import Colors, colorize


class Printer:
    """Class-based interface for printing colored text."""

    @staticmethod
    def black(text, **kwargs):
        """Print text in black."""
        print(colorize(text, Colors.BLACK), **kwargs)

    @staticmethod
    def red(text, **kwargs):
        """Print text in red."""
        print(colorize(text, Colors.RED), **kwargs)

    @staticmethod
    def green(text, **kwargs):
        """Print text in green."""
        print(colorize(text, Colors.GREEN), **kwargs)

    @staticmethod
    def yellow(text, **kwargs):
        """Print text in yellow."""
        print(colorize(text, Colors.YELLOW), **kwargs)

    @staticmethod
    def blue(text, **kwargs):
        """Print text in blue."""
        print(colorize(text, Colors.BLUE), **kwargs)

    @staticmethod
    def magenta(text, **kwargs):
        """Print text in magenta."""
        print(colorize(text, Colors.MAGENTA), **kwargs)

    @staticmethod
    def cyan(text, **kwargs):
        """Print text in cyan."""
        print(colorize(text, Colors.CYAN), **kwargs)

    @staticmethod
    def white(text, **kwargs):
        """Print text in white."""
        print(colorize(text, Colors.WHITE), **kwargs)

    @staticmethod
    def bright_black(text, **kwargs):
        """Print text in bright black (gray)."""
        print(colorize(text, Colors.BRIGHT_BLACK), **kwargs)

    @staticmethod
    def bright_red(text, **kwargs):
        """Print text in bright red."""
        print(colorize(text, Colors.BRIGHT_RED), **kwargs)

    @staticmethod
    def bright_green(text, **kwargs):
        """Print text in bright green."""
        print(colorize(text, Colors.BRIGHT_GREEN), **kwargs)

    @staticmethod
    def bright_yellow(text, **kwargs):
        """Print text in bright yellow."""
        print(colorize(text, Colors.BRIGHT_YELLOW), **kwargs)

    @staticmethod
    def bright_blue(text, **kwargs):
        """Print text in bright blue."""
        print(colorize(text, Colors.BRIGHT_BLUE), **kwargs)

    @staticmethod
    def bright_magenta(text, **kwargs):
        """Print text in bright magenta."""
        print(colorize(text, Colors.BRIGHT_MAGENTA), **kwargs)

    @staticmethod
    def bright_cyan(text, **kwargs):
        """Print text in bright cyan."""
        print(colorize(text, Colors.BRIGHT_CYAN), **kwargs)

    @staticmethod
    def bright_white(text, **kwargs):
        """Print text in bright white."""
        print(colorize(text, Colors.BRIGHT_WHITE), **kwargs)
