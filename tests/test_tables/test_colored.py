"""Test cases for Colored table."""

import unittest
from io import StringIO
from unittest.mock import patch

from colorterminal import ColoredTable, Colors


class TestColoredTable(unittest.TestCase):
    """Test ColoredTable functionality."""

    def test_colored_table_creation(self):
        """Test basic colored table creation."""
        table = ColoredTable(headers=["Name", "Age", "City"])
        self.assertEqual(table.headers, ["Name", "Age", "City"])
        self.assertIsNotNone(table.alternating_colors)
        self.assertEqual(len(table.row_colors), 0)

    def test_custom_colored_table_creation(self):
        """Test colored table with custom parameters."""
        table = ColoredTable(
            headers=["Col1", "Col2"],
            style="double",
            alternating_colors=[Colors.GREEN, Colors.BLUE],
        )
        self.assertEqual(table.style, "double")
        self.assertEqual(table.alternating_colors, [Colors.GREEN, Colors.BLUE])

    def test_add_row_without_color(self):
        """Test adding row without explicit color."""
        table = ColoredTable(headers=["Name", "Age"])
        table.add_row(["Alice", 30])
        self.assertEqual(len(table.rows), 1)
        self.assertEqual(len(table.row_colors), 1)
        self.assertIsNone(table.row_colors[0])

    def test_add_row_with_color(self):
        """Test adding row with explicit color."""
        table = ColoredTable(headers=["Name", "Age"])
        table.add_row(["Alice", 30], color=Colors.RED)
        self.assertEqual(len(table.rows), 1)
        self.assertEqual(table.row_colors[0], Colors.RED)

    def test_multiple_rows_with_colors(self):
        """Test adding multiple rows with different colors."""
        table = ColoredTable(headers=["Name", "Age"])
        table.add_row(["Alice", 30], color=Colors.RED)
        table.add_row(["Bob", 25], color=Colors.GREEN)
        table.add_row(["Charlie", 35], color=Colors.BLUE)

        self.assertEqual(len(table.rows), 3)
        self.assertEqual(table.row_colors[0], Colors.RED)
        self.assertEqual(table.row_colors[1], Colors.GREEN)
        self.assertEqual(table.row_colors[2], Colors.BLUE)

    def test_default_alternating_colors(self):
        """Test default alternating colors."""
        table = ColoredTable(headers=["Name"])
        self.assertIsNotNone(table.alternating_colors)
        self.assertEqual(len(table.alternating_colors), 2)

    @patch("sys.stdout", new_callable=StringIO)
    def test_colored_table_display(self, mock_stdout):
        """Test colored table display."""
        table = ColoredTable(headers=["Name", "Age"])
        table.add_row(["Alice", 30], color=Colors.GREEN)
        table.display()
        output = mock_stdout.getvalue()
        self.assertIn("Name", output)
        self.assertIn("Alice", output)
        self.assertIn(Colors.GREEN, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_alternating_colors_applied(self, mock_stdout):
        """Test that alternating colors are applied."""
        table = ColoredTable(
            headers=["Name"], alternating_colors=[Colors.RED, Colors.BLUE]
        )
        table.add_row(["Alice"])
        table.add_row(["Bob"])
        table.add_row(["Charlie"])
        table.display()
        output = mock_stdout.getvalue()
        # Both alternating colors should appear
        self.assertIn(Colors.RED, output)
        self.assertIn(Colors.BLUE, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_explicit_color_overrides_alternating(self, mock_stdout):
        """Test that explicit row color overrides alternating."""
        table = ColoredTable(
            headers=["Name"], alternating_colors=[Colors.RED, Colors.BLUE]
        )
        table.add_row(["Alice"], color=Colors.GREEN)
        table.display()
        output = mock_stdout.getvalue()
        # Should contain the explicit color
        self.assertIn(Colors.GREEN, output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_empty_colored_table(self, mock_stdout):
        """Test displaying empty colored table."""
        table = ColoredTable()
        table.display()
        output = mock_stdout.getvalue()
        self.assertEqual(output, "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_colored_table_with_multiple_styles(self, mock_stdout):
        """Test colored table with different border styles."""
        for style in ["light", "heavy", "double", "rounded", "ascii"]:
            table = ColoredTable(headers=["Col1"], style=style)
            table.add_row(["Data"], color=Colors.CYAN)
            table.display()
            output = mock_stdout.getvalue()
            self.assertIn("Data", output)
            self.assertIn(Colors.CYAN, output)
            mock_stdout.truncate(0)
            mock_stdout.seek(0)

    def test_inherits_from_table(self):
        """Test that ColoredTable inherits from Table."""
        from colorterminal.tables.base import Table

        table = ColoredTable(headers=["Col1"])
        self.assertIsInstance(table, Table)

    @patch("sys.stdout", new_callable=StringIO)
    def test_mixed_colored_and_default_rows(self, mock_stdout):
        """Test mixing explicitly colored and default rows."""
        table = ColoredTable(
            headers=["Name"], alternating_colors=[None, Colors.BRIGHT_BLACK]
        )
        table.add_row(["Alice"], color=Colors.RED)
        table.add_row(["Bob"])  # Will use alternating color
        table.add_row(["Charlie"])  # Will use alternating color
        table.display()
        output = mock_stdout.getvalue()
        self.assertIn(Colors.RED, output)
        self.assertIn(Colors.BRIGHT_BLACK, output)
