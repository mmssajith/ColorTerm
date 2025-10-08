"""Test cases for Line shape."""

import unittest
from io import StringIO
from unittest.mock import patch
from colorterminal import Line, Colors


class TestLine(unittest.TestCase):
    """Test Line shape functionality."""

    def test_line_creation(self):
        """Test basic line creation."""
        line = Line(length=10)
        self.assertEqual(line.length, 10)
        self.assertEqual(line.orientation, "horizontal")
        self.assertEqual(line.color_code, Colors.WHITE)

    def test_custom_line_creation(self):
        """Test line creation with custom parameters."""
        line = Line(length=20, orientation="vertical", color_code=Colors.RED, fill_char="*")
        self.assertEqual(line.length, 20)
        self.assertEqual(line.orientation, "vertical")
        self.assertEqual(line.color_code, Colors.RED)
        self.assertEqual(line.fill_char, "*")

    @patch('sys.stdout', new_callable=StringIO)
    def test_horizontal_line_rendering(self, mock_stdout):
        """Test horizontal line rendering."""
        line = Line(length=10, orientation="horizontal", fill_char="=")
        line.draw()
        output = mock_stdout.getvalue()
        self.assertIn("=", output)
        self.assertIn(Colors.RESET, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_vertical_line_rendering(self, mock_stdout):
        """Test vertical line rendering."""
        line = Line(length=5, orientation="vertical", fill_char="|")
        line.draw()
        output = mock_stdout.getvalue()
        # Should have 5 lines
        lines = output.strip().split('\n')
        self.assertEqual(len(lines), 5)
        self.assertIn("|", output)

    def test_invalid_orientation_raises_error(self):
        """Test that invalid orientation raises ValueError."""
        line = Line(length=10, orientation="diagonal")
        with self.assertRaises(ValueError):
            line.draw()

    @patch('sys.stdout', new_callable=StringIO)
    def test_color_applied(self, mock_stdout):
        """Test that color code is applied."""
        line = Line(length=5, color_code=Colors.GREEN)
        line.draw()
        output = mock_stdout.getvalue()
        self.assertIn(Colors.GREEN, output)

    def test_orientation_case_insensitive(self):
        """Test orientation is case insensitive."""
        line1 = Line(length=5, orientation="HORIZONTAL")
        line2 = Line(length=5, orientation="Vertical")
        self.assertEqual(line1.orientation, "horizontal")
        self.assertEqual(line2.orientation, "vertical")
