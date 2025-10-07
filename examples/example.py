#!/usr/bin/env python3
"""
Example usage of the ColorTerminal library.
Run this script to see all the different color and style options.
"""

from colorterminal import *


def main():
    print("\n=== ColorTerminal Library Demo ===\n")

    # Basic colors
    print("--- Basic Colors ---")
    print_red("This is red text")
    print_green("This is green text")
    print_yellow("This is yellow text")
    print_blue("This is blue text")
    print_magenta("This is magenta text")
    print_cyan("This is cyan text")
    print_white("This is white text")

    # Bright colors
    print("\n--- Bright Colors ---")
    print_bright_red("This is bright red text")
    print_bright_green("This is bright green text")
    print_bright_yellow("This is bright yellow text")
    print_bright_blue("This is bright blue text")

    # Semantic/contextual messages
    print("\n--- Semantic Messages ---")
    print_success("Operation completed successfully!")
    print_error("Failed to connect to server!")
    print_warning("This action cannot be undone!")
    print_info("Database contains 1,234 records")

    # Text styles
    print("\n--- Text Styles ---")
    print_bold("This is bold text")
    print_underline("This is underlined text")
    print_italic("This is italic text")

    # Combined styles
    print("\n--- Combined Styles ---")
    print_bold_red("This is bold red text")
    print_bold_green("This is bold green text")
    print_bold_yellow("This is bold yellow text")

    # Manual colorization
    print("\n--- Manual Colorization ---")
    print(colorize("Custom colored text", Colors.MAGENTA))
    print(stylize("Custom styled text", Styles.BOLD, Styles.UNDERLINE, Colors.CYAN))

    # Practical examples
    print("\n--- Practical Examples ---")
    print_info("Starting application...")
    print_success("Connected to database")
    print_warning("Cache is nearly full (90%)")
    print_success("Processing complete: 100 items processed")

    print("\n--- Mixed Content ---")
    print(f"Status: {colorize('ONLINE', Colors.GREEN)} | "
          f"Users: {colorize('42', Colors.CYAN)} | "
          f"Errors: {colorize('0', Colors.GREEN)}")

    print()


if __name__ == "__main__":
    main()
