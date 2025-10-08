"""Test cases for Multi progress bar."""

import unittest
from io import StringIO
from unittest.mock import patch
from colorterminal import MultiProgressBar, Colors


class TestMultiProgressBar(unittest.TestCase):
    """Test MultiProgressBar functionality."""

    def test_multi_progress_bar_creation(self):
        """Test basic multi progress bar creation."""
        multi = MultiProgressBar()
        self.assertEqual(len(multi.bars), 0)
        self.assertEqual(len(multi.labels), 0)

    def test_add_single_bar(self):
        """Test adding a single progress bar."""
        multi = MultiProgressBar()
        multi.add_bar("task1", total=100)
        self.assertEqual(len(multi.bars), 1)
        self.assertIn("task1", multi.bars)
        self.assertIn("task1", multi.labels)

    def test_add_multiple_bars(self):
        """Test adding multiple progress bars."""
        multi = MultiProgressBar()
        multi.add_bar("task1", total=100)
        multi.add_bar("task2", total=50)
        multi.add_bar("task3", total=200)

        self.assertEqual(len(multi.bars), 3)
        self.assertIn("task1", multi.bars)
        self.assertIn("task2", multi.bars)
        self.assertIn("task3", multi.bars)

    def test_add_bar_with_custom_settings(self):
        """Test adding bar with custom settings."""
        multi = MultiProgressBar()
        multi.add_bar(
            "task1",
            total=100,
            width=50,
            color_code=Colors.BLUE,
            fill_char="#"
        )

        bar = multi.get_bar("task1")
        self.assertEqual(bar.total, 100)
        self.assertEqual(bar.width, 50)
        self.assertEqual(bar.color_code, Colors.BLUE)
        self.assertEqual(bar.fill_char, "#")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_bar(self, mock_stdout):
        """Test updating a specific bar."""
        multi = MultiProgressBar()
        multi.add_bar("task1", total=100)
        multi.update("task1", 50)

        bar = multi.get_bar("task1")
        self.assertEqual(bar.current, 50)

    def test_update_nonexistent_bar(self):
        """Test updating a bar that doesn't exist."""
        multi = MultiProgressBar()
        # Should not raise exception
        multi.update("nonexistent", 50)

    def test_get_bar(self):
        """Test retrieving a specific bar."""
        multi = MultiProgressBar()
        multi.add_bar("task1", total=100)

        bar = multi.get_bar("task1")
        self.assertIsNotNone(bar)
        self.assertEqual(bar.total, 100)

    def test_get_nonexistent_bar(self):
        """Test retrieving a nonexistent bar."""
        multi = MultiProgressBar()
        bar = multi.get_bar("nonexistent")
        self.assertIsNone(bar)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_all(self, mock_stdout):
        """Test displaying all progress bars."""
        multi = MultiProgressBar()
        multi.add_bar("task1", total=100)
        multi.add_bar("task2", total=50)
        multi.update("task1", 50)
        multi.update("task2", 25)

        multi.display_all()
        output = mock_stdout.getvalue()

        self.assertIn("Progress Status", output)
        self.assertIn("task1:", output)
        self.assertIn("task2:", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_labels_order_preserved(self, mock_stdout):
        """Test that labels are displayed in order added."""
        multi = MultiProgressBar()
        multi.add_bar("first", total=100)
        multi.add_bar("second", total=100)
        multi.add_bar("third", total=100)

        self.assertEqual(multi.labels, ["first", "second", "third"])

    @patch('sys.stdout', new_callable=StringIO)
    def test_multiple_updates(self, mock_stdout):
        """Test multiple updates to same bar."""
        multi = MultiProgressBar()
        multi.add_bar("task1", total=100)

        multi.update("task1", 25)
        self.assertEqual(multi.get_bar("task1").current, 25)

        multi.update("task1", 50)
        self.assertEqual(multi.get_bar("task1").current, 50)

        multi.update("task1", 100)
        self.assertEqual(multi.get_bar("task1").current, 100)

    @patch('sys.stdout', new_callable=StringIO)
    def test_bar_prefix_includes_label(self, mock_stdout):
        """Test that bar prefix includes the label."""
        multi = MultiProgressBar()
        multi.add_bar("Download", total=100)

        bar = multi.get_bar("Download")
        self.assertIn("Download:", bar.prefix)
