"""
SpinnerProgressBar class for progress bars with spinner animations.
"""

import sys
from .base import ProgressBar


class SpinnerProgressBar(ProgressBar):
    """Progress bar with a spinner animation."""

    SPINNERS = {
        "dots": ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"],
        "line": ["|", "/", "-", "\\"],
        "arrow": ["←", "↖", "↑", "↗", "→", "↘", "↓", "↙"],
        "dots2": ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"],
        "box": ["◰", "◳", "◲", "◱"],
        "circle": ["◴", "◷", "◶", "◵"],
        "bounce": ["⠁", "⠂", "⠄", "⡀", "⢀", "⠠", "⠐", "⠈"],
    }

    def __init__(
        self,
        total=100,
        width=40,
        fill_char="█",
        empty_char="░",
        color_code=None,
        spinner_style="dots",
        show_percentage=True,
        prefix="",
        suffix="",
    ):
        """
        Initialize a spinner progress bar.

        Args:
            total: Total value for 100% completion
            width: Width of the progress bar
            fill_char: Character for filled portion
            empty_char: Character for empty portion
            color_code: ANSI color code
            spinner_style: Spinner animation style ('dots', 'line', 'arrow', etc.)
            show_percentage: Whether to show percentage
            prefix: Text before the bar
            suffix: Text after the bar
        """
        # Import Colors here to avoid circular import
        from .. import Colors

        if color_code is None:
            color_code = Colors.GREEN

        super().__init__(
            total,
            width,
            fill_char,
            empty_char,
            color_code,
            show_percentage,
            prefix,
            suffix,
        )
        self.spinner_style = spinner_style
        self.spinner_index = 0
        self.spinner = self.SPINNERS.get(spinner_style, self.SPINNERS["dots"])

    def display(self):
        """Display the progress bar with spinner."""
        from .. import colorize

        percent = (self.current / self.total) * 100 if self.total > 0 else 0
        filled_width = (
            int(self.width * self.current / self.total) if self.total > 0 else 0
        )
        empty_width = self.width - filled_width

        filled = colorize(self.fill_char * filled_width, self.color_code)
        empty = self.empty_char * empty_width

        bar = f"{filled}{empty}"

        # Get current spinner character
        spinner_char = self.spinner[self.spinner_index % len(self.spinner)]
        self.spinner_index += 1

        if self.show_percentage:
            percentage = f" {percent:6.2f}%"
        else:
            percentage = ""

        output = f"\r{spinner_char} {self.prefix}{bar}{percentage}{self.suffix}"

        sys.stdout.write(output)
        sys.stdout.flush()

        if self.current >= self.total:
            print()  # New line when complete
