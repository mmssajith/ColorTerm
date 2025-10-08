"""Integration tests for full ColorTerm workflows."""

import unittest
from io import StringIO
from unittest.mock import patch
from colorterminal import (
    Printer, StylePrinter, SemanticPrinter,
    ProgressBar, AnimatedProgressBar, MultiProgressBar, SpinnerProgressBar,
    Table, ColoredTable, Grid,
    Line, Rectangle, Circle, Triangle, Diamond, Box,
    Colors, Styles
)


class TestFullWorkflow(unittest.TestCase):
    """Test complete ColorTerm workflows."""

    @patch('sys.stdout', new_callable=StringIO)
    def test_combined_features(self, mock_stdout):
        """Test using multiple features together."""
        # Test printers together
        Printer.red("Error occurred")
        StylePrinter.bold("Important message")
        SemanticPrinter.success("Operation completed")

        output = mock_stdout.getvalue()
        self.assertIn("Error occurred", output)
        self.assertIn("Important message", output)
        self.assertIn("Operation completed", output)
        self.assertIn(Colors.RED, output)
        self.assertIn(Styles.BOLD, output)
        self.assertIn(Colors.GREEN, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_table_and_shapes_together(self, mock_stdout):
        """Test combining tables and shapes."""
        # Create and display a table
        table = Table(headers=["Feature", "Status"])
        table.add_row(["Tables", "Working"])
        table.add_row(["Shapes", "Working"])
        table.display()

        # Create a box around some content
        box = Box(width=30, height=3, title="Summary")
        box.draw()

        output = mock_stdout.getvalue()
        self.assertIn("Feature", output)
        self.assertIn("Status", output)
        self.assertIn("Summary", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_progress_bars_workflow(self, mock_stdout):
        """Test progress bar workflow."""
        # Create multiple progress bars
        multi = MultiProgressBar()
        multi.add_bar("Download", total=100, color_code=Colors.GREEN)
        multi.add_bar("Upload", total=50, color_code=Colors.BLUE)

        multi.update("Download", 50)
        multi.update("Upload", 25)

        multi.display_all()

        output = mock_stdout.getvalue()
        self.assertIn("Download", output)
        self.assertIn("Upload", output)
        self.assertIn("Progress Status", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_colored_table_with_semantic_messages(self, mock_stdout):
        """Test colored table with semantic messages."""
        SemanticPrinter.info("Creating report...")

        table = ColoredTable(headers=["Name", "Score", "Grade"])
        table.add_row(["Alice", "95", "A"], color=Colors.GREEN)
        table.add_row(["Bob", "85", "B"], color=Colors.BLUE)
        table.add_row(["Charlie", "75", "C"], color=Colors.YELLOW)
        table.display()

        SemanticPrinter.success("Report created successfully")

        output = mock_stdout.getvalue()
        self.assertIn("Creating report", output)
        self.assertIn("Alice", output)
        self.assertIn("Report created successfully", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_shapes_gallery(self, mock_stdout):
        """Test creating a gallery of shapes."""
        shapes = [
            Line(length=20, orientation="horizontal"),
            Rectangle(width=10, height=3, filled=True),
            Triangle(height=3, orientation="up"),
            Diamond(size=3, filled=True),
        ]

        for shape in shapes:
            shape.draw()

        output = mock_stdout.getvalue()
        # Should have output from all shapes
        self.assertGreater(len(output), 0)
        # Check for ANSI codes
        self.assertIn(Colors.RESET, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_complex_rendering(self, mock_stdout):
        """Test complex rendering scenarios."""
        # Title
        StylePrinter.bold("System Status Report")

        # Status messages
        SemanticPrinter.success("Database: Online")
        SemanticPrinter.warning("Cache: Low memory")
        SemanticPrinter.error("API: Timeout")

        # Statistics table
        table = Table(
            headers=["Service", "Uptime", "Requests"],
            alignment=["left", "center", "right"]
        )
        table.add_row(["API Gateway", "99.9%", "1,234,567"])
        table.add_row(["Database", "100%", "987,654"])
        table.add_row(["Cache", "98.5%", "543,210"])
        table.display()

        # Decorative box
        box = Box(width=40, height=2, style="double", title="Summary")
        box.draw()

        output = mock_stdout.getvalue()
        self.assertIn("System Status Report", output)
        self.assertIn("Database: Online", output)
        self.assertIn("API Gateway", output)
        self.assertIn("Summary", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_grid_with_different_content(self, mock_stdout):
        """Test grid with various content types."""
        grid = Grid(columns=3, cell_width=15, cell_height=2, style="rounded")

        grid.add_cell("Item 1")
        grid.add_cell(["Multi", "Line"])
        grid.add_cell("Item 3")
        grid.add_cell("Item 4")
        grid.add_cell("Item 5")
        grid.add_cell(["Another", "Multi-line"])

        grid.display()

        output = mock_stdout.getvalue()
        self.assertIn("Item 1", output)
        self.assertIn("Multi", output)
        self.assertIn("Item 3", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_printer_types(self, mock_stdout):
        """Test all printer types in sequence."""
        # Base printers
        Printer.red("Red text")
        Printer.green("Green text")
        Printer.blue("Blue text")

        # Style printers
        StylePrinter.bold("Bold text")
        StylePrinter.underline("Underlined text")
        StylePrinter.bold_yellow("Bold yellow text")

        # Semantic printers
        SemanticPrinter.success("Success message")
        SemanticPrinter.error("Error message")
        SemanticPrinter.warning("Warning message")
        SemanticPrinter.info("Info message")

        output = mock_stdout.getvalue()
        self.assertIn("Red text", output)
        self.assertIn("Bold text", output)
        self.assertIn("Success message", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_shape_types(self, mock_stdout):
        """Test all shape types."""
        shapes = {
            "line": Line(length=10),
            "rectangle": Rectangle(width=5, height=3),
            "circle": Circle(radius=3),
            "triangle": Triangle(height=3),
            "diamond": Diamond(size=3),
            "box": Box(width=10, height=2)
        }

        for name, shape in shapes.items():
            shape.draw()

        output = mock_stdout.getvalue()
        # All shapes should produce some output
        self.assertGreater(len(output), 100)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_table_types(self, mock_stdout):
        """Test all table types."""
        # Standard table
        table1 = Table(headers=["Col1", "Col2"])
        table1.add_row(["A", "B"])
        table1.display()

        # Colored table
        table2 = ColoredTable(headers=["Name", "Value"])
        table2.add_row(["Test", "123"], color=Colors.GREEN)
        table2.display()

        # Grid
        grid = Grid(columns=2, cell_width=10, cell_height=2)
        grid.add_cell("Cell 1")
        grid.add_cell("Cell 2")
        grid.display()

        output = mock_stdout.getvalue()
        self.assertIn("Col1", output)
        self.assertIn("Name", output)
        self.assertIn("Cell 1", output)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('time.sleep')
    def test_progress_bar_types(self, mock_sleep, mock_stdout):
        """Test different progress bar types."""
        # Basic progress bar
        bar1 = ProgressBar(total=100)
        bar1.update(50)

        # Animated progress bar
        bar2 = AnimatedProgressBar(total=100)
        bar2.update(75)

        # Spinner progress bar
        bar3 = SpinnerProgressBar(total=100, spinner_style="dots")
        bar3.update(25)

        # Multi progress bar
        multi = MultiProgressBar()
        multi.add_bar("Task 1", total=100)
        multi.update("Task 1", 50)
        multi.display_all()

        output = mock_stdout.getvalue()
        self.assertIn("50.00%", output)
        self.assertIn("Task 1", output)

    def test_colors_and_styles_constants(self):
        """Test that all color and style constants are accessible."""
        # Test basic colors
        self.assertIsNotNone(Colors.RED)
        self.assertIsNotNone(Colors.GREEN)
        self.assertIsNotNone(Colors.BLUE)

        # Test bright colors
        self.assertIsNotNone(Colors.BRIGHT_RED)
        self.assertIsNotNone(Colors.BRIGHT_GREEN)

        # Test styles
        self.assertIsNotNone(Styles.BOLD)
        self.assertIsNotNone(Styles.UNDERLINE)
        self.assertIsNotNone(Styles.ITALIC)

    @patch('sys.stdout', new_callable=StringIO)
    def test_realistic_dashboard_scenario(self, mock_stdout):
        """Test a realistic dashboard scenario."""
        # Header
        box = Box(width=50, height=1, style="double", title="System Dashboard")
        box.draw()

        # System status
        SemanticPrinter.info("System Status:")
        SemanticPrinter.success("CPU: Normal")
        SemanticPrinter.warning("Memory: 75% used")
        SemanticPrinter.error("Disk: 90% full")

        # Services table
        table = ColoredTable(headers=["Service", "Status", "Uptime"])
        table.add_row(["Web Server", "Running", "99.9%"], color=Colors.GREEN)
        table.add_row(["Database", "Running", "100%"], color=Colors.GREEN)
        table.add_row(["Cache", "Degraded", "95%"], color=Colors.YELLOW)
        table.display()

        # Progress indicators
        multi = MultiProgressBar()
        multi.add_bar("CPU", total=100, color_code=Colors.GREEN)
        multi.add_bar("Memory", total=100, color_code=Colors.YELLOW)
        multi.add_bar("Disk", total=100, color_code=Colors.RED)
        multi.update("CPU", 45)
        multi.update("Memory", 75)
        multi.update("Disk", 90)
        multi.display_all()

        output = mock_stdout.getvalue()
        self.assertIn("System Dashboard", output)
        self.assertIn("CPU: Normal", output)
        self.assertIn("Web Server", output)
        self.assertIn("Progress Status", output)
