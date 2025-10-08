"""
AnimatedProgressBar class for animated progress bars.
"""

import sys
import time

from .base import ProgressBar


class AnimatedProgressBar(ProgressBar):
    """Animated progress bar that updates in place."""

    def __init__(
        self,
        total=100,
        width=40,
        fill_char="█",
        empty_char="░",
        color_code=None,
        show_percentage=True,
        prefix="",
        suffix="",
    ):
        """
        Initialize an animated progress bar.

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
        self.started = False

    def display(self):
        """Display the progress bar at current progress (overwrites previous line)."""
        from .. import colorize

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

        output = f"\r{self.prefix}{bar}{percentage}{self.suffix}"

        sys.stdout.write(output)
        sys.stdout.flush()

        if self.current >= self.total:
            print()  # New line when complete

    def animate_to(self, target, steps=20, delay=0.05):
        """
        Animate the progress bar to a target value.

        Args:
            target: Target progress value
            steps: Number of animation steps
            delay: Delay between steps in seconds
        """
        target = min(target, self.total)
        start = self.current
        increment = (target - start) / steps

        for _ in range(steps):
            self.current = min(self.current + increment, target)
            self.display()
            time.sleep(delay)

        self.current = target
        self.display()

    def simulate(self, duration=2.0, steps=50):
        """
        Simulate a complete progress animation.

        Args:
            duration: Total duration of the animation in seconds
            steps: Number of steps in the animation
        """
        delay = duration / steps
        increment = self.total / steps

        for _ in range(steps):
            self.increment(increment)
            time.sleep(delay)

        self.complete()
