"""
ColoredTable class with row coloring support.
"""

from .. import Colors
from .base import Table


class ColoredTable(Table):
    """Table with colored rows support."""

    def __init__(
        self,
        headers=None,
        style="light",
        color_code=Colors.WHITE,
        header_color=Colors.BRIGHT_CYAN,
        padding=1,
        alignment=None,
        alternating_colors=None,
    ):
        """
        Initialize a colored table.

        Args:
            headers: List of column headers
            style: Border style
            color_code: ANSI color code for borders
            header_color: ANSI color code for headers
            padding: Cell padding
            alignment: List of alignment per column
            alternating_colors: List of two colors for alternating row colors
        """
        super().__init__(headers, style, color_code, header_color, padding, alignment)
        self.alternating_colors = alternating_colors or [None, Colors.BRIGHT_BLACK]
        self.row_colors = []

    def add_row(self, row, color=None):
        """
        Add a row with optional color.

        Args:
            row: List of cell values
            color: Optional color for this row
        """
        super().add_row(row)
        self.row_colors.append(color)

    def display(self):
        """Display the table with colored rows."""
        if not self.headers:
            return

        self._calculate_widths()

        # Top border
        self._draw_separator(self.chars["tl"], self.chars["top"], self.chars["tr"])

        # Header row
        if self.headers:
            self._draw_row(self.headers, self.header_color)

        # Header separator
        if self.rows:
            self._draw_separator(
                self.chars["left"], self.chars["cross"], self.chars["right"]
            )

        # Data rows
        for i, row in enumerate(self.rows):
            # Determine row color
            if i < len(self.row_colors) and self.row_colors[i] is not None:
                row_color = self.row_colors[i]
            elif self.alternating_colors:
                row_color = self.alternating_colors[i % len(self.alternating_colors)]
            else:
                row_color = None

            # Ensure row has same number of columns as headers
            row_data = row + [""] * (len(self.headers) - len(row))
            self._draw_row(row_data, row_color)

        # Bottom border
        self._draw_separator(self.chars["bl"], self.chars["bottom"], self.chars["br"])
