"""
Base ProgressBar class for static progress bars.
"""

from .. import Colors, colorize


class ProgressBar:
    """Static progress bar with percentage display."""

    def __init__(
        self,
        total=100,
        width=40,
        fill_char="█",
        empty_char="░",
        color_code=Colors.GREEN,
        show_percentage=True,
        prefix="",
        suffix="",
    ):
        """
        Initialize a progress bar.

        Args:
            total: Total value for 100% completion
            width: Width of the progress bar in characters
            fill_char: Character for filled portion
            empty_char: Character for empty portion
            color_code: ANSI color code for the filled portion
            show_percentage: Whether to show percentage
            prefix: Text to show before the bar
            suffix: Text to show after the bar
        """
        self.total = total
        self.width = width
        self.fill_char = fill_char
        self.empty_char = empty_char
        self.color_code = color_code
        self.show_percentage = show_percentage
        self.prefix = prefix
        self.suffix = suffix
        self.current = 0

    def update(self, current):
        """
        Update and display the progress bar.

        Args:
            current: Current progress value
        """
        self.current = min(current, self.total)
        self.display()

    def display(self):
        """Display the progress bar at current progress."""
        percent = (self.current / self.total) * 100 if self.total > 0 else 0
        filled_width = (
            int(self.width * self.current / self.total) if self.total > 0 else 0
        )
        empty_width = self.width - filled_width

        filled = colorize(self.fill_char * filled_width, self.color_code)
        empty = self.empty_char * empty_width

        bar = f"{filled}{empty}"

        if self.show_percentage:
            percentage = f" {percent:6.2f}%"
        else:
            percentage = ""

        output = f"{self.prefix}{bar}{percentage}{self.suffix}"
        print(output)

    def increment(self, amount=1):
        """
        Increment the progress by a given amount.

        Args:
            amount: Amount to increment
        """
        self.update(self.current + amount)

    def complete(self):
        """Mark the progress as complete."""
        self.update(self.total)
