"""Tests for TextArt class."""

from colorterminal import Colors, TextArt


class TestTextArt:
    """Test cases for TextArt class."""

    def test_initialization(self):
        """Test TextArt initialization."""
        art = TextArt()
        assert art.font is not None
        assert isinstance(art.font, dict)

    def test_initialization_with_font(self):
        """Test TextArt initialization with font parameter."""
        art = TextArt(font="simple")
        assert art.font is not None

    def test_generate_single_character(self):
        """Test generating ASCII art for a single character."""
        art = TextArt()
        result = art.generate("A")
        assert result is not None
        assert isinstance(result, str)
        assert len(result.split("\n")) == 5  # 5 lines per character

    def test_generate_multiple_characters(self):
        """Test generating ASCII art for multiple characters."""
        art = TextArt()
        result = art.generate("HELLO")
        assert result is not None
        assert "H" in result or "h" in result  # Character representation
        lines = result.split("\n")
        assert len(lines) == 5

    def test_generate_with_numbers(self):
        """Test generating ASCII art with numbers."""
        art = TextArt()
        result = art.generate("123")
        assert result is not None
        assert len(result.split("\n")) == 5

    def test_generate_with_spaces(self):
        """Test generating ASCII art with spaces."""
        art = TextArt()
        result = art.generate("HI THERE")
        assert result is not None
        lines = result.split("\n")
        assert len(lines) == 5

    def test_generate_with_special_characters(self):
        """Test generating ASCII art with special characters."""
        art = TextArt()
        result = art.generate("HELLO!")
        assert result is not None
        lines = result.split("\n")
        assert len(lines) == 5

    def test_generate_unknown_character_defaults_to_space(self):
        """Test that unknown characters default to space."""
        art = TextArt()
        result = art.generate("A@B")  # @ is not in the font
        assert result is not None
        lines = result.split("\n")
        assert len(lines) == 5

    def test_generate_lowercase_converts_to_uppercase(self):
        """Test that lowercase letters are converted to uppercase."""
        art = TextArt()
        result_lower = art.generate("hello")
        result_upper = art.generate("HELLO")
        assert result_lower == result_upper

    def test_generate_with_color(self):
        """Test generating ASCII art with color."""
        art = TextArt()
        result = art.generate("TEST", color_code=Colors.RED)
        assert result is not None
        assert Colors.RED in result
        assert Colors.RESET in result

    def test_generate_without_color(self):
        """Test generating ASCII art without color."""
        art = TextArt()
        result = art.generate("TEST")
        assert result is not None
        assert Colors.RED not in result
        assert Colors.RESET not in result

    def test_generate_empty_string(self):
        """Test generating ASCII art for empty string."""
        art = TextArt()
        result = art.generate("")
        assert result is not None
        lines = result.split("\n")
        assert len(lines) == 5

    def test_generate_all_supported_letters(self):
        """Test generating ASCII art for all supported letters."""
        art = TextArt()
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = art.generate(alphabet)
        assert result is not None
        lines = result.split("\n")
        assert len(lines) == 5
        # Check that result is not empty
        assert any(len(line.strip()) > 0 for line in lines)

    def test_generate_all_supported_numbers(self):
        """Test generating ASCII art for all supported numbers."""
        art = TextArt()
        numbers = "0123456789"
        result = art.generate(numbers)
        assert result is not None
        lines = result.split("\n")
        assert len(lines) == 5
        assert any(len(line.strip()) > 0 for line in lines)

    def test_generate_banner_basic(self):
        """Test generating a basic banner."""
        art = TextArt()
        result = art.generate_banner("TEST")
        assert result is not None
        lines = result.split("\n")
        assert len(lines) > 5  # Should have borders + text lines
        # First and last lines should be borders
        assert "=" in lines[0]
        assert "=" in lines[-1]

    def test_generate_banner_with_custom_border(self):
        """Test generating banner with custom border character."""
        art = TextArt()
        result = art.generate_banner("TEST", border_char="-")
        assert result is not None
        lines = result.split("\n")
        assert "-" in lines[0]
        assert "-" in lines[-1]

    def test_generate_banner_with_color(self):
        """Test generating colored banner."""
        art = TextArt()
        result = art.generate_banner("TEST", color_code=Colors.CYAN)
        assert result is not None
        assert Colors.CYAN in result
        assert Colors.RESET in result

    def test_generate_banner_with_asterisk_border(self):
        """Test generating banner with asterisk border."""
        art = TextArt()
        result = art.generate_banner("HI", border_char="*")
        assert result is not None
        lines = result.split("\n")
        assert "*" in lines[0]
        assert "*" in lines[-1]

    def test_display_method(self, capsys):
        """Test display method prints to stdout."""
        art = TextArt()
        art.display("A")
        captured = capsys.readouterr()
        assert captured.out is not None
        assert len(captured.out) > 0

    def test_display_method_with_color(self, capsys):
        """Test display method with color."""
        art = TextArt()
        art.display("A", color_code=Colors.GREEN)
        captured = capsys.readouterr()
        assert Colors.GREEN in captured.out
        assert Colors.RESET in captured.out

    def test_display_banner_method(self, capsys):
        """Test display_banner method prints to stdout."""
        art = TextArt()
        art.display_banner("TEST")
        captured = capsys.readouterr()
        assert captured.out is not None
        assert "=" in captured.out

    def test_display_banner_with_custom_border(self, capsys):
        """Test display_banner with custom border."""
        art = TextArt()
        art.display_banner("HI", border_char="#")
        captured = capsys.readouterr()
        assert "#" in captured.out

    def test_display_banner_with_color(self, capsys):
        """Test display_banner with color."""
        art = TextArt()
        art.display_banner("TEST", color_code=Colors.MAGENTA)
        captured = capsys.readouterr()
        assert Colors.MAGENTA in captured.out

    def test_font_contains_required_characters(self):
        """Test that font contains all required characters."""
        art = TextArt()
        required_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
        for char in required_chars:
            assert char in art.font, f"Character '{char}' missing from font"

    def test_font_character_has_five_lines(self):
        """Test that each font character has exactly 5 lines."""
        art = TextArt()
        for char, lines in art.font.items():
            assert len(lines) == 5, f"Character '{char}' should have 5 lines"

    def test_generate_with_different_colors(self):
        """Test generating with different color codes."""
        art = TextArt()
        colors = [
            Colors.RED,
            Colors.GREEN,
            Colors.BLUE,
            Colors.YELLOW,
            Colors.MAGENTA,
            Colors.CYAN,
        ]
        for color in colors:
            result = art.generate("A", color_code=color)
            assert color in result
            assert Colors.RESET in result

    def test_generate_mixed_alphanumeric(self):
        """Test generating mixed alphanumeric text."""
        art = TextArt()
        result = art.generate("ABC123XYZ")
        assert result is not None
        lines = result.split("\n")
        assert len(lines) == 5
        assert any(len(line.strip()) > 0 for line in lines)

    def test_generate_with_punctuation(self):
        """Test generating with punctuation marks."""
        art = TextArt()
        result = art.generate("HELLO!")
        assert result is not None
        lines = result.split("\n")
        assert len(lines) == 5

    def test_banner_border_width_matches_content(self):
        """Test that banner border width matches content width."""
        art = TextArt()
        result = art.generate_banner("TEST")
        lines = result.split("\n")
        # Remove ANSI codes for proper length comparison
        clean_lines = [line.replace("\033[", "").replace("m", "") for line in lines]
        border_length = len(clean_lines[0])
        # All lines should have similar lengths (accounting for spacing)
        for line in clean_lines:
            assert len(line) <= border_length + 10  # Allow some variance

    def test_consistent_output_format(self):
        """Test that output format is consistent."""
        art = TextArt()
        result1 = art.generate("TEST")
        result2 = art.generate("TEST")
        assert result1 == result2  # Same input should produce same output

    def test_generate_preserves_whitespace(self):
        """Test that whitespace is preserved in output."""
        art = TextArt()
        result = art.generate("A B C")
        lines = result.split("\n")
        # Should have spacing between letters
        assert len(lines[0]) > 15  # Rough check for spacing
