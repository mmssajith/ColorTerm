# ColorTerm 🎨

A comprehensive Python library for colored terminal output, progress bars, tables, and shapes using ANSI escape codes. Perfect for making your CLI applications more readable, interactive, and user-friendly!

## Features

### 🎨 Text Output
- **Basic Colors**: 8 standard colors + 8 bright colors
- **Text Styles**: Bold, italic, underline, and more
- **Semantic Printers**: Success, error, warning, info with icons (✓, ✗, ⚠, ℹ)

### 📊 Progress Bars
- **ProgressBar**: Static progress bar with customizable appearance
- **AnimatedProgressBar**: Smooth animated progress with transitions
- **SpinnerProgressBar**: Progress with spinner animations (dots, line, arrow, circle)
- **MultiProgressBar**: Display multiple progress bars simultaneously

### 📋 Tables
- **Table**: Basic tables with headers, rows, and alignment
- **ColoredTable**: Tables with row coloring and alternating colors
- **Grid**: Grid layout for cell-based content
- **5 Border Styles**: Light, heavy, double, rounded, ASCII

### 🔷 Shapes
- **Line**: Horizontal and vertical lines
- **Rectangle**: Filled or bordered rectangles
- **Circle**: Filled or bordered circles
- **Triangle**: Triangles in 4 orientations (up, down, left, right)
- **Diamond**: Diamond shapes
- **Box**: Unicode boxes with titles and multiple styles

## Installation

```bash
pip install terminal-colorize
```

Or install from source:

```bash
git clone https://github.com/mmssajith/colorterm.git
cd colorterm
pip install -e .
```

## Quick Start

### Colored Text

```python
from colorterminal import Printer, StylePrinter, SemanticPrinter

# Basic colors
Printer.red("Error message")
Printer.green("Success message")
Printer.blue("Information")

# Text styles
StylePrinter.bold("Bold text")
StylePrinter.underline("Underlined text")
StylePrinter.bold_red("Bold red text")

# Semantic messages with icons
SemanticPrinter.success("Operation completed")  # ✓
SemanticPrinter.error("Connection failed")      # ✗
SemanticPrinter.warning("Low disk space")       # ⚠
SemanticPrinter.info("Processing data")         # ℹ
```

### Progress Bars

```python
from colorterminal import AnimatedProgressBar, MultiProgressBar, Colors

# Single animated progress bar
bar = AnimatedProgressBar(total=100, color_code=Colors.GREEN)
bar.simulate(duration=2, steps=50)

# Multiple progress bars
multi = MultiProgressBar()
multi.add_bar("Download", total=100, color_code=Colors.GREEN)
multi.add_bar("Upload", total=100, color_code=Colors.BLUE)
multi.update("Download", 75)
multi.update("Upload", 45)
multi.display_all()
```

### Tables

```python
from colorterminal import Table, ColoredTable, Colors

# Basic table
table = Table(headers=["Name", "Age", "City"])
table.add_row(["Alice", "30", "New York"])
table.add_row(["Bob", "25", "San Francisco"])
table.display()

# Colored table with row colors
table = ColoredTable(headers=["Test", "Result", "Time"])
table.add_row(["Test 1", "PASSED", "0.5s"], color=Colors.GREEN)
table.add_row(["Test 2", "FAILED", "1.2s"], color=Colors.RED)
table.display()
```

### Shapes

```python
from colorterminal import Line, Rectangle, Circle, Box, Colors

# Draw a line
Line(length=40, color_code=Colors.CYAN).draw()

# Draw a rectangle
Rectangle(width=20, height=5, color_code=Colors.GREEN).draw()

# Draw a circle
Circle(radius=5, filled=True, color_code=Colors.MAGENTA).draw()

# Draw a box with title
Box(width=40, height=3, title="Status", style="double").draw()
```

## Complete Examples

### Dashboard Example

```python
from colorterminal import (
    Box, ColoredTable, MultiProgressBar,
    SemanticPrinter, StylePrinter, Colors
)

# Header
Box(width=60, height=1, style="double", title="System Dashboard").draw()

# System status
StylePrinter.bold("System Status:")
SemanticPrinter.success("CPU: Normal (45%)")
SemanticPrinter.warning("Memory: High (85%)")
SemanticPrinter.error("Disk: Critical (92%)")

# Services table
table = ColoredTable(headers=["Service", "Status", "Uptime"])
table.add_row(["Web Server", "Running", "99.9%"], color=Colors.GREEN)
table.add_row(["Database", "Running", "100%"], color=Colors.GREEN)
table.add_row(["Cache", "Degraded", "98.5%"], color=Colors.YELLOW)
table.display()

# Resource usage
multi = MultiProgressBar()
multi.add_bar("CPU", total=100, color_code=Colors.GREEN)
multi.add_bar("Memory", total=100, color_code=Colors.YELLOW)
multi.add_bar("Disk", total=100, color_code=Colors.RED)
multi.update("CPU", 45)
multi.update("Memory", 85)
multi.update("Disk", 92)
multi.display_all()
```

## API Reference

### Printers

**Printer** - Basic colored text output
- `Printer.red()`, `Printer.green()`, `Printer.blue()`, etc.
- `Printer.bright_red()`, `Printer.bright_green()`, etc.

**StylePrinter** - Styled and combined text
- `StylePrinter.bold()`, `StylePrinter.underline()`, `StylePrinter.italic()`
- `StylePrinter.bold_red()`, `StylePrinter.bold_green()`, etc.

**SemanticPrinter** - Contextual messages with icons
- `SemanticPrinter.success()` - Green with ✓
- `SemanticPrinter.error()` - Red with ✗
- `SemanticPrinter.warning()` - Yellow with ⚠
- `SemanticPrinter.info()` - Cyan with ℹ

### Progress Bars

**ProgressBar** - Basic progress bar
```python
bar = ProgressBar(total=100, width=40, color_code=Colors.GREEN)
bar.update(50)
```

**AnimatedProgressBar** - Animated progress
```python
bar = AnimatedProgressBar(total=100)
bar.animate_to(75, steps=20, delay=0.05)
bar.simulate(duration=2, steps=50)
```

**SpinnerProgressBar** - Progress with spinner
```python
bar = SpinnerProgressBar(total=100, spinner_style="dots")
bar.update(50)
```

**MultiProgressBar** - Multiple bars
```python
multi = MultiProgressBar()
multi.add_bar("Task 1", total=100, color_code=Colors.GREEN)
multi.update("Task 1", 50)
multi.display_all()
```

### Tables

**Table** - Basic table
```python
table = Table(
    headers=["Col1", "Col2"],
    style="light",  # light, heavy, double, rounded, ascii
    alignment=["left", "center"]
)
table.add_row(["Data 1", "Data 2"])
table.display()
```

**ColoredTable** - Table with colors
```python
table = ColoredTable(
    headers=["Name", "Status"],
    alternating_colors=[None, Colors.BRIGHT_BLACK]
)
table.add_row(["Item 1", "Active"], color=Colors.GREEN)
table.display()
```

**Grid** - Grid layout
```python
grid = Grid(columns=3, cell_width=15, cell_height=2)
grid.add_cell("Cell 1")
grid.add_cell(["Multi", "Line"])
grid.display()
```

### Shapes

**Line**
```python
Line(length=40, orientation="horizontal", color_code=Colors.CYAN).draw()
```

**Rectangle**
```python
Rectangle(width=20, height=5, filled=True, color_code=Colors.GREEN).draw()
```

**Circle**
```python
Circle(radius=5, filled=False, color_code=Colors.MAGENTA).draw()
```

**Triangle**
```python
Triangle(height=5, orientation="up", color_code=Colors.YELLOW).draw()
```

**Diamond**
```python
Diamond(size=5, filled=True, color_code=Colors.CYAN).draw()
```

**Box**
```python
Box(width=40, height=3, style="double", title="Title").draw()
```

## Examples

Check the `examples/` directory for complete examples:
- `basic_example.py` - Text output basics
- `shapes_example.py` - All shape types
- `tables_example.py` - Table demonstrations
- `progress_example.py` - Progress bar examples
- `dashboard_example.py` - Complete dashboard

Run any example:
```bash
python examples/basic_example.py
```

## Colors & Styles

### Available Colors
```python
Colors.RED, Colors.GREEN, Colors.BLUE, Colors.YELLOW
Colors.MAGENTA, Colors.CYAN, Colors.WHITE, Colors.BLACK
Colors.BRIGHT_RED, Colors.BRIGHT_GREEN, Colors.BRIGHT_BLUE
Colors.BRIGHT_YELLOW, Colors.BRIGHT_MAGENTA, Colors.BRIGHT_CYAN
```

### Available Styles
```python
Styles.BOLD, Styles.ITALIC, Styles.UNDERLINE
Styles.DIM, Styles.BLINK, Styles.REVERSE, Styles.STRIKETHROUGH
```

### Manual Colorization
```python
from colorterminal import colorize, stylize, Colors, Styles

print(colorize("Custom text", Colors.MAGENTA))
print(stylize("Styled text", Styles.BOLD, Styles.UNDERLINE, Colors.CYAN))
```

## Compatibility

- ✅ Linux
- ✅ macOS
- ✅ Windows 10+ (with ANSI support)

## Requirements

- Python 3.6+
- No external dependencies

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Links

- GitHub: https://github.com/mmssajith/colorterm
- PyPI: https://pypi.org/project/terminal-colorize/
- Issues: https://github.com/mmssajith/colorterm/issues
