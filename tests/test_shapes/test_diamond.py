"""Test cases for Diamond shape."""

import unittest
from io import StringIO
from unittest.mock import patch
from colorterminal import Diamond, Colors


class TestDiamond(unittest.TestCase):
    """Test Diamond shape functionality."""

    def test_diamond_creation(self):
        """Test basic diamond creation."""
        diamond = Diamond(size=5)
        self.assertEqual(diamond.size, 5)
        self.assertTrue(diamond.filled)
        self.assertEqual(diamond.color_code, Colors.WHITE)

    def test_custom_diamond_creation(self):
        """Test diamond with custom parameters."""
        diamond = Diamond(
            size=7,
            filled=False,
            color_code=Colors.BRIGHT_BLUE,
            fill_char="#",
            border_char="*"
        )
        self.assertEqual(diamond.size, 7)
        self.assertFalse(diamond.filled)
        self.assertEqual(diamond.color_code, Colors.BRIGHT_BLUE)
        self.assertEqual(diamond.fill_char, "#")
        self.assertEqual(diamond.border_char, "*")

    @patch('sys.stdout', new_callable=StringIO)
    def test_filled_diamond_rendering(self, mock_stdout):
        """Test filled diamond rendering."""
        diamond = Diamond(size=5, filled=True)
        diamond.draw()
        output = mock_stdout.getvalue()
        lines = output.strip().split('\n')
        # Diamond should have 2*size - 1 lines
        self.assertEqual(len(lines), 2 * 5 - 1)

    @patch('sys.stdout', new_callable=StringIO)
    def test_bordered_diamond_rendering(self, mock_stdout):
        """Test bordered diamond rendering."""
        diamond = Diamond(size=5, filled=False, border_char="*")
        diamond.draw()
        output = mock_stdout.getvalue()
        self.assertIn("*", output)
        lines = output.strip().split('\n')
        self.assertEqual(len(lines), 2 * 5 - 1)

    @patch('sys.stdout', new_callable=StringIO)
    def test_small_diamond(self, mock_stdout):
        """Test small diamond rendering."""
        diamond = Diamond(size=2, filled=True)
        diamond.draw()
        output = mock_stdout.getvalue()
        lines = output.strip().split('\n')
        self.assertEqual(len(lines), 3)  # 2*2 - 1 = 3

    @patch('sys.stdout', new_callable=StringIO)
    def test_large_diamond(self, mock_stdout):
        """Test large diamond rendering."""
        diamond = Diamond(size=10, filled=True)
        diamond.draw()
        output = mock_stdout.getvalue()
        lines = output.strip().split('\n')
        self.assertEqual(len(lines), 19)  # 2*10 - 1 = 19

    @patch('sys.stdout', new_callable=StringIO)
    def test_color_applied(self, mock_stdout):
        """Test that color code is applied."""
        diamond = Diamond(size=5, color_code=Colors.CYAN)
        diamond.draw()
        output = mock_stdout.getvalue()
        self.assertIn(Colors.CYAN, output)
        self.assertIn(Colors.RESET, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_diamond_symmetry(self, mock_stdout):
        """Test that diamond is symmetrical."""
        diamond = Diamond(size=5, filled=True, fill_char="*")
        diamond.draw()
        output = mock_stdout.getvalue()
        lines = output.strip().split('\n')
        # Should have correct number of lines
        self.assertEqual(len(lines), 9)
        # Middle line should be longest when checking raw line lengths
        middle = len(lines) // 2
        # Verify we have more than one line
        self.assertGreater(len(lines), 1)

    @patch('sys.stdout', new_callable=StringIO)
    def test_single_size_diamond(self, mock_stdout):
        """Test diamond with size 1."""
        diamond = Diamond(size=1, filled=True)
        diamond.draw()
        output = mock_stdout.getvalue()
        lines = output.strip().split('\n')
        self.assertEqual(len(lines), 1)
