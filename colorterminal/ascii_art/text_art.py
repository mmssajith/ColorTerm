"""Generate ASCII text art with different fonts."""

from .. import colorize


class TextArt:
    """Generate ASCII text art."""

    # Simple 3-line font
    FONT_SIMPLE = {
        "A": ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
        "B": ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "],
        "C": [" CCC ", "C   C", "C    ", "C   C", " CCC "],
        "D": ["DDDD ", "D   D", "D   D", "D   D", "DDDD "],
        "E": ["EEEEE", "E    ", "EEE  ", "E    ", "EEEEE"],
        "F": ["FFFFF", "F    ", "FFF  ", "F    ", "F    "],
        "G": [" GGG ", "G    ", "G  GG", "G   G", " GGG "],
        "H": ["H   H", "H   H", "HHHHH", "H   H", "H   H"],
        "I": ["IIIII", "  I  ", "  I  ", "  I  ", "IIIII"],
        "J": ["JJJJJ", "    J", "    J", "J   J", " JJJ "],
        "K": ["K   K", "K  K ", "KKK  ", "K  K ", "K   K"],
        "L": ["L    ", "L    ", "L    ", "L    ", "LLLLL"],
        "M": ["M   M", "MM MM", "M M M", "M   M", "M   M"],
        "N": ["N   N", "NN  N", "N N N", "N  NN", "N   N"],
        "O": [" OOO ", "O   O", "O   O", "O   O", " OOO "],
        "P": ["PPPP ", "P   P", "PPPP ", "P    ", "P    "],
        "Q": [" QQQ ", "Q   Q", "Q   Q", "Q  Q ", " QQ Q"],
        "R": ["RRRR ", "R   R", "RRRR ", "R  R ", "R   R"],
        "S": [" SSS ", "S    ", " SSS ", "    S", "SSSS "],
        "T": ["TTTTT", "  T  ", "  T  ", "  T  ", "  T  "],
        "U": ["U   U", "U   U", "U   U", "U   U", " UUU "],
        "V": ["V   V", "V   V", "V   V", " V V ", "  V  "],
        "W": ["W   W", "W   W", "W W W", "WW WW", "W   W"],
        "X": ["X   X", " X X ", "  X  ", " X X ", "X   X"],
        "Y": ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  "],
        "Z": ["ZZZZZ", "   Z ", "  Z  ", " Z   ", "ZZZZZ"],
        "0": [" 000 ", "0   0", "0   0", "0   0", " 000 "],
        "1": ["  1  ", " 11  ", "  1  ", "  1  ", "11111"],
        "2": [" 222 ", "2   2", "   2 ", "  2  ", "22222"],
        "3": [" 333 ", "3   3", "  33 ", "3   3", " 333 "],
        "4": ["4   4", "4   4", "44444", "    4", "    4"],
        "5": ["55555", "5    ", "5555 ", "    5", "5555 "],
        "6": [" 666 ", "6    ", "6666 ", "6   6", " 666 "],
        "7": ["77777", "    7", "   7 ", "  7  ", " 7   "],
        "8": [" 888 ", "8   8", " 888 ", "8   8", " 888 "],
        "9": [" 999 ", "9   9", " 9999", "    9", " 999 "],
        " ": ["     ", "     ", "     ", "     ", "     "],
        "!": ["  !  ", "  !  ", "  !  ", "     ", "  !  "],
        "?": [" ??? ", "?   ?", "   ? ", "  ?  ", "     "],
        ".": ["     ", "     ", "     ", "     ", "  .  "],
        ",": ["     ", "     ", "     ", "  ,  ", " ,   "],
    }

    def __init__(self, font="simple"):
        """
        Initialize text art generator.

        Args:
            font: Font style ('simple')
        """
        self.font = self.FONT_SIMPLE if font == "simple" else self.FONT_SIMPLE

    def generate(self, text, color_code=None):
        """
        Generate ASCII art text.

        Args:
            text: Text to convert to ASCII art
            color_code: Optional color code for the text

        Returns:
            ASCII art as string
        """
        text = text.upper()
        lines = [""] * 5  # 5 lines for each character

        for char in text:
            if char not in self.font:
                char = " "  # Default to space for unknown characters

            char_lines = self.font[char]
            for i, line in enumerate(char_lines):
                lines[i] += line + " "

        # Apply color if specified
        result = []
        for line in lines:
            if color_code:
                result.append(colorize(line, color_code))
            else:
                result.append(line)

        return "\n".join(result)

    def display(self, text, color_code=None):
        """
        Display ASCII art text.

        Args:
            text: Text to convert and display
            color_code: Optional color code for the text
        """
        ascii_art = self.generate(text, color_code=color_code)
        print(ascii_art)

    def generate_banner(self, text, border_char="=", color_code=None):
        """
        Generate a banner with ASCII art text.

        Args:
            text: Text for the banner
            border_char: Character to use for borders
            color_code: Optional color code

        Returns:
            Banner as string
        """
        art = self.generate(text, color_code=color_code)
        lines = art.split("\n")
        width = len(lines[0]) if lines else 0

        border = border_char * (width + 4)
        if color_code:
            border = colorize(border, color_code)

        result = [border]
        for line in lines:
            padding = " " * (
                (width - len(line.replace("\033[", "").replace("m", ""))) // 2
            )
            result.append(f"{padding}{line}")
        result.append(border)

        return "\n".join(result)

    def display_banner(self, text, border_char="=", color_code=None):
        """
        Display a banner with ASCII art text.

        Args:
            text: Text for the banner
            border_char: Character to use for borders
            color_code: Optional color code
        """
        banner = self.generate_banner(text, border_char, color_code)
        print(banner)
