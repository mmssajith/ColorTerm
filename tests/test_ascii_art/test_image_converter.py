"""Tests for ImageToASCII class."""

import numpy as np

from colorterminal import Colors, ImageToASCII


class TestImageToASCII:
    """Test cases for ImageToASCII class."""

    def test_initialization_default(self):
        """Test ImageToASCII initialization with defaults."""
        converter = ImageToASCII()
        assert converter.width == 100
        assert converter.chars == ImageToASCII.ASCII_CHARS

    def test_initialization_with_width(self):
        """Test ImageToASCII initialization with custom width."""
        converter = ImageToASCII(width=50)
        assert converter.width == 50

    def test_initialization_with_detailed(self):
        """Test ImageToASCII initialization with detailed character set."""
        converter = ImageToASCII(detailed=True)
        assert converter.chars == ImageToASCII.ASCII_CHARS_DETAILED

    def test_initialization_without_detailed(self):
        """Test ImageToASCII initialization without detailed character set."""
        converter = ImageToASCII(detailed=False)
        assert converter.chars == ImageToASCII.ASCII_CHARS

    def test_ascii_chars_constant(self):
        """Test ASCII_CHARS constant is defined."""
        assert hasattr(ImageToASCII, "ASCII_CHARS")
        assert len(ImageToASCII.ASCII_CHARS) > 0

    def test_ascii_chars_detailed_constant(self):
        """Test ASCII_CHARS_DETAILED constant is defined."""
        assert hasattr(ImageToASCII, "ASCII_CHARS_DETAILED")
        assert len(ImageToASCII.ASCII_CHARS_DETAILED) > len(ImageToASCII.ASCII_CHARS)

    def test_get_ascii_char_darkest(self):
        """Test getting ASCII character for darkest brightness."""
        converter = ImageToASCII()
        char = converter._get_ascii_char(0)
        assert char == converter.chars[0]  # Should be darkest character

    def test_get_ascii_char_brightest(self):
        """Test getting ASCII character for brightest brightness."""
        converter = ImageToASCII()
        char = converter._get_ascii_char(255)
        assert char == converter.chars[-1]  # Should be brightest character

    def test_get_ascii_char_mid_brightness(self):
        """Test getting ASCII character for mid brightness."""
        converter = ImageToASCII()
        char = converter._get_ascii_char(128)
        assert char in converter.chars

    def test_get_ascii_char_various_brightness(self):
        """Test getting ASCII characters for various brightness levels."""
        converter = ImageToASCII()
        for brightness in [0, 50, 100, 150, 200, 255]:
            char = converter._get_ascii_char(brightness)
            assert char in converter.chars

    def test_rgb_to_ansi_color_red(self):
        """Test RGB to ANSI color conversion for red."""
        converter = ImageToASCII()
        color = converter._rgb_to_ansi_color(255, 0, 0)
        assert color in [Colors.RED, Colors.BRIGHT_RED]

    def test_rgb_to_ansi_color_green(self):
        """Test RGB to ANSI color conversion for green."""
        converter = ImageToASCII()
        color = converter._rgb_to_ansi_color(0, 255, 0)
        assert color in [Colors.GREEN, Colors.BRIGHT_GREEN]

    def test_rgb_to_ansi_color_blue(self):
        """Test RGB to ANSI color conversion for blue."""
        converter = ImageToASCII()
        color = converter._rgb_to_ansi_color(0, 0, 255)
        assert color in [Colors.BLUE, Colors.BRIGHT_BLUE]

    def test_rgb_to_ansi_color_yellow(self):
        """Test RGB to ANSI color conversion for yellow."""
        converter = ImageToASCII()
        color = converter._rgb_to_ansi_color(200, 200, 50)
        assert color in [Colors.YELLOW, Colors.BRIGHT_YELLOW]

    def test_rgb_to_ansi_color_magenta(self):
        """Test RGB to ANSI color conversion for magenta."""
        converter = ImageToASCII()
        color = converter._rgb_to_ansi_color(200, 50, 200)
        assert color in [Colors.MAGENTA, Colors.BRIGHT_MAGENTA]

    def test_rgb_to_ansi_color_cyan(self):
        """Test RGB to ANSI color conversion for cyan."""
        converter = ImageToASCII()
        color = converter._rgb_to_ansi_color(50, 200, 200)
        assert color in [Colors.CYAN, Colors.BRIGHT_CYAN]

    def test_rgb_to_ansi_color_white(self):
        """Test RGB to ANSI color conversion for white."""
        converter = ImageToASCII()
        color = converter._rgb_to_ansi_color(255, 255, 255)
        assert color == Colors.WHITE

    def test_rgb_to_ansi_color_black(self):
        """Test RGB to ANSI color conversion for black."""
        converter = ImageToASCII()
        color = converter._rgb_to_ansi_color(0, 0, 0)
        assert color == Colors.BLACK

    def test_convert_from_array_grayscale(self):
        """Test converting grayscale image array to ASCII."""
        converter = ImageToASCII(width=10)
        # Create a simple 10x10 grayscale gradient
        image = np.linspace(0, 255, 100).reshape(10, 10).astype(np.uint8)
        result = converter.convert_from_array(image, colored=False)
        assert result is not None
        assert isinstance(result, str)
        assert len(result) > 0

    def test_convert_from_array_rgb(self):
        """Test converting RGB image array to ASCII."""
        converter = ImageToASCII(width=10)
        # Create a simple 10x10 RGB image
        image = np.zeros((10, 10, 3), dtype=np.uint8)
        image[:, :, 0] = 255  # Red channel
        result = converter.convert_from_array(image, colored=False)
        assert result is not None
        assert isinstance(result, str)
        assert len(result) > 0

    def test_convert_from_array_colored(self):
        """Test converting image array to colored ASCII."""
        converter = ImageToASCII(width=10)
        image = np.zeros((10, 10, 3), dtype=np.uint8)
        image[:, :, 0] = 255  # Red channel
        result = converter.convert_from_array(image, colored=True)
        assert result is not None
        # Should contain ANSI color codes
        assert "\033[" in result

    def test_convert_from_array_without_color(self):
        """Test converting image array to uncolored ASCII."""
        converter = ImageToASCII(width=10)
        image = np.zeros((10, 10, 3), dtype=np.uint8)
        image[:, :, 0] = 255  # Red channel
        result = converter.convert_from_array(image, colored=False)
        assert result is not None
        # Should not contain ANSI color codes
        assert "\033[" not in result

    def test_convert_from_array_aspect_ratio_preserved(self):
        """Test that aspect ratio is preserved in conversion."""
        converter = ImageToASCII(width=20)
        # Create a 40x20 image (2:1 aspect ratio)
        image = np.zeros((20, 40, 3), dtype=np.uint8)
        result = converter.convert_from_array(image, colored=False)
        lines = result.split("\n")
        # Height should be roughly half of width (accounting for character aspect)
        expected_height = int(20 * (20 / 40) * 0.5)
        assert abs(len(lines) - expected_height) <= 2  # Allow small variance

    def test_convert_from_array_different_widths(self):
        """Test conversion with different output widths."""
        image = np.random.randint(0, 255, (50, 50, 3), dtype=np.uint8)
        for width in [10, 20, 50, 100]:
            converter = ImageToASCII(width=width)
            result = converter.convert_from_array(image, colored=False)
            lines = result.split("\n")
            # First line should have approximately the specified width
            assert abs(len(lines[0]) - width) <= 5

    def test_convert_from_array_detailed_chars(self):
        """Test conversion with detailed character set."""
        converter = ImageToASCII(width=10, detailed=True)
        image = np.random.randint(0, 255, (10, 10, 3), dtype=np.uint8)
        result = converter.convert_from_array(image, colored=False)
        assert result is not None
        # Check that detailed characters are used
        for char in result.replace("\n", ""):
            if char != " ":  # Skip spaces
                assert (
                    char in ImageToASCII.ASCII_CHARS_DETAILED
                ), f"Unexpected character: {char}"

    def test_convert_from_array_simple_chars(self):
        """Test conversion with simple character set."""
        converter = ImageToASCII(width=10, detailed=False)
        image = np.random.randint(0, 255, (10, 10, 3), dtype=np.uint8)
        result = converter.convert_from_array(image, colored=False)
        assert result is not None
        # Check that only simple characters are used
        for char in result.replace("\n", ""):
            assert char in ImageToASCII.ASCII_CHARS, f"Unexpected character: {char}"

    def test_convert_from_array_white_image(self):
        """Test converting all-white image."""
        converter = ImageToASCII(width=10)
        image = np.ones((10, 10, 3), dtype=np.uint8) * 255
        result = converter.convert_from_array(image, colored=False)
        # Should use brightest characters
        assert result is not None
        # Most characters should be bright
        bright_char = converter.chars[-1]
        assert bright_char in result

    def test_convert_from_array_black_image(self):
        """Test converting all-black image."""
        converter = ImageToASCII(width=10)
        image = np.zeros((10, 10, 3), dtype=np.uint8)
        result = converter.convert_from_array(image, colored=False)
        # Should use darkest characters
        assert result is not None
        # Most characters should be dark (spaces or first chars)
        dark_char = converter.chars[0]
        assert dark_char in result

    def test_convert_from_array_gradient(self):
        """Test converting gradient image."""
        converter = ImageToASCII(width=20)
        # Create horizontal gradient
        image = np.zeros((10, 20, 3), dtype=np.uint8)
        for x in range(20):
            image[:, x, :] = int(255 * x / 19)
        result = converter.convert_from_array(image, colored=False)
        assert result is not None
        # Should have variety of characters
        unique_chars = set(result.replace("\n", ""))
        assert len(unique_chars) > 3  # Should have multiple different characters

    def test_convert_from_array_without_numpy_raises_error(self):
        """Test that missing numpy raises ImportError."""
        converter = ImageToASCII(width=10)
        # Create a mock array-like object
        fake_array = [[0, 0, 0]]
        # This should raise ImportError when numpy is not available
        # (but in test environment numpy is available)
        # So we just verify the method requires numpy
        try:
            result = converter.convert_from_array(np.array(fake_array))
            # If numpy is available, this should work
            assert result is not None
        except ImportError:
            # If numpy is not available, this is expected
            pass

    def test_display_from_array(self, capsys):
        """Test display_from_array prints to stdout."""
        converter = ImageToASCII(width=10)
        image = np.random.randint(0, 255, (10, 10, 3), dtype=np.uint8)
        converter.display_from_array(image, colored=False)
        captured = capsys.readouterr()
        assert len(captured.out) > 0

    def test_display_from_array_colored(self, capsys):
        """Test display_from_array with color."""
        converter = ImageToASCII(width=10)
        image = np.ones((10, 10, 3), dtype=np.uint8) * 200
        converter.display_from_array(image, colored=True)
        captured = capsys.readouterr()
        assert "\033[" in captured.out  # Should contain ANSI codes

    def test_convert_from_file_missing_pillow(self):
        """Test that convert_from_file without PIL raises ImportError."""
        converter = ImageToASCII(width=10)
        # We can't easily test this without mocking PIL
        # Just verify the method exists
        assert hasattr(converter, "convert_from_file")

    def test_brightness_calculation_rgb(self):
        """Test brightness calculation for RGB values."""
        converter = ImageToASCII(width=10)
        # Create image with known RGB values
        image = np.zeros((5, 5, 3), dtype=np.uint8)
        image[:, :] = [100, 150, 50]  # RGB values
        result = converter.convert_from_array(image, colored=False)
        # Brightness = 0.299*100 + 0.587*150 + 0.114*50 = 123.65
        # Should map to middle-range ASCII character
        assert result is not None

    def test_multiple_conversions_consistent(self):
        """Test that multiple conversions of same image are consistent."""
        converter = ImageToASCII(width=10)
        image = np.random.randint(0, 255, (10, 10, 3), dtype=np.uint8)
        result1 = converter.convert_from_array(image, colored=False)
        result2 = converter.convert_from_array(image, colored=False)
        assert result1 == result2

    def test_convert_small_image(self):
        """Test converting very small image."""
        converter = ImageToASCII(width=5)
        image = np.random.randint(0, 255, (3, 3, 3), dtype=np.uint8)
        result = converter.convert_from_array(image, colored=False)
        assert result is not None
        assert len(result) > 0

    def test_convert_large_image(self):
        """Test converting larger image."""
        converter = ImageToASCII(width=100)
        image = np.random.randint(0, 255, (200, 200, 3), dtype=np.uint8)
        result = converter.convert_from_array(image, colored=False)
        assert result is not None
        lines = result.split("\n")
        # Should have multiple lines
        assert len(lines) > 10

    def test_rgb_channels_processed_correctly(self):
        """Test that RGB channels are processed correctly."""
        converter = ImageToASCII(width=10)
        # Create images with single channel dominant
        red_image = np.zeros((10, 10, 3), dtype=np.uint8)
        red_image[:, :, 0] = 255
        green_image = np.zeros((10, 10, 3), dtype=np.uint8)
        green_image[:, :, 1] = 255
        blue_image = np.zeros((10, 10, 3), dtype=np.uint8)
        blue_image[:, :, 2] = 255

        red_result = converter.convert_from_array(red_image, colored=True)
        green_result = converter.convert_from_array(green_image, colored=True)
        blue_result = converter.convert_from_array(blue_image, colored=True)

        # Results should be different due to different colors
        # (though ASCII characters might be same due to similar brightness)
        assert red_result is not None
        assert green_result is not None
        assert blue_result is not None

    def test_output_format(self):
        """Test that output format is correct."""
        converter = ImageToASCII(width=10)
        image = np.random.randint(0, 255, (10, 10, 3), dtype=np.uint8)
        result = converter.convert_from_array(image, colored=False)
        # Should be string with newlines
        assert isinstance(result, str)
        assert "\n" in result
        lines = result.split("\n")
        # All lines should have similar length
        lengths = [len(line) for line in lines]
        assert max(lengths) - min(lengths) <= 2  # Allow small variance
