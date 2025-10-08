"""Test cases for Base Table."""

import unittest
from io import StringIO
from unittest.mock import patch
from colorterminal import Table, Colors


class TestTable(unittest.TestCase):
    """Test Table base functionality."""

    def test_table_creation(self):
        """Test basic table creation."""
        table = Table(headers=["Name", "Age", "City"])
        self.assertEqual(table.headers, ["Name", "Age", "City"])
        self.assertEqual(table.style, "light")
        self.assertEqual(len(table.rows), 0)

    def test_custom_table_creation(self):
        """Test table with custom parameters."""
        table = Table(
            headers=["Col1", "Col2"],
            style="heavy",
            color_code=Colors.BLUE,
            header_color=Colors.YELLOW,
            padding=2
        )
        self.assertEqual(table.style, "heavy")
        self.assertEqual(table.color_code, Colors.BLUE)
        self.assertEqual(table.header_color, Colors.YELLOW)
        self.assertEqual(table.padding, 2)

    def test_table_styles_available(self):
        """Test that all table styles are available."""
        self.assertIn("light", Table.BORDER_STYLES)
        self.assertIn("heavy", Table.BORDER_STYLES)
        self.assertIn("double", Table.BORDER_STYLES)
        self.assertIn("rounded", Table.BORDER_STYLES)
        self.assertIn("ascii", Table.BORDER_STYLES)

    def test_invalid_style_raises_error(self):
        """Test that invalid style raises ValueError."""
        with self.assertRaises(ValueError):
            Table(headers=["Col1"], style="invalid")

    def test_add_row(self):
        """Test adding a single row."""
        table = Table(headers=["Name", "Age"])
        table.add_row(["Alice", 30])
        self.assertEqual(len(table.rows), 1)
        self.assertEqual(table.rows[0], ["Alice", "30"])

    def test_add_multiple_rows(self):
        """Test adding multiple rows."""
        table = Table(headers=["Name", "Age"])
        table.add_rows([
            ["Alice", 30],
            ["Bob", 25],
            ["Charlie", 35]
        ])
        self.assertEqual(len(table.rows), 3)

    def test_clear_rows(self):
        """Test clearing all rows."""
        table = Table(headers=["Name", "Age"])
        table.add_rows([["Alice", 30], ["Bob", 25]])
        self.assertEqual(len(table.rows), 2)
        table.clear()
        self.assertEqual(len(table.rows), 0)

    def test_column_width_calculation(self):
        """Test that column widths are calculated correctly."""
        table = Table(headers=["Name", "Age"])
        table.add_row(["Alice", 30])
        table.add_row(["VeryLongName", 25])
        table._calculate_widths()
        self.assertGreater(table.col_widths[0], len("Name"))
        self.assertEqual(table.col_widths[0], len("VeryLongName"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_table_display(self, mock_stdout):
        """Test table display."""
        table = Table(headers=["Name", "Age"])
        table.add_row(["Alice", 30])
        table.display()
        output = mock_stdout.getvalue()
        self.assertIn("Name", output)
        self.assertIn("Age", output)
        self.assertIn("Alice", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_table_display(self, mock_stdout):
        """Test displaying empty table does nothing."""
        table = Table()
        table.display()
        output = mock_stdout.getvalue()
        self.assertEqual(output, "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_light_style_borders(self, mock_stdout):
        """Test light style border characters."""
        table = Table(headers=["Col1"], style="light")
        table.display()
        output = mock_stdout.getvalue()
        self.assertIn("┌", output)
        self.assertIn("└", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_heavy_style_borders(self, mock_stdout):
        """Test heavy style border characters."""
        table = Table(headers=["Col1"], style="heavy")
        table.display()
        output = mock_stdout.getvalue()
        self.assertIn("┏", output)
        self.assertIn("┗", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_ascii_style_borders(self, mock_stdout):
        """Test ASCII style border characters."""
        table = Table(headers=["Col1"], style="ascii")
        table.display()
        output = mock_stdout.getvalue()
        self.assertIn("+", output)
        self.assertIn("-", output)

    def test_alignment_left(self):
        """Test left alignment."""
        table = Table(headers=["Name"], alignment=["left"])
        aligned = table._align_text("Test", 10, "left")
        self.assertEqual(aligned, "Test      ")

    def test_alignment_right(self):
        """Test right alignment."""
        table = Table(headers=["Name"], alignment=["right"])
        aligned = table._align_text("Test", 10, "right")
        self.assertEqual(aligned, "      Test")

    def test_alignment_center(self):
        """Test center alignment."""
        table = Table(headers=["Name"], alignment=["center"])
        aligned = table._align_text("Test", 10, "center")
        self.assertEqual(len(aligned), 10)
        self.assertTrue("Test" in aligned)

    def test_default_alignment(self):
        """Test default alignment is left."""
        table = Table(headers=["Col1", "Col2", "Col3"])
        self.assertEqual(table.alignment, ["left", "left", "left"])

    def test_custom_alignment(self):
        """Test custom alignment per column."""
        table = Table(headers=["Col1", "Col2", "Col3"], alignment=["left", "center", "right"])
        self.assertEqual(table.alignment, ["left", "center", "right"])

    @patch('sys.stdout', new_callable=StringIO)
    def test_color_codes_applied(self, mock_stdout):
        """Test that color codes are applied."""
        table = Table(headers=["Name"], color_code=Colors.RED, header_color=Colors.GREEN)
        table.display()
        output = mock_stdout.getvalue()
        self.assertIn(Colors.RED, output)
        self.assertIn(Colors.GREEN, output)

    def test_style_case_insensitive(self):
        """Test style is case insensitive."""
        table = Table(headers=["Col1"], style="HEAVY")
        self.assertEqual(table.style, "heavy")
