"""Test cases for Animated progress bar."""

import unittest
from unittest.mock import MagicMock, patch

from colorterminal import AnimatedProgressBar, Colors


class TestAnimatedProgressBar(unittest.TestCase):
    """Test AnimatedProgressBar functionality."""

    def test_progress_bar_creation(self):
        """Test basic animated progress bar creation."""
        bar = AnimatedProgressBar(total=100, width=40)
        self.assertEqual(bar.total, 100)
        self.assertEqual(bar.width, 40)
        self.assertEqual(bar.current, 0)
        self.assertFalse(bar.started)

    def test_default_color(self):
        """Test default color is set."""
        bar = AnimatedProgressBar(total=100)
        self.assertEqual(bar.color_code, Colors.GREEN)

    def test_custom_color(self):
        """Test custom color setting."""
        bar = AnimatedProgressBar(total=100, color_code=Colors.BLUE)
        self.assertEqual(bar.color_code, Colors.BLUE)

    @patch("sys.stdout", new=MagicMock())
    def test_update_progress(self):
        """Test updating animated progress."""
        bar = AnimatedProgressBar(total=100)
        bar.update(50)
        self.assertEqual(bar.current, 50)

    @patch("sys.stdout", new=MagicMock())
    def test_display_uses_carriage_return(self):
        """Test that display uses carriage return for animation."""
        bar = AnimatedProgressBar(total=100)
        with patch("sys.stdout.write") as mock_write:
            bar.update(50)
            # Check if any call contains \r
            calls = [str(call) for call in mock_write.call_args_list]
            self.assertTrue(any("\\r" in call for call in calls))

    @patch("sys.stdout", new=MagicMock())
    @patch("time.sleep")
    def test_animate_to(self, mock_sleep):
        """Test animate_to method."""
        bar = AnimatedProgressBar(total=100)
        bar.animate_to(50, steps=10, delay=0.01)
        self.assertEqual(bar.current, 50)
        # Verify sleep was called
        self.assertTrue(mock_sleep.called)

    @patch("sys.stdout", new=MagicMock())
    @patch("time.sleep")
    def test_simulate(self, mock_sleep):
        """Test simulate method."""
        bar = AnimatedProgressBar(total=100)
        bar.simulate(duration=0.1, steps=10)
        self.assertEqual(bar.current, 100)
        # Verify sleep was called
        self.assertTrue(mock_sleep.called)

    @patch("sys.stdout", new=MagicMock())
    def test_complete_prints_newline(self):
        """Test that completing prints a newline."""
        bar = AnimatedProgressBar(total=100)
        with patch("builtins.print") as mock_print:
            bar.update(100)
            # Should print newline when complete
            mock_print.assert_called()

    @patch("sys.stdout", new=MagicMock())
    @patch("time.sleep")
    def test_animate_to_caps_at_total(self, mock_sleep):
        """Test that animate_to caps at total."""
        bar = AnimatedProgressBar(total=100)
        bar.animate_to(150, steps=10)
        self.assertEqual(bar.current, 100)

    @patch("sys.stdout", new=MagicMock())
    def test_increment(self):
        """Test incrementing animated progress."""
        bar = AnimatedProgressBar(total=100)
        bar.increment(25)
        self.assertEqual(bar.current, 25)
        bar.increment(25)
        self.assertEqual(bar.current, 50)
