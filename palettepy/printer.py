from palettepy.utils import extract_rgb_from_color


class Printer:
    def __init__(self, **kwargs):
        self.italic = False
        self.bold = False
        self.underline = False
        self.strikethrough = False
        self.foreground_color = None
        self.background_color = None

        for i in kwargs:
            setattr(self, i, kwargs[i])

    def run(self):
        text_colors = ""
        if self.foreground_color:
            r, g, b = extract_rgb_from_color(self.foreground_color)
            c = f"2;{r};{g};{b}"
            text_colors += f"\x1b[38;{c}m"

        if self.background_color:
            r, g, b = extract_rgb_from_color(self.background_color)
            c = f"2;{r};{g};{b}"
            text_colors += f"\x1b[48;{c}m"

        if self.italic:
            text_colors += f"\x1b[3m"

        if self.bold:
            text_colors += f"\x1b[1m"

        if self.underline:
            text_colors += f"\x1b[4m"

        if self.strikethrough:
            text_colors += f"\x1b[9m"

        return f"{text_colors}"

    def reset(self):
        return "\x1b[0m"

    def build_config(self):
        return PrinterConfiguration(self)


class PrinterConfiguration:
    def __init__(self, printer: Printer = Printer()):
        self.printer = printer
        self.ansi_enabled = False
