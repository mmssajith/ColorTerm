"""Test cases for Style printer."""

import unittest
from io import StringIO
from unittest.mock import patch

from colorterminal import Colors, StylePrinter, Styles


class TestStylePrinter(unittest.TestCase):
    """Test StylePrinter functionality."""

    def test_style_printer_exists(self):
        """Test that StylePrinter class exists."""
        self.assertTrue(hasattr(StylePrinter, "bold"))
        self.assertTrue(hasattr(StylePrinter, "underline"))
        self.assertTrue(hasattr(StylePrinter, "italic"))

    @patch("sys.stdout", new_callable=StringIO)
    def test_bold_output(self, mock_stdout):
        """Test bold style output."""
        StylePrinter.bold("Bold text")
        output = mock_stdout.getvalue()
        self.assertIn("Bold text", output)
        self.assertIn(Styles.BOLD, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_underline_output(self, mock_stdout):
        """Test underline style output."""
        StylePrinter.underline("Underlined text")
        output = mock_stdout.getvalue()
        self.assertIn("Underlined text", output)
        self.assertIn(Styles.UNDERLINE, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_italic_output(self, mock_stdout):
        """Test italic style output."""
        StylePrinter.italic("Italic text")
        output = mock_stdout.getvalue()
        self.assertIn("Italic text", output)
        self.assertIn(Styles.ITALIC, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_bold_red_output(self, mock_stdout):
        """Test bold red combined style."""
        StylePrinter.bold_red("Bold Red")
        output = mock_stdout.getvalue()
        self.assertIn("Bold Red", output)
        self.assertIn(Styles.BOLD, output)
        self.assertIn(Colors.RED, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_bold_green_output(self, mock_stdout):
        """Test bold green combined style."""
        StylePrinter.bold_green("Bold Green")
        output = mock_stdout.getvalue()
        self.assertIn("Bold Green", output)
        self.assertIn(Styles.BOLD, output)
        self.assertIn(Colors.GREEN, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_bold_yellow_output(self, mock_stdout):
        """Test bold yellow combined style."""
        StylePrinter.bold_yellow("Bold Yellow")
        output = mock_stdout.getvalue()
        self.assertIn("Bold Yellow", output)
        self.assertIn(Styles.BOLD, output)
        self.assertIn(Colors.YELLOW, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_reset_code_present(self, mock_stdout):
        """Test that reset code is included in styled output."""
        StylePrinter.bold("Test")
        output = mock_stdout.getvalue()
        self.assertIn(Colors.RESET, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_kwargs_passthrough(self, mock_stdout):
        """Test that kwargs are passed through to print."""
        StylePrinter.bold("Test", end="")
        output = mock_stdout.getvalue()
        # Should not have newline at the end
        self.assertEqual(output, f"{Styles.BOLD}Test{Colors.RESET}")
