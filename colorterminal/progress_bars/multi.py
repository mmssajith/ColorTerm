"""
MultiProgressBar class for managing multiple progress bars.
"""

from .base import ProgressBar
from .. import Colors


class MultiProgressBar:
    """Manage multiple progress bars simultaneously."""

    def __init__(self):
        """Initialize a multi-progress bar manager."""
        self.bars = {}
        self.labels = []

    def add_bar(
        self,
        label,
        total=100,
        width=30,
        fill_char="█",
        empty_char="░",
        color_code=Colors.GREEN,
        show_percentage=True,
    ):
        """
        Add a progress bar.

        Args:
            label: Unique label for this progress bar
            total: Total value for 100% completion
            width: Width of the progress bar
            fill_char: Character for filled portion
            empty_char: Character for empty portion
            color_code: ANSI color code
            show_percentage: Whether to show percentage
        """
        bar = ProgressBar(
            total,
            width,
            fill_char,
            empty_char,
            color_code,
            show_percentage,
            prefix=f"{label}: ",
        )
        self.bars[label] = bar
        self.labels.append(label)

    def update(self, label, current):
        """
        Update a specific progress bar.

        Args:
            label: Label of the bar to update
            current: Current progress value
        """
        if label in self.bars:
            self.bars[label].update(current)

    def display_all(self):
        """Display all progress bars."""
        print("\n--- Progress Status ---")
        for label in self.labels:
            self.bars[label].display()
        print()

    def get_bar(self, label):
        """
        Get a specific progress bar.

        Args:
            label: Label of the bar to retrieve

        Returns:
            ProgressBar instance or None
        """
        return self.bars.get(label)
