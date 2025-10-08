"""Test cases for Base Printer."""

import unittest
from io import StringIO
from unittest.mock import patch

from colorterminal import Colors, Printer


class TestPrinter(unittest.TestCase):
    """Test Printer base functionality."""

    def test_printer_exists(self):
        """Test that Printer class exists."""
        self.assertTrue(hasattr(Printer, "red"))
        self.assertTrue(hasattr(Printer, "green"))
        self.assertTrue(hasattr(Printer, "blue"))

    @patch("sys.stdout", new_callable=StringIO)
    def test_red_output(self, mock_stdout):
        """Test red color output."""
        Printer.red("Test message")
        output = mock_stdout.getvalue()
        self.assertIn("Test message", output)
        self.assertIn(Colors.RED, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_green_output(self, mock_stdout):
        """Test green color output."""
        Printer.green("Success")
        output = mock_stdout.getvalue()
        self.assertIn("Success", output)
        self.assertIn(Colors.GREEN, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_blue_output(self, mock_stdout):
        """Test blue color output."""
        Printer.blue("Info")
        output = mock_stdout.getvalue()
        self.assertIn("Info", output)
        self.assertIn(Colors.BLUE, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_yellow_output(self, mock_stdout):
        """Test yellow color output."""
        Printer.yellow("Warning")
        output = mock_stdout.getvalue()
        self.assertIn("Warning", output)
        self.assertIn(Colors.YELLOW, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_magenta_output(self, mock_stdout):
        """Test magenta color output."""
        Printer.magenta("Message")
        output = mock_stdout.getvalue()
        self.assertIn("Message", output)
        self.assertIn(Colors.MAGENTA, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_cyan_output(self, mock_stdout):
        """Test cyan color output."""
        Printer.cyan("Note")
        output = mock_stdout.getvalue()
        self.assertIn("Note", output)
        self.assertIn(Colors.CYAN, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_white_output(self, mock_stdout):
        """Test white color output."""
        Printer.white("Text")
        output = mock_stdout.getvalue()
        self.assertIn("Text", output)
        self.assertIn(Colors.WHITE, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_black_output(self, mock_stdout):
        """Test black color output."""
        Printer.black("Dark")
        output = mock_stdout.getvalue()
        self.assertIn("Dark", output)
        self.assertIn(Colors.BLACK, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_bright_colors(self, mock_stdout):
        """Test bright color outputs."""
        Printer.bright_red("Bright Red")
        output = mock_stdout.getvalue()
        self.assertIn("Bright Red", output)
        self.assertIn(Colors.BRIGHT_RED, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_reset_code_present(self, mock_stdout):
        """Test that reset code is included in output."""
        Printer.red("Test")
        output = mock_stdout.getvalue()
        self.assertIn(Colors.RESET, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_kwargs_passthrough(self, mock_stdout):
        """Test that kwargs are passed through to print."""
        Printer.green("Test", end="")
        output = mock_stdout.getvalue()
        # Should not have newline at the end
        self.assertEqual(output, f"{Colors.GREEN}Test{Colors.RESET}")
