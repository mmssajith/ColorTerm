#!/usr/bin/env python3
"""Example demonstrating ASCII art functionality."""

import numpy as np

from colorterminal import Colors, ImageToASCII, SemanticPrinter, TextArt


def main():
    print("\n=== ColorTerm ASCII Art Example ===\n")

    # Text Art Examples
    print("Text Art - Simple Banner:")
    text_art = TextArt()
    text_art.display_banner("HELLO", color_code=Colors.CYAN)

    print("\nText Art - Colored Text:")
    text_art.display("PYTHON", color_code=Colors.GREEN)

    print("\nText Art - Numbers:")
    text_art.display("2024", color_code=Colors.YELLOW)

    # Create a simple gradient image for demonstration
    print("\n\nImage to ASCII - Simple Gradient:")
    try:
        # Create a simple gradient (doesn't require PIL)
        width, height = 60, 30
        gradient = np.zeros((height, width, 3), dtype=np.uint8)

        for y in range(height):
            for x in range(width):
                gradient[y, x] = [
                    int(255 * x / width),  # Red increases left to right
                    int(255 * y / height),  # Green increases top to bottom
                    128,  # Blue constant
                ]

        converter = ImageToASCII(width=80, detailed=False)
        converter.display_from_array(gradient, colored=True)

        print("\n\nImage to ASCII - Circle Pattern:")
        # Create a circular pattern
        size = 50
        circle_img = np.zeros((size, size, 3), dtype=np.uint8)
        center = size // 2

        for y in range(size):
            for x in range(size):
                distance = ((x - center) ** 2 + (y - center) ** 2) ** 0.5
                if distance < size // 2:
                    intensity = int(255 * (1 - distance / (size // 2)))
                    circle_img[y, x] = [intensity, intensity // 2, 255 - intensity]

        converter2 = ImageToASCII(width=60, detailed=True)
        converter2.display_from_array(circle_img, colored=True)

        SemanticPrinter.success("\nASCII art examples completed!")

    except ImportError as e:
        SemanticPrinter.warning(f"NumPy not installed: {e}")
        SemanticPrinter.info("Install NumPy for image conversion: pip install numpy")

    # Alternative: From image file (requires Pillow)
    print("\n\nTo convert image files to ASCII:")
    print("  converter = ImageToASCII(width=100)")
    print("  converter.display_from_file('image.jpg', colored=True)")
    print("\nNote: Requires Pillow - install with: pip install Pillow")

    print()


if __name__ == "__main__":
    main()
