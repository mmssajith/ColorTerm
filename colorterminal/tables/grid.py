"""
Grid class for simple grid layouts.
"""

from .. import Colors, colorize
from .base import Table


class Grid:
    """Simple grid layout for displaying data in a grid format."""

    def __init__(
        self,
        columns=3,
        cell_width=20,
        cell_height=3,
        style="light",
        color_code=Colors.WHITE,
    ):
        """
        Initialize a grid.

        Args:
            columns: Number of columns in the grid
            cell_width: Width of each cell
            cell_height: Height of each cell (in lines)
            style: Border style
            color_code: ANSI color code for borders
        """
        self.columns = columns
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.style = style.lower()
        self.color_code = color_code
        self.cells = []

        if self.style not in Table.BORDER_STYLES:
            raise ValueError(
                f"Style must be one of: {', '.join(Table.BORDER_STYLES.keys())}"
            )

        self.chars = Table.BORDER_STYLES[self.style]

    def add_cell(self, content):
        """
        Add a cell to the grid.

        Args:
            content: Content for the cell (string or list of strings)
        """
        if isinstance(content, str):
            content = [content]
        self.cells.append(content)

    def display(self):
        """Display the grid."""
        if not self.cells:
            return

        # Calculate number of rows needed
        num_rows = (len(self.cells) + self.columns - 1) // self.columns

        for row_idx in range(num_rows):
            # Draw top border (for first row) or separator
            if row_idx == 0:
                self._draw_horizontal_line("top")
            else:
                self._draw_horizontal_line("middle")

            # Draw cell content
            for line_idx in range(self.cell_height):
                line_parts = []

                for col_idx in range(self.columns):
                    cell_idx = row_idx * self.columns + col_idx

                    if cell_idx < len(self.cells):
                        cell_content = self.cells[cell_idx]
                        if line_idx < len(cell_content):
                            text = cell_content[line_idx][: self.cell_width]
                        else:
                            text = ""
                    else:
                        text = ""

                    # Pad text to cell width
                    text = text.ljust(self.cell_width)
                    line_parts.append(text)

                # Print the line
                v = colorize(self.chars["v"], self.color_code)
                print(v + v.join([" " + part + " " for part in line_parts]) + v)

        # Draw bottom border
        self._draw_horizontal_line("bottom")

    def _draw_horizontal_line(self, position):
        """
        Draw a horizontal line.

        Args:
            position: 'top', 'middle', or 'bottom'
        """
        if position == "top":
            left = self.chars["tl"]
            middle = self.chars["top"]
            right = self.chars["tr"]
        elif position == "bottom":
            left = self.chars["bl"]
            middle = self.chars["bottom"]
            right = self.chars["br"]
        else:  # middle
            left = self.chars["left"]
            middle = self.chars["cross"]
            right = self.chars["right"]

        parts = [self.chars["h"] * (self.cell_width + 2)] * self.columns
        line = left + middle.join(parts) + right
        print(colorize(line, self.color_code))
