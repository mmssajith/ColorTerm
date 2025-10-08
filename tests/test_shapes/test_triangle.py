"""Test cases for Triangle shape."""

import unittest
from io import StringIO
from unittest.mock import patch
from colorterminal import Triangle, Colors


class TestTriangle(unittest.TestCase):
    """Test Triangle shape functionality."""

    def test_triangle_creation(self):
        """Test basic triangle creation."""
        triangle = Triangle(height=5)
        self.assertEqual(triangle.height, 5)
        self.assertTrue(triangle.filled)
        self.assertEqual(triangle.orientation, "up")
        self.assertEqual(triangle.color_code, Colors.WHITE)

    def test_custom_triangle_creation(self):
        """Test triangle with custom parameters."""
        triangle = Triangle(
            height=10,
            filled=False,
            orientation="down",
            color_code=Colors.MAGENTA,
            fill_char="*",
            border_char="o"
        )
        self.assertEqual(triangle.height, 10)
        self.assertFalse(triangle.filled)
        self.assertEqual(triangle.orientation, "down")
        self.assertEqual(triangle.color_code, Colors.MAGENTA)
        self.assertEqual(triangle.fill_char, "*")
        self.assertEqual(triangle.border_char, "o")

    @patch('sys.stdout', new_callable=StringIO)
    def test_up_triangle_rendering(self, mock_stdout):
        """Test upward-pointing triangle rendering."""
        triangle = Triangle(height=5, orientation="up")
        triangle.draw()
        output = mock_stdout.getvalue()
        lines = output.strip().split('\n')
        self.assertEqual(len(lines), 5)

    @patch('sys.stdout', new_callable=StringIO)
    def test_down_triangle_rendering(self, mock_stdout):
        """Test downward-pointing triangle rendering."""
        triangle = Triangle(height=5, orientation="down")
        triangle.draw()
        output = mock_stdout.getvalue()
        lines = output.strip().split('\n')
        self.assertEqual(len(lines), 5)

    @patch('sys.stdout', new_callable=StringIO)
    def test_left_triangle_rendering(self, mock_stdout):
        """Test left-pointing triangle rendering."""
        triangle = Triangle(height=5, orientation="left")
        triangle.draw()
        output = mock_stdout.getvalue()
        lines = output.strip().split('\n')
        self.assertEqual(len(lines), 5)

    @patch('sys.stdout', new_callable=StringIO)
    def test_right_triangle_rendering(self, mock_stdout):
        """Test right-pointing triangle rendering."""
        triangle = Triangle(height=5, orientation="right")
        triangle.draw()
        output = mock_stdout.getvalue()
        lines = output.strip().split('\n')
        self.assertEqual(len(lines), 5)

    def test_invalid_orientation_raises_error(self):
        """Test that invalid orientation raises ValueError."""
        triangle = Triangle(height=5, orientation="diagonal")
        with self.assertRaises(ValueError):
            triangle.draw()

    @patch('sys.stdout', new_callable=StringIO)
    def test_filled_triangle(self, mock_stdout):
        """Test filled triangle has fill characters."""
        triangle = Triangle(height=5, filled=True, fill_char="*")
        triangle.draw()
        output = mock_stdout.getvalue()
        self.assertIn("*", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_bordered_triangle(self, mock_stdout):
        """Test bordered triangle has border characters."""
        triangle = Triangle(height=5, filled=False, border_char="o")
        triangle.draw()
        output = mock_stdout.getvalue()
        self.assertIn("o", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_color_applied(self, mock_stdout):
        """Test that color code is applied."""
        triangle = Triangle(height=5, color_code=Colors.GREEN)
        triangle.draw()
        output = mock_stdout.getvalue()
        self.assertIn(Colors.GREEN, output)
        self.assertIn(Colors.RESET, output)

    def test_orientation_case_insensitive(self):
        """Test orientation is case insensitive."""
        triangle = Triangle(height=5, orientation="UP")
        self.assertEqual(triangle.orientation, "up")
