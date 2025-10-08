"""Test cases for Circle shape."""

import unittest
from io import StringIO
from unittest.mock import patch

from colorterminal import Circle, Colors


class TestCircle(unittest.TestCase):
    """Test Circle shape functionality."""

    def test_circle_creation(self):
        """Test basic circle creation."""
        circle = Circle(radius=5)
        self.assertEqual(circle.radius, 5)
        self.assertTrue(circle.filled)
        self.assertEqual(circle.color_code, Colors.WHITE)

    def test_custom_circle_creation(self):
        """Test circle with custom parameters."""
        circle = Circle(
            radius=10,
            filled=False,
            color_code=Colors.CYAN,
            fill_char="O",
            border_char="*",
        )
        self.assertEqual(circle.radius, 10)
        self.assertFalse(circle.filled)
        self.assertEqual(circle.color_code, Colors.CYAN)
        self.assertEqual(circle.fill_char, "O")
        self.assertEqual(circle.border_char, "*")

    @patch("sys.stdout", new_callable=StringIO)
    def test_filled_circle_rendering(self, mock_stdout):
        """Test filled circle rendering."""
        circle = Circle(radius=5, filled=True)
        circle.draw()
        output = mock_stdout.getvalue()
        # Should produce output with filled characters
        self.assertGreater(len(output), 0)
        lines = [line for line in output.split("\n") if line.strip()]
        self.assertGreater(len(lines), 0)

    @patch("sys.stdout", new_callable=StringIO)
    def test_bordered_circle_rendering(self, mock_stdout):
        """Test bordered circle rendering."""
        circle = Circle(radius=5, filled=False, border_char="*")
        circle.draw()
        output = mock_stdout.getvalue()
        self.assertIn("*", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_small_circle(self, mock_stdout):
        """Test small circle rendering."""
        circle = Circle(radius=2, filled=True)
        circle.draw()
        output = mock_stdout.getvalue()
        self.assertGreater(len(output), 0)

    @patch("sys.stdout", new_callable=StringIO)
    def test_color_applied(self, mock_stdout):
        """Test that color code is applied."""
        circle = Circle(radius=5, color_code=Colors.YELLOW)
        circle.draw()
        output = mock_stdout.getvalue()
        self.assertIn(Colors.YELLOW, output)
        self.assertIn(Colors.RESET, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_large_circle(self, mock_stdout):
        """Test large circle rendering."""
        circle = Circle(radius=10, filled=True)
        circle.draw()
        output = mock_stdout.getvalue()
        lines = [line for line in output.split("\n") if line.strip()]
        # Larger circle should have more lines
        self.assertGreater(len(lines), 10)
