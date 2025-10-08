"""Test cases for Rectangle shape."""

import unittest
from io import StringIO
from unittest.mock import patch

from colorterminal import Colors, Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle shape functionality."""

    def test_rectangle_creation(self):
        """Test basic rectangle creation."""
        rect = Rectangle(width=10, height=5)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 5)
        self.assertTrue(rect.filled)
        self.assertEqual(rect.color_code, Colors.WHITE)

    def test_custom_rectangle_creation(self):
        """Test rectangle with custom parameters."""
        rect = Rectangle(
            width=15,
            height=8,
            filled=False,
            color_code=Colors.BLUE,
            fill_char="#",
            border_char="*",
        )
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 8)
        self.assertFalse(rect.filled)
        self.assertEqual(rect.color_code, Colors.BLUE)
        self.assertEqual(rect.fill_char, "#")
        self.assertEqual(rect.border_char, "*")

    @patch("sys.stdout", new_callable=StringIO)
    def test_filled_rectangle_rendering(self, mock_stdout):
        """Test filled rectangle rendering."""
        rect = Rectangle(width=5, height=3, filled=True)
        rect.draw()
        output = mock_stdout.getvalue()
        lines = output.strip().split("\n")
        self.assertEqual(len(lines), 3)

    @patch("sys.stdout", new_callable=StringIO)
    def test_bordered_rectangle_rendering(self, mock_stdout):
        """Test bordered rectangle rendering."""
        rect = Rectangle(width=5, height=3, filled=False, border_char="*")
        rect.draw()
        output = mock_stdout.getvalue()
        lines = output.strip().split("\n")
        self.assertEqual(len(lines), 3)
        self.assertIn("*", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_single_line_rectangle(self, mock_stdout):
        """Test rectangle with height of 1."""
        rect = Rectangle(width=10, height=1, filled=False)
        rect.draw()
        output = mock_stdout.getvalue()
        lines = output.strip().split("\n")
        self.assertEqual(len(lines), 1)

    @patch("sys.stdout", new_callable=StringIO)
    def test_color_applied(self, mock_stdout):
        """Test that color code is applied."""
        rect = Rectangle(width=5, height=3, color_code=Colors.RED)
        rect.draw()
        output = mock_stdout.getvalue()
        self.assertIn(Colors.RED, output)
        self.assertIn(Colors.RESET, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_bordered_rectangle_middle_rows(self, mock_stdout):
        """Test bordered rectangle has correct middle rows."""
        rect = Rectangle(width=5, height=5, filled=False, border_char="#")
        rect.draw()
        output = mock_stdout.getvalue()
        # Should have borders on sides with spaces in middle
        self.assertIn("#   #", output)
