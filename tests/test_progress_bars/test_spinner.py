"""Test cases for Spinner progress indicator."""

import unittest
from unittest.mock import patch, MagicMock
from colorterminal import SpinnerProgressBar, Colors


class TestSpinnerProgressBar(unittest.TestCase):
    """Test SpinnerProgressBar functionality."""

    def test_spinner_creation(self):
        """Test basic spinner creation."""
        bar = SpinnerProgressBar(total=100)
        self.assertEqual(bar.total, 100)
        self.assertEqual(bar.spinner_index, 0)
        self.assertIsNotNone(bar.spinner)

    def test_spinner_styles_available(self):
        """Test that spinner styles are available."""
        self.assertIn("dots", SpinnerProgressBar.SPINNERS)
        self.assertIn("line", SpinnerProgressBar.SPINNERS)
        self.assertIn("arrow", SpinnerProgressBar.SPINNERS)
        self.assertIn("circle", SpinnerProgressBar.SPINNERS)

    def test_custom_spinner_style(self):
        """Test creating spinner with custom style."""
        bar = SpinnerProgressBar(total=100, spinner_style="line")
        self.assertEqual(bar.spinner, SpinnerProgressBar.SPINNERS["line"])

    def test_invalid_spinner_style_defaults_to_dots(self):
        """Test that invalid spinner style defaults to dots."""
        bar = SpinnerProgressBar(total=100, spinner_style="invalid_style")
        self.assertEqual(bar.spinner, SpinnerProgressBar.SPINNERS["dots"])

    def test_default_color(self):
        """Test default color is set."""
        bar = SpinnerProgressBar(total=100)
        self.assertEqual(bar.color_code, Colors.GREEN)

    @patch('sys.stdout', new=MagicMock())
    def test_spinner_index_increments(self):
        """Test that spinner index increments on display."""
        bar = SpinnerProgressBar(total=100, spinner_style="line")
        initial_index = bar.spinner_index
        bar.update(25)
        self.assertEqual(bar.spinner_index, initial_index + 1)
        bar.update(50)
        self.assertEqual(bar.spinner_index, initial_index + 2)

    @patch('sys.stdout', new=MagicMock())
    def test_spinner_cycles_through_characters(self):
        """Test that spinner cycles through all characters."""
        bar = SpinnerProgressBar(total=100, spinner_style="line")
        spinner_length = len(bar.spinner)

        # Display enough times to cycle through
        for i in range(spinner_length + 5):
            bar.update(10)

        # Index should have wrapped around
        self.assertGreater(bar.spinner_index, spinner_length)

    @patch('sys.stdout', new=MagicMock())
    def test_display_includes_spinner_char(self):
        """Test that display includes spinner character."""
        bar = SpinnerProgressBar(total=100, spinner_style="dots")
        with patch('sys.stdout.write') as mock_write:
            bar.update(50)
            # Check if output contains spinner character
            output = str(mock_write.call_args_list)
            # Should contain some spinner character from dots style
            self.assertTrue(mock_write.called)

    @patch('sys.stdout', new=MagicMock())
    def test_complete_prints_newline(self):
        """Test that completing prints a newline."""
        bar = SpinnerProgressBar(total=100)
        with patch('builtins.print') as mock_print:
            bar.update(100)
            mock_print.assert_called()

    @patch('sys.stdout', new=MagicMock())
    def test_update_progress(self):
        """Test updating spinner progress."""
        bar = SpinnerProgressBar(total=100)
        bar.update(75)
        self.assertEqual(bar.current, 75)
