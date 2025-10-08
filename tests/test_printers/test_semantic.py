"""Test cases for Semantic printer."""

import unittest
from io import StringIO
from unittest.mock import patch
from colorterminal import SemanticPrinter, Colors


class TestSemanticPrinter(unittest.TestCase):
    """Test SemanticPrinter functionality."""

    def test_semantic_printer_exists(self):
        """Test that SemanticPrinter class exists."""
        self.assertTrue(hasattr(SemanticPrinter, 'success'))
        self.assertTrue(hasattr(SemanticPrinter, 'error'))
        self.assertTrue(hasattr(SemanticPrinter, 'warning'))
        self.assertTrue(hasattr(SemanticPrinter, 'info'))

    @patch('sys.stdout', new_callable=StringIO)
    def test_success_message(self, mock_stdout):
        """Test success message output."""
        SemanticPrinter.success("Operation completed")
        output = mock_stdout.getvalue()
        self.assertIn("Operation completed", output)
        self.assertIn("✓", output)
        self.assertIn(Colors.GREEN, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_error_message(self, mock_stdout):
        """Test error message output."""
        SemanticPrinter.error("Something went wrong")
        output = mock_stdout.getvalue()
        self.assertIn("Something went wrong", output)
        self.assertIn("✗", output)
        self.assertIn(Colors.RED, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_warning_message(self, mock_stdout):
        """Test warning message output."""
        SemanticPrinter.warning("Be careful")
        output = mock_stdout.getvalue()
        self.assertIn("Be careful", output)
        self.assertIn("⚠", output)
        self.assertIn(Colors.YELLOW, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_info_message(self, mock_stdout):
        """Test info message output."""
        SemanticPrinter.info("Just so you know")
        output = mock_stdout.getvalue()
        self.assertIn("Just so you know", output)
        self.assertIn("ℹ", output)
        self.assertIn(Colors.CYAN, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_reset_code_present(self, mock_stdout):
        """Test that reset code is included in output."""
        SemanticPrinter.success("Test")
        output = mock_stdout.getvalue()
        self.assertIn(Colors.RESET, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_kwargs_passthrough(self, mock_stdout):
        """Test that kwargs are passed through to print."""
        SemanticPrinter.success("Test", end='')
        output = mock_stdout.getvalue()
        # Should not have newline at the end
        expected = f"{Colors.GREEN}✓ Test{Colors.RESET}"
        self.assertEqual(output, expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_multiple_semantic_calls(self, mock_stdout):
        """Test multiple semantic messages in sequence."""
        SemanticPrinter.success("Step 1 complete")
        SemanticPrinter.info("Processing step 2")
        SemanticPrinter.warning("Step 2 has issues")
        SemanticPrinter.error("Step 2 failed")

        output = mock_stdout.getvalue()
        self.assertIn("Step 1 complete", output)
        self.assertIn("Processing step 2", output)
        self.assertIn("Step 2 has issues", output)
        self.assertIn("Step 2 failed", output)
