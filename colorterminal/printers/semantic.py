"""
SemanticPrinter class for semantic/contextual message output.
"""

from .. import Colors, colorize


class SemanticPrinter:
    """Class-based interface for printing semantic/contextual messages."""

    @staticmethod
    def success(text, **kwargs):
        """Print success message in green."""
        print(colorize(f"✓ {text}", Colors.GREEN), **kwargs)

    @staticmethod
    def error(text, **kwargs):
        """Print error message in red."""
        print(colorize(f"✗ {text}", Colors.RED), **kwargs)

    @staticmethod
    def warning(text, **kwargs):
        """Print warning message in yellow."""
        print(colorize(f"⚠ {text}", Colors.YELLOW), **kwargs)

    @staticmethod
    def info(text, **kwargs):
        """Print info message in cyan."""
        print(colorize(f"ℹ {text}", Colors.CYAN), **kwargs)
