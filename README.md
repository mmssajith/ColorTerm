# ColorTerm 🎨

A simple Python library for printing colored and styled text to the terminal using ANSI escape codes. Perfect for making your CLI applications more readable and user-friendly!

## Features

- 🎨 8 basic colors + 4 bright colors
- ✨ Text styling (bold, italic, underline, etc.)
- 🚦 Semantic functions (`print_success`, `print_error`, `print_warning`, `print_info`)
- 🔧 Manual colorization with `colorize()` and `stylize()`
- 🎯 Simple, intuitive API

## Installation

Install via pip:

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

```python
from colorterminal import *

# Simple colored output
print_green("Operation successful!")
print_red("Error occurred!")

# Semantic messages with icons
print_success("File saved successfully!")
print_error("Failed to connect to server!")
print_warning("Disk space is running low!")
print_info("Processing 100 items...")

# Styled text
print_bold("Important message")
print_underline("Underlined text")

# Combined styles
print_bold_green("Bold green text")
```

## API Reference

### Basic Color Functions

- `print_red(text)` - Print in red
- `print_green(text)` - Print in green
- `print_yellow(text)` - Print in yellow
- `print_blue(text)` - Print in blue
- `print_magenta(text)` - Print in magenta
- `print_cyan(text)` - Print in cyan
- `print_white(text)` - Print in white

### Bright Color Functions

- `print_bright_red(text)`
- `print_bright_green(text)`
- `print_bright_yellow(text)`
- `print_bright_blue(text)`
- And more...

### Semantic Functions

- `print_success(text)` - Green text with ✓ checkmark
- `print_error(text)` - Red text with ✗ cross
- `print_warning(text)` - Yellow text with ⚠ warning sign
- `print_info(text)` - Cyan text with ℹ info icon

### Style Functions

- `print_bold(text)` - Bold text
- `print_italic(text)` - Italic text
- `print_underline(text)` - Underlined text

### Combined Functions

- `print_bold_red(text)`
- `print_bold_green(text)`
- `print_bold_yellow(text)`

### Manual Colorization

For more control, use the `colorize()` and `stylize()` functions:

```python
# Custom color
print(colorize("Custom text", Colors.MAGENTA))

# Multiple styles
print(stylize("Fancy text", Styles.BOLD, Styles.UNDERLINE, Colors.CYAN))

# Mix with regular text
print(f"Status: {colorize('ONLINE', Colors.GREEN)}")
```

### Available Color Codes

Access via the `Colors` class:
- `Colors.RED`, `Colors.GREEN`, `Colors.YELLOW`, `Colors.BLUE`, etc.
- `Colors.BRIGHT_RED`, `Colors.BRIGHT_GREEN`, etc.
- `Colors.BG_RED`, `Colors.BG_GREEN`, etc. (background colors)

### Available Style Codes

Access via the `Styles` class:
- `Styles.BOLD`
- `Styles.ITALIC`
- `Styles.UNDERLINE`
- `Styles.DIM`
- `Styles.BLINK`
- `Styles.REVERSE`
- `Styles.STRIKETHROUGH`

## Examples

Check the `examples/` directory for sample code, or run:

```bash
python examples/example.py
```

### Practical Example

```python
from colorterminal import *

print_info("Starting backup process...")

try:
    # Backup code here
    files_backed_up = 42
    print_success(f"Backup completed! {files_backed_up} files backed up.")
except Exception as e:
    print_error(f"Backup failed: {e}")

print_warning("Remember to verify your backups regularly!")
```

### Status Dashboard Example

```python
from colorterminal import *

print(f"Server Status: {colorize('ONLINE', Colors.GREEN)}")
print(f"Active Users: {colorize('127', Colors.CYAN)}")
print(f"Errors: {colorize('0', Colors.GREEN)}")
print(f"Warnings: {colorize('3', Colors.YELLOW)}")
```

## How It Works

ColorTerm uses ANSI escape codes to color and style terminal text. For example:
- `\033[31m` makes text red
- `\033[1m` makes text bold
- `\033[0m` resets formatting

The library abstracts these codes into easy-to-use functions, so you don't need to remember the codes!

## Compatibility

Works on:
- ✅ Linux
- ✅ macOS
- ✅ Windows (Windows 10+ with ANSI support enabled)

## License

MIT License - see LICENSE file for details.
