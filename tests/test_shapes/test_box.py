"""Test cases for Box shape."""

import unittest
from io import StringIO
from unittest.mock import patch

from colorterminal import Box, Colors


class TestBox(unittest.TestCase):
    """Test Box shape functionality."""

    def test_box_creation(self):
        """Test basic box creation."""
        box = Box(width=10, height=5)
        self.assertEqual(box.width, 10)
        self.assertEqual(box.height, 5)
        self.assertEqual(box.style, "light")
        self.assertEqual(box.color_code, Colors.WHITE)

    def test_custom_box_creation(self):
        """Test box with custom parameters."""
        box = Box(
            width=20,
            height=10,
            style="heavy",
            color_code=Colors.BRIGHT_GREEN,
            title="Test Box",
        )
        self.assertEqual(box.width, 20)
        self.assertEqual(box.height, 10)
        self.assertEqual(box.style, "heavy")
        self.assertEqual(box.color_code, Colors.BRIGHT_GREEN)
        self.assertEqual(box.title, "Test Box")

    def test_box_styles_available(self):
        """Test that all box styles are available."""
        self.assertIn("light", Box.STYLES)
        self.assertIn("heavy", Box.STYLES)
        self.assertIn("double", Box.STYLES)
        self.assertIn("rounded", Box.STYLES)
        self.assertIn("dashed", Box.STYLES)

    def test_invalid_style_raises_error(self):
        """Test that invalid style raises ValueError."""
        with self.assertRaises(ValueError):
            Box(width=10, height=5, style="invalid_style")

    @patch("sys.stdout", new_callable=StringIO)
    def test_light_box_rendering(self, mock_stdout):
        """Test light style box rendering."""
        box = Box(width=10, height=5, style="light")
        box.draw()
        output = mock_stdout.getvalue()
        lines = output.strip().split("\n")
        # Should have height + 2 lines (top and bottom borders)
        self.assertEqual(len(lines), 7)
        # Check for light box characters
        self.assertIn("┌", output)
        self.assertIn("└", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_heavy_box_rendering(self, mock_stdout):
        """Test heavy style box rendering."""
        box = Box(width=10, height=5, style="heavy")
        box.draw()
        output = mock_stdout.getvalue()
        self.assertIn("┏", output)
        self.assertIn("┗", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_double_box_rendering(self, mock_stdout):
        """Test double style box rendering."""
        box = Box(width=10, height=5, style="double")
        box.draw()
        output = mock_stdout.getvalue()
        self.assertIn("╔", output)
        self.assertIn("╚", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_rounded_box_rendering(self, mock_stdout):
        """Test rounded style box rendering."""
        box = Box(width=10, height=5, style="rounded")
        box.draw()
        output = mock_stdout.getvalue()
        self.assertIn("╭", output)
        self.assertIn("╰", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_box_with_title(self, mock_stdout):
        """Test box with title rendering."""
        box = Box(width=20, height=5, title="My Title")
        box.draw()
        output = mock_stdout.getvalue()
        self.assertIn("My Title", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_color_applied(self, mock_stdout):
        """Test that color code is applied."""
        box = Box(width=10, height=5, color_code=Colors.BLUE)
        box.draw()
        output = mock_stdout.getvalue()
        self.assertIn(Colors.BLUE, output)
        self.assertIn(Colors.RESET, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_small_box(self, mock_stdout):
        """Test small box rendering."""
        box = Box(width=5, height=2)
        box.draw()
        output = mock_stdout.getvalue()
        lines = output.strip().split("\n")
        self.assertEqual(len(lines), 4)  # 2 + 2 borders

    @patch("sys.stdout", new_callable=StringIO)
    def test_large_box(self, mock_stdout):
        """Test large box rendering."""
        box = Box(width=50, height=20)
        box.draw()
        output = mock_stdout.getvalue()
        lines = output.strip().split("\n")
        self.assertEqual(len(lines), 22)  # 20 + 2 borders

    def test_style_case_insensitive(self):
        """Test style is case insensitive."""
        box = Box(width=10, height=5, style="HEAVY")
        self.assertEqual(box.style, "heavy")
