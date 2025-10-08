#!/usr/bin/env python3
"""Basic example demonstrating ColorTerm features."""

from colorterminal import Printer, SemanticPrinter, StylePrinter


def main():
    print("\n=== ColorTerm Basic Example ===\n")

    # Basic colored text
    print("Basic Colors:")
    Printer.red("Red text")
    Printer.green("Green text")
    Printer.blue("Blue text")
    Printer.yellow("Yellow text")

    # Text styles
    print("\nText Styles:")
    StylePrinter.bold("Bold text")
    StylePrinter.underline("Underlined text")
    StylePrinter.italic("Italic text")

    # Semantic messages
    print("\nSemantic Messages:")
    SemanticPrinter.success("Operation completed")
    SemanticPrinter.error("Connection failed")
    SemanticPrinter.warning("Low disk space")
    SemanticPrinter.info("Database updated")

    print()


if __name__ == "__main__":
    main()
