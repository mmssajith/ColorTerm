"""
StylePrinter class for styled text output.
"""

from .. import Colors, Styles, stylize


class StylePrinter:
    """Class-based interface for printing styled text."""

    @staticmethod
    def bold(text, **kwargs):
        """Print text in bold."""
        print(stylize(text, Styles.BOLD), **kwargs)

    @staticmethod
    def underline(text, **kwargs):
        """Print text underlined."""
        print(stylize(text, Styles.UNDERLINE), **kwargs)

    @staticmethod
    def italic(text, **kwargs):
        """Print text in italic."""
        print(stylize(text, Styles.ITALIC), **kwargs)

    @staticmethod
    def bold_red(text, **kwargs):
        """Print text in bold red."""
        print(stylize(text, Styles.BOLD, Colors.RED), **kwargs)

    @staticmethod
    def bold_green(text, **kwargs):
        """Print text in bold green."""
        print(stylize(text, Styles.BOLD, Colors.GREEN), **kwargs)

    @staticmethod
    def bold_yellow(text, **kwargs):
        """Print text in bold yellow."""
        print(stylize(text, Styles.BOLD, Colors.YELLOW), **kwargs)
