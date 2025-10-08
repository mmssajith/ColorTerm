"""Integration tests for ASCII art module."""

import numpy as np

from colorterminal import Colors, ImageToASCII, TextArt


class TestASCIIArtIntegration:
    """Integration tests for ASCII art functionality."""

    def test_text_art_and_image_converter_together(self):
        """Test using both TextArt and ImageToASCII in same session."""
        text_art = TextArt()
        image_converter = ImageToASCII(width=20)

        # Generate text art
        text_result = text_art.generate("TEST")
        assert text_result is not None

        # Convert image
        image = np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)
        image_result = image_converter.convert_from_array(image, colored=False)
        assert image_result is not None

        # Both should work independently
        assert len(text_result) > 0
        assert len(image_result) > 0

    def test_text_art_with_all_colors(self):
        """Test TextArt with all available colors."""
        art = TextArt()
        colors = [
            Colors.RED,
            Colors.GREEN,
            Colors.BLUE,
            Colors.YELLOW,
            Colors.MAGENTA,
            Colors.CYAN,
            Colors.WHITE,
            Colors.BLACK,
            Colors.BRIGHT_RED,
            Colors.BRIGHT_GREEN,
            Colors.BRIGHT_BLUE,
            Colors.BRIGHT_YELLOW,
            Colors.BRIGHT_MAGENTA,
            Colors.BRIGHT_CYAN,
        ]

        for color in colors:
            result = art.generate("A", color_code=color)
            assert color in result
            assert Colors.RESET in result

    def test_image_converter_with_all_color_ranges(self):
        """Test ImageToASCII with various color ranges."""
        converter = ImageToASCII(width=10)

        # Test with different color patterns
        # Pure red
        red_image = np.zeros((10, 10, 3), dtype=np.uint8)
        red_image[:, :, 0] = 255
        red_result = converter.convert_from_array(red_image, colored=True)
        assert red_result is not None
        assert "\033[" in red_result

        # Pure green
        green_image = np.zeros((10, 10, 3), dtype=np.uint8)
        green_image[:, :, 1] = 255
        green_result = converter.convert_from_array(green_image, colored=True)
        assert green_result is not None

        # Pure blue
        blue_image = np.zeros((10, 10, 3), dtype=np.uint8)
        blue_image[:, :, 2] = 255
        blue_result = converter.convert_from_array(blue_image, colored=True)
        assert blue_result is not None

    def test_text_art_banner_full_workflow(self):
        """Test complete text art banner workflow."""
        art = TextArt()

        # Generate banner with different border characters
        banner1 = art.generate_banner("HELLO", border_char="=")
        banner2 = art.generate_banner("WORLD", border_char="-")
        banner3 = art.generate_banner("TEST", border_char="*")

        assert "=" in banner1
        assert "-" in banner2
        assert "*" in banner3

        # All should have proper structure
        for banner in [banner1, banner2, banner3]:
            lines = banner.split("\n")
            assert len(lines) > 5  # Border + text lines

    def test_image_converter_brightness_range(self):
        """Test ImageToASCII with full brightness range."""
        converter = ImageToASCII(width=20, detailed=False)

        # Create gradient from black to white
        gradient = np.zeros((10, 20, 3), dtype=np.uint8)
        for x in range(20):
            brightness = int(255 * x / 19)
            gradient[:, x, :] = brightness

        result = converter.convert_from_array(gradient, colored=False)
        assert result is not None

        # Should use variety of ASCII characters
        unique_chars = set(result.replace("\n", ""))
        # Should have at least half the character set represented
        assert len(unique_chars) >= len(converter.chars) // 2

    def test_text_art_all_supported_characters(self):
        """Test TextArt with all supported characters."""
        art = TextArt()

        # Test all letters
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letter_result = art.generate(letters)
        assert letter_result is not None
        assert len(letter_result.split("\n")) == 5

        # Test all numbers
        numbers = "0123456789"
        number_result = art.generate(numbers)
        assert number_result is not None
        assert len(number_result.split("\n")) == 5

        # Test special characters
        special = "! ? . ,"
        special_result = art.generate(special)
        assert special_result is not None
        assert len(special_result.split("\n")) == 5

    def test_image_converter_different_image_sizes(self):
        """Test ImageToASCII with various image sizes."""
        converter = ImageToASCII(width=30)

        sizes = [(10, 10), (20, 40), (50, 25), (100, 100)]

        for height, width in sizes:
            image = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
            result = converter.convert_from_array(image, colored=False)
            assert result is not None
            lines = result.split("\n")
            # Should have some lines
            assert len(lines) > 0

    def test_text_art_display_methods(self, capsys):
        """Test all TextArt display methods."""
        art = TextArt()

        # Test display
        art.display("TEST")
        captured = capsys.readouterr()
        assert len(captured.out) > 0

        # Test display_banner
        art.display_banner("TEST")
        captured = capsys.readouterr()
        assert len(captured.out) > 0
        assert "=" in captured.out

    def test_image_converter_display_methods(self, capsys):
        """Test all ImageToASCII display methods."""
        converter = ImageToASCII(width=10)
        image = np.random.randint(0, 255, (10, 10, 3), dtype=np.uint8)

        # Test display_from_array
        converter.display_from_array(image, colored=False)
        captured = capsys.readouterr()
        assert len(captured.out) > 0

    def test_text_art_color_consistency(self):
        """Test that color is consistently applied in TextArt."""
        art = TextArt()

        text = "HELLO"
        result = art.generate(text, color_code=Colors.RED)

        # Count color codes
        red_count = result.count(Colors.RED)
        reset_count = result.count(Colors.RESET)

        # Should have color codes for each line
        assert red_count > 0
        assert reset_count > 0
        # Resets should match color applications
        assert red_count == reset_count

    def test_image_converter_color_consistency(self):
        """Test that colors are consistently applied in ImageToASCII."""
        converter = ImageToASCII(width=20)
        image = np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)

        result = converter.convert_from_array(image, colored=True)

        # Should have ANSI color codes
        assert "\033[" in result
        # Should have reset codes
        assert Colors.RESET in result

    def test_mixed_usage_pattern(self):
        """Test mixed usage pattern of ASCII art features."""
        # Create instances
        text_art = TextArt()
        img_converter_simple = ImageToASCII(width=20, detailed=False)
        img_converter_detailed = ImageToASCII(width=20, detailed=True)

        # Use text art
        banner = text_art.generate_banner("BANNER", color_code=Colors.CYAN)
        assert Colors.CYAN in banner

        # Use simple image converter
        simple_image = np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)
        simple_result = img_converter_simple.convert_from_array(
            simple_image, colored=False
        )
        assert simple_result is not None

        # Use detailed image converter
        detailed_result = img_converter_detailed.convert_from_array(
            simple_image, colored=False
        )
        assert detailed_result is not None

        # Detailed should use more characters
        simple_chars = set(simple_result.replace("\n", ""))
        detailed_chars = set(detailed_result.replace("\n", ""))
        assert len(detailed_chars) >= len(simple_chars)

    def test_performance_text_art(self):
        """Test TextArt performance with long text."""
        art = TextArt()

        # Generate long text
        long_text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 3
        result = art.generate(long_text)

        assert result is not None
        assert len(result) > 0
        lines = result.split("\n")
        assert len(lines) == 5  # Should still have 5 lines

    def test_performance_image_converter(self):
        """Test ImageToASCII performance with large image."""
        converter = ImageToASCII(width=100)

        # Create large image
        large_image = np.random.randint(0, 255, (200, 200, 3), dtype=np.uint8)
        result = converter.convert_from_array(large_image, colored=False)

        assert result is not None
        assert len(result) > 0

    def test_text_art_edge_cases(self):
        """Test TextArt with edge cases."""
        art = TextArt()

        # Empty string
        empty_result = art.generate("")
        assert empty_result is not None

        # Single character
        single_result = art.generate("A")
        assert single_result is not None

        # Special characters only
        special_result = art.generate("!!!")
        assert special_result is not None

    def test_image_converter_edge_cases(self):
        """Test ImageToASCII with edge cases."""
        converter = ImageToASCII(width=5)

        # Minimum size image
        tiny_image = np.zeros((2, 2, 3), dtype=np.uint8)
        tiny_result = converter.convert_from_array(tiny_image, colored=False)
        assert tiny_result is not None

        # Single color image
        solid_image = np.ones((10, 10, 3), dtype=np.uint8) * 128
        solid_result = converter.convert_from_array(solid_image, colored=False)
        assert solid_result is not None

    def test_complete_workflow_example(self):
        """Test complete workflow example combining features."""
        # Create header with text art
        header = TextArt()
        title = header.generate_banner("ASCII ART", color_code=Colors.GREEN)
        assert title is not None

        # Create sample image visualization
        converter = ImageToASCII(width=40, detailed=True)
        # Create a simple pattern
        pattern = np.zeros((20, 40, 3), dtype=np.uint8)
        # Create checkerboard pattern
        for i in range(20):
            for j in range(40):
                if (i // 5 + j // 5) % 2 == 0:
                    pattern[i, j] = [255, 255, 255]
                else:
                    pattern[i, j] = [0, 0, 0]

        pattern_ascii = converter.convert_from_array(pattern, colored=False)
        assert pattern_ascii is not None

        # Both should work together
        combined = title + "\n\n" + pattern_ascii
        assert len(combined) > 0
        assert "\n" in combined

    def test_grayscale_vs_rgb_consistency(self):
        """Test consistency between grayscale and RGB conversion."""
        converter = ImageToASCII(width=20)

        # Create grayscale image with fixed seed for consistency
        np.random.seed(42)
        gray_image = np.random.randint(0, 255, (20, 20), dtype=np.uint8)

        # For grayscale, we need to test that the conversion works
        gray_result = converter.convert_from_array(gray_image, colored=False)

        # For RGB with same values in all channels
        rgb_image = np.stack([gray_image, gray_image, gray_image], axis=-1)
        rgb_result = converter.convert_from_array(rgb_image, colored=False)

        # Both should produce valid output
        assert gray_result is not None
        assert rgb_result is not None
        # Both should have same number of lines
        assert len(gray_result.split("\n")) == len(rgb_result.split("\n"))

    def test_multiple_instances_independence(self):
        """Test that multiple instances don't interfere with each other."""
        art1 = TextArt()
        art2 = TextArt()
        converter1 = ImageToASCII(width=20)
        converter2 = ImageToASCII(width=40)

        # Use instances
        result1 = art1.generate("A")
        result2 = art2.generate("B")
        assert result1 != result2

        image = np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)
        img_result1 = converter1.convert_from_array(image, colored=False)
        img_result2 = converter2.convert_from_array(image, colored=False)
        # Different widths should produce different results
        assert len(img_result1.split("\n")[0]) != len(img_result2.split("\n")[0])
