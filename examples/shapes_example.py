#!/usr/bin/env python3
"""Example demonstrating shape drawing."""

from colorterminal import Line, Rectangle, Circle, Triangle, Diamond, Box, Colors


def main():
    print("\n=== ColorTerm Shapes Example ===\n")

    # Line
    print("Horizontal Line:")
    Line(length=40, color_code=Colors.CYAN).draw()

    print("\nVertical Line:")
    Line(length=5, orientation="vertical", color_code=Colors.GREEN).draw()

    # Rectangle
    print("\nFilled Rectangle:")
    Rectangle(width=20, height=5, color_code=Colors.BLUE).draw()

    print("\nBordered Rectangle:")
    Rectangle(width=20, height=5, filled=False, color_code=Colors.YELLOW).draw()

    # Circle
    print("\nFilled Circle:")
    Circle(radius=5, color_code=Colors.MAGENTA).draw()

    print("\nBordered Circle:")
    Circle(radius=5, filled=False, color_code=Colors.RED).draw()

    # Triangle
    print("\nUpward Triangle:")
    Triangle(height=5, color_code=Colors.GREEN).draw()

    print("\nDownward Triangle:")
    Triangle(height=5, orientation="down", color_code=Colors.CYAN).draw()

    # Diamond
    print("\nDiamond:")
    Diamond(size=5, color_code=Colors.YELLOW).draw()

    # Box
    print("\nBox (Light Style):")
    Box(width=30, height=3, title="Title", color_code=Colors.BRIGHT_CYAN).draw()

    print("\nBox (Double Style):")
    Box(width=30, height=3, style="double", title="Info", color_code=Colors.BRIGHT_GREEN).draw()

    print()


if __name__ == "__main__":
    main()
