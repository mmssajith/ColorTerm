"""Test cases for Grid table."""

import unittest
from io import StringIO
from unittest.mock import patch

from colorterminal import Colors, Grid


class TestGrid(unittest.TestCase):
    """Test Grid functionality."""

    def test_grid_creation(self):
        """Test basic grid creation."""
        grid = Grid(columns=3, cell_width=20, cell_height=3)
        self.assertEqual(grid.columns, 3)
        self.assertEqual(grid.cell_width, 20)
        self.assertEqual(grid.cell_height, 3)
        self.assertEqual(len(grid.cells), 0)

    def test_custom_grid_creation(self):
        """Test grid with custom parameters."""
        grid = Grid(
            columns=4,
            cell_width=15,
            cell_height=2,
            style="heavy",
            color_code=Colors.BLUE,
        )
        self.assertEqual(grid.columns, 4)
        self.assertEqual(grid.cell_width, 15)
        self.assertEqual(grid.cell_height, 2)
        self.assertEqual(grid.style, "heavy")
        self.assertEqual(grid.color_code, Colors.BLUE)

    def test_add_cell_string(self):
        """Test adding a cell with string content."""
        grid = Grid(columns=2)
        grid.add_cell("Cell 1")
        self.assertEqual(len(grid.cells), 1)
        self.assertEqual(grid.cells[0], ["Cell 1"])

    def test_add_cell_list(self):
        """Test adding a cell with list content."""
        grid = Grid(columns=2)
        grid.add_cell(["Line 1", "Line 2", "Line 3"])
        self.assertEqual(len(grid.cells), 1)
        self.assertEqual(grid.cells[0], ["Line 1", "Line 2", "Line 3"])

    def test_add_multiple_cells(self):
        """Test adding multiple cells."""
        grid = Grid(columns=2)
        grid.add_cell("Cell 1")
        grid.add_cell("Cell 2")
        grid.add_cell("Cell 3")
        self.assertEqual(len(grid.cells), 3)

    @patch("sys.stdout", new_callable=StringIO)
    def test_grid_display_empty(self, mock_stdout):
        """Test displaying empty grid does nothing."""
        grid = Grid(columns=2)
        grid.display()
        output = mock_stdout.getvalue()
        self.assertEqual(output, "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_grid_display_with_cells(self, mock_stdout):
        """Test grid display with cells."""
        grid = Grid(columns=2, cell_width=10, cell_height=2)
        grid.add_cell("Cell 1")
        grid.add_cell("Cell 2")
        grid.display()
        output = mock_stdout.getvalue()
        self.assertIn("Cell 1", output)
        self.assertIn("Cell 2", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_grid_with_light_style(self, mock_stdout):
        """Test grid with light style borders."""
        grid = Grid(columns=2, style="light")
        grid.add_cell("Test")
        grid.display()
        output = mock_stdout.getvalue()
        self.assertIn("┌", output)
        self.assertIn("└", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_grid_with_heavy_style(self, mock_stdout):
        """Test grid with heavy style borders."""
        grid = Grid(columns=2, style="heavy")
        grid.add_cell("Test")
        grid.display()
        output = mock_stdout.getvalue()
        self.assertIn("┏", output)
        self.assertIn("┗", output)

    def test_invalid_style_raises_error(self):
        """Test that invalid style raises ValueError."""
        with self.assertRaises(ValueError):
            Grid(columns=2, style="invalid_style")

    @patch("sys.stdout", new_callable=StringIO)
    def test_grid_multiple_rows(self, mock_stdout):
        """Test grid with multiple rows."""
        grid = Grid(columns=2, cell_width=10, cell_height=2)
        for i in range(5):
            grid.add_cell(f"Cell {i + 1}")
        grid.display()
        output = mock_stdout.getvalue()
        # Should create 3 rows (5 cells / 2 columns = 2.5 rounds up to 3)
        for i in range(1, 6):
            self.assertIn(f"Cell {i}", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_grid_color_applied(self, mock_stdout):
        """Test that color code is applied to grid."""
        grid = Grid(columns=2, color_code=Colors.RED)
        grid.add_cell("Test")
        grid.display()
        output = mock_stdout.getvalue()
        self.assertIn(Colors.RED, output)
        self.assertIn(Colors.RESET, output)

    def test_style_case_insensitive(self):
        """Test style is case insensitive."""
        grid = Grid(columns=2, style="HEAVY")
        self.assertEqual(grid.style, "heavy")

    @patch("sys.stdout", new_callable=StringIO)
    def test_grid_cell_truncation(self, mock_stdout):
        """Test that long cell content is truncated."""
        grid = Grid(columns=1, cell_width=5, cell_height=1)
        grid.add_cell("This is a very long text that should be truncated")
        grid.display()
        output = mock_stdout.getvalue()
        # Should only show first 5 characters
        self.assertIn("This ", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_grid_multiline_cell(self, mock_stdout):
        """Test grid with multiline cell content."""
        grid = Grid(columns=1, cell_width=10, cell_height=3)
        grid.add_cell(["Line 1", "Line 2", "Line 3"])
        grid.display()
        output = mock_stdout.getvalue()
        self.assertIn("Line 1", output)
        self.assertIn("Line 2", output)
        self.assertIn("Line 3", output)
