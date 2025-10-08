#!/usr/bin/env python3
"""Example demonstrating progress bars."""

import time

from colorterminal import (
    AnimatedProgressBar,
    Colors,
    MultiProgressBar,
    ProgressBar,
    SemanticPrinter,
    SpinnerProgressBar,
)


def main():
    print("\n=== ColorTerm Progress Bars Example ===\n")

    # Static progress bar
    print("Static Progress Bar:")
    bar = ProgressBar(total=100, color_code=Colors.GREEN)
    for i in [0, 25, 50, 75, 100]:
        bar.update(i)
    print()

    # Animated progress bar
    print("Animated Progress Bar:")
    bar = AnimatedProgressBar(total=100, color_code=Colors.BLUE)
    bar.simulate(duration=2, steps=40)

    # Spinner progress bar
    print("Spinner Progress Bar:")
    bar = SpinnerProgressBar(total=100, spinner_style="dots", color_code=Colors.CYAN)
    for i in range(0, 101, 10):
        bar.update(i)
        time.sleep(0.1)
    print()

    # Multiple progress bars
    print("Multiple Progress Bars:")
    multi = MultiProgressBar()
    multi.add_bar("Download", total=100, color_code=Colors.GREEN)
    multi.add_bar("Upload", total=100, color_code=Colors.BLUE)
    multi.add_bar("Processing", total=100, color_code=Colors.YELLOW)

    multi.update("Download", 100)
    multi.update("Upload", 65)
    multi.update("Processing", 40)
    multi.display_all()

    SemanticPrinter.success("All progress bars completed!")
    print()


if __name__ == "__main__":
    main()
