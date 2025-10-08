"""Test cases for Base ProgressBar."""

import unittest
from io import StringIO
from unittest.mock import patch

from colorterminal import Colors, ProgressBar


class TestProgressBar(unittest.TestCase):
    """Test ProgressBar base functionality."""

    def test_progress_bar_creation(self):
        """Test basic progress bar creation."""
        bar = ProgressBar(total=100, width=40)
        self.assertEqual(bar.total, 100)
        self.assertEqual(bar.width, 40)
        self.assertEqual(bar.current, 0)

    def test_custom_characters(self):
        """Test custom fill and empty characters."""
        bar = ProgressBar(total=100, fill_char="#", empty_char="-")
        self.assertEqual(bar.fill_char, "#")
        self.assertEqual(bar.empty_char, "-")

    def test_update_progress(self):
        """Test updating progress."""
        bar = ProgressBar(total=100)
        bar.update(50)
        self.assertEqual(bar.current, 50)

    def test_update_exceeds_total(self):
        """Test that update caps at total."""
        bar = ProgressBar(total=100)
        bar.update(150)
        self.assertEqual(bar.current, 100)

    def test_increment(self):
        """Test incrementing progress."""
        bar = ProgressBar(total=100)
        bar.increment(10)
        self.assertEqual(bar.current, 10)
        bar.increment(5)
        self.assertEqual(bar.current, 15)

    def test_complete(self):
        """Test marking progress as complete."""
        bar = ProgressBar(total=100)
        bar.update(50)
        bar.complete()
        self.assertEqual(bar.current, 100)

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_output(self, mock_stdout):
        """Test progress bar display output."""
        bar = ProgressBar(total=100, width=10, fill_char="█", empty_char="░")
        bar.update(50)
        output = mock_stdout.getvalue()
        self.assertIn("█", output)
        self.assertIn("░", output)
        self.assertIn("50.00%", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_no_percentage(self, mock_stdout):
        """Test display without percentage."""
        bar = ProgressBar(total=100, show_percentage=False)
        bar.update(50)
        output = mock_stdout.getvalue()
        self.assertNotIn("%", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_prefix_suffix(self, mock_stdout):
        """Test prefix and suffix display."""
        bar = ProgressBar(total=100, prefix="Loading: ", suffix=" Done")
        bar.update(50)
        output = mock_stdout.getvalue()
        self.assertIn("Loading:", output)
        self.assertIn("Done", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_color_code_applied(self, mock_stdout):
        """Test that color code is applied."""
        bar = ProgressBar(total=100, color_code=Colors.BLUE)
        bar.update(50)
        output = mock_stdout.getvalue()
        self.assertIn(Colors.BLUE, output)
        self.assertIn(Colors.RESET, output)

    def test_zero_division_protection(self):
        """Test that zero total doesn't cause division errors."""
        bar = ProgressBar(total=0)
        bar.display()  # Should not raise exception

    @patch("sys.stdout", new_callable=StringIO)
    def test_full_progress(self, mock_stdout):
        """Test 100% progress display."""
        bar = ProgressBar(total=100, width=10)
        bar.update(100)
        output = mock_stdout.getvalue()
        self.assertIn("100.00%", output)
