"""
Base Table class for formatted table output.
"""

from .. import Colors, colorize


class Table:
    """Create formatted tables with borders, alignment, and colors."""

    # Border styles using Unicode box-drawing characters
    BORDER_STYLES = {
        "light": {
            "tl": "┌",
            "tr": "┐",
            "bl": "└",
            "br": "┘",
            "h": "─",
            "v": "│",
            "cross": "┼",
            "top": "┬",
            "bottom": "┴",
            "left": "├",
            "right": "┤",
        },
        "heavy": {
            "tl": "┏",
            "tr": "┓",
            "bl": "┗",
            "br": "┛",
            "h": "━",
            "v": "┃",
            "cross": "╋",
            "top": "┳",
            "bottom": "┻",
            "left": "┣",
            "right": "┫",
        },
        "double": {
            "tl": "╔",
            "tr": "╗",
            "bl": "╚",
            "br": "╝",
            "h": "═",
            "v": "║",
            "cross": "╬",
            "top": "╦",
            "bottom": "╩",
            "left": "╠",
            "right": "╣",
        },
        "rounded": {
            "tl": "╭",
            "tr": "╮",
            "bl": "╰",
            "br": "╯",
            "h": "─",
            "v": "│",
            "cross": "┼",
            "top": "┬",
            "bottom": "┴",
            "left": "├",
            "right": "┤",
        },
        "ascii": {
            "tl": "+",
            "tr": "+",
            "bl": "+",
            "br": "+",
            "h": "-",
            "v": "|",
            "cross": "+",
            "top": "+",
            "bottom": "+",
            "left": "+",
            "right": "+",
        },
    }

    def __init__(
        self,
        headers=None,
        style="light",
        color_code=Colors.WHITE,
        header_color=Colors.BRIGHT_CYAN,
        padding=1,
        alignment=None,
    ):
        """
        Initialize a table.

        Args:
            headers: List of column headers
            style: Border style ('light', 'heavy', 'double', 'rounded', 'ascii')
            color_code: ANSI color code for borders
            header_color: ANSI color code for headers
            padding: Cell padding (spaces on each side)
            alignment: List of alignment per column ('left', 'center', 'right')
                      If None, defaults to 'left' for all columns
        """
        self.headers = headers or []
        self.style = style.lower()
        self.color_code = color_code
        self.header_color = header_color
        self.padding = padding
        self.rows = []
        self.col_widths = []

        if self.style not in self.BORDER_STYLES:
            raise ValueError(
                f"Style must be one of: {', '.join(self.BORDER_STYLES.keys())}"
            )

        self.chars = self.BORDER_STYLES[self.style]

        # Set alignment
        if alignment is None:
            self.alignment = ["left"] * len(self.headers)
        else:
            self.alignment = alignment
            # Extend with 'left' if not enough alignments specified
            while len(self.alignment) < len(self.headers):
                self.alignment.append("left")

    def add_row(self, row):
        """
        Add a row to the table.

        Args:
            row: List of cell values
        """
        self.rows.append([str(cell) for cell in row])
        self._calculate_widths()

    def add_rows(self, rows):
        """
        Add multiple rows to the table.

        Args:
            rows: List of row lists
        """
        for row in rows:
            self.add_row(row)

    def _calculate_widths(self):
        """Calculate the width needed for each column."""
        # Start with header widths
        self.col_widths = [len(str(h)) for h in self.headers]

        # Check all rows
        for row in self.rows:
            for i, cell in enumerate(row):
                if i < len(self.col_widths):
                    self.col_widths[i] = max(self.col_widths[i], len(str(cell)))
                else:
                    self.col_widths.append(len(str(cell)))

        # Ensure we have widths for all columns
        while len(self.col_widths) < len(self.headers):
            self.col_widths.append(0)

    def _align_text(self, text, width, alignment):
        """
        Align text within a given width.

        Args:
            text: Text to align
            width: Width to align within
            alignment: 'left', 'center', or 'right'

        Returns:
            Aligned text
        """
        text = str(text)
        if alignment == "center":
            return text.center(width)
        elif alignment == "right":
            return text.rjust(width)
        else:  # left or default
            return text.ljust(width)

    def _draw_separator(self, left, middle, right):
        """Draw a horizontal separator line."""
        parts = []
        for width in self.col_widths:
            parts.append(self.chars["h"] * (width + 2 * self.padding))

        line = left + middle.join(parts) + right
        print(colorize(line, self.color_code))

    def _draw_row(self, cells, cell_color=None):
        """Draw a row with cells."""
        # Prepare cells with alignment
        aligned_cells = []
        for i, cell in enumerate(cells):
            width = self.col_widths[i] if i < len(self.col_widths) else 0
            alignment = self.alignment[i] if i < len(self.alignment) else "left"
            aligned = self._align_text(cell, width, alignment)
            aligned_cells.append(aligned)

        # Build the row
        cell_strs = []
        for cell in aligned_cells:
            padded = " " * self.padding + cell + " " * self.padding
            if cell_color:
                padded = colorize(padded, cell_color)
            cell_strs.append(padded)

        v_char = colorize(self.chars["v"], self.color_code)
        line = v_char + v_char.join(cell_strs) + v_char
        print(line)

    def display(self):
        """Display the complete table."""
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
            # Ensure row has same number of columns as headers
            row_data = row + [""] * (len(self.headers) - len(row))
            self._draw_row(row_data)

        # Bottom border
        self._draw_separator(self.chars["bl"], self.chars["bottom"], self.chars["br"])

    def clear(self):
        """Clear all rows from the table."""
        self.rows = []
        self.col_widths = []
