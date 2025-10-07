"""
ColorTerm - A simple library for colored terminal output using ANSI escape codes.

This library provides easy-to-use functions for printing colored and styled text
to the terminal without needing to remember ANSI escape codes.
"""


class Colors:
    """ANSI color codes for terminal output."""
    # Reset
    RESET = '\033[0m'

    # Regular colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'


class Styles:
    """ANSI style codes for terminal output."""
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKETHROUGH = '\033[9m'


def colorize(text, color_code):
    """Apply a color code to text and reset afterwards."""
    return f"{color_code}{text}{Colors.RESET}"


def stylize(text, *style_codes):
    """Apply one or more style codes to text."""
    styles = ''.join(style_codes)
    return f"{styles}{text}{Colors.RESET}"


# Basic color print functions
def print_red(text, **kwargs):
    """Print text in red."""
    print(colorize(text, Colors.RED), **kwargs)


def print_green(text, **kwargs):
    """Print text in green."""
    print(colorize(text, Colors.GREEN), **kwargs)


def print_yellow(text, **kwargs):
    """Print text in yellow."""
    print(colorize(text, Colors.YELLOW), **kwargs)


def print_blue(text, **kwargs):
    """Print text in blue."""
    print(colorize(text, Colors.BLUE), **kwargs)


def print_magenta(text, **kwargs):
    """Print text in magenta."""
    print(colorize(text, Colors.MAGENTA), **kwargs)


def print_cyan(text, **kwargs):
    """Print text in cyan."""
    print(colorize(text, Colors.CYAN), **kwargs)


def print_white(text, **kwargs):
    """Print text in white."""
    print(colorize(text, Colors.WHITE), **kwargs)


# Bright color print functions
def print_bright_red(text, **kwargs):
    """Print text in bright red."""
    print(colorize(text, Colors.BRIGHT_RED), **kwargs)


def print_bright_green(text, **kwargs):
    """Print text in bright green."""
    print(colorize(text, Colors.BRIGHT_GREEN), **kwargs)


def print_bright_yellow(text, **kwargs):
    """Print text in bright yellow."""
    print(colorize(text, Colors.BRIGHT_YELLOW), **kwargs)


def print_bright_blue(text, **kwargs):
    """Print text in bright blue."""
    print(colorize(text, Colors.BRIGHT_BLUE), **kwargs)


# Semantic/contextual print functions
def print_success(text, **kwargs):
    """Print success message in green."""
    print(colorize(f"✓ {text}", Colors.GREEN), **kwargs)


def print_error(text, **kwargs):
    """Print error message in red."""
    print(colorize(f"✗ {text}", Colors.RED), **kwargs)


def print_warning(text, **kwargs):
    """Print warning message in yellow."""
    print(colorize(f"⚠ {text}", Colors.YELLOW), **kwargs)


def print_info(text, **kwargs):
    """Print info message in cyan."""
    print(colorize(f"ℹ {text}", Colors.CYAN), **kwargs)


# Style print functions
def print_bold(text, **kwargs):
    """Print text in bold."""
    print(stylize(text, Styles.BOLD), **kwargs)


def print_underline(text, **kwargs):
    """Print text underlined."""
    print(stylize(text, Styles.UNDERLINE), **kwargs)


def print_italic(text, **kwargs):
    """Print text in italic."""
    print(stylize(text, Styles.ITALIC), **kwargs)


# Combined style and color functions
def print_bold_red(text, **kwargs):
    """Print text in bold red."""
    print(stylize(text, Styles.BOLD, Colors.RED), **kwargs)


def print_bold_green(text, **kwargs):
    """Print text in bold green."""
    print(stylize(text, Styles.BOLD, Colors.GREEN), **kwargs)


def print_bold_yellow(text, **kwargs):
    """Print text in bold yellow."""
    print(stylize(text, Styles.BOLD, Colors.YELLOW), **kwargs)
