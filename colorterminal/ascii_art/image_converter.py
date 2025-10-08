"""Convert images to colored ASCII art."""

from .. import Colors, colorize


class ImageToASCII:
    """Convert images to ASCII art with colors."""

    # ASCII characters from darkest to lightest
    ASCII_CHARS = " .:-=+*#%@"
    ASCII_CHARS_DETAILED = (
        " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    )

    def __init__(self, width=100, detailed=False):
        """
        Initialize ASCII art converter.

        Args:
            width: Output width in characters
            detailed: Use detailed character set for better quality
        """
        self.width = width
        self.chars = self.ASCII_CHARS_DETAILED if detailed else self.ASCII_CHARS

    def _get_ascii_char(self, brightness):
        """
        Get ASCII character based on brightness (0-255).

        Args:
            brightness: Brightness value (0-255)

        Returns:
            ASCII character
        """
        index = int(brightness / 255 * (len(self.chars) - 1))
        return self.chars[index]

    def _rgb_to_ansi_color(self, r, g, b):
        """
        Convert RGB to closest ANSI color code.

        Args:
            r, g, b: RGB values (0-255)

        Returns:
            ANSI color code
        """
        # Simple mapping to 8 basic colors
        brightness = (int(r) + int(g) + int(b)) / 3

        if r > g and r > b:
            return Colors.RED if brightness < 128 else Colors.BRIGHT_RED
        elif g > r and g > b:
            return Colors.GREEN if brightness < 128 else Colors.BRIGHT_GREEN
        elif b > r and b > g:
            return Colors.BLUE if brightness < 128 else Colors.BRIGHT_BLUE
        elif r > 150 and g > 150 and b < 100:
            return Colors.YELLOW if brightness < 128 else Colors.BRIGHT_YELLOW
        elif r > 150 and b > 150 and g < 100:
            return Colors.MAGENTA if brightness < 128 else Colors.BRIGHT_MAGENTA
        elif g > 150 and b > 150 and r < 100:
            return Colors.CYAN if brightness < 128 else Colors.BRIGHT_CYAN
        elif brightness > 200:
            return Colors.WHITE
        elif brightness < 50:
            return Colors.BLACK
        else:
            return Colors.WHITE

    def convert_from_array(self, image_array, colored=True):
        """
        Convert image array to ASCII art.

        Args:
            image_array: 2D or 3D numpy array (grayscale or RGB)
            colored: Whether to colorize the output

        Returns:
            ASCII art as string
        """
        try:
            import numpy as np
        except ImportError as err:
            raise ImportError(
                "NumPy is required for image conversion. Install it with: pip install numpy"
            ) from err

        height, width = image_array.shape[:2]
        aspect_ratio = height / width
        new_height = int(self.width * aspect_ratio * 0.5)  # 0.5 for character aspect

        # Resize logic (simple nearest neighbor)
        y_indices = (np.arange(new_height) * height / new_height).astype(int)
        x_indices = (np.arange(self.width) * width / self.width).astype(int)

        result = []
        for y in y_indices:
            line = ""
            for x in x_indices:
                pixel = image_array[y, x]

                if len(image_array.shape) == 3:  # RGB image
                    r, g, b = pixel[:3]
                    brightness = int(0.299 * r + 0.587 * g + 0.114 * b)
                else:  # Grayscale
                    brightness = int(pixel)
                    r = g = b = brightness

                char = self._get_ascii_char(brightness)

                if colored:
                    color = self._rgb_to_ansi_color(r, g, b)
                    line += colorize(char, color)
                else:
                    line += char

            result.append(line)

        return "\n".join(result)

    def convert_from_file(self, image_path, colored=True):
        """
        Convert image file to ASCII art.

        Args:
            image_path: Path to image file
            colored: Whether to colorize the output

        Returns:
            ASCII art as string
        """
        try:
            import numpy as np
            from PIL import Image
        except ImportError as err:
            raise ImportError(
                "Pillow is required for image file conversion. "
                "Install it with: pip install Pillow"
            ) from err

        # Open and convert image
        img = Image.open(image_path)
        img_array = np.array(img)

        return self.convert_from_array(img_array, colored=colored)

    def display_from_file(self, image_path, colored=True):
        """
        Display ASCII art from image file.

        Args:
            image_path: Path to image file
            colored: Whether to colorize the output
        """
        ascii_art = self.convert_from_file(image_path, colored=colored)
        print(ascii_art)

    def display_from_array(self, image_array, colored=True):
        """
        Display ASCII art from image array.

        Args:
            image_array: 2D or 3D numpy array
            colored: Whether to colorize the output
        """
        ascii_art = self.convert_from_array(image_array, colored=colored)
        print(ascii_art)
