import dataclasses


class ColorPyState:
    def __init__(self, italic=False, bold=False, underline=False,
                 strikethrough=False, foreground_color=None,
                 background_color=None):
        self.italic = italic
        self.bold = bold
        self.underline = underline
        self.strikethrough = strikethrough
        self.foreground_color = foreground_color
        self.background_color = background_color
        self.reset = False

    def set_reset(self, value):
        self.reset = value
        return self

    def set_italic(self, italic):
        self.italic = italic
        return self

    def set_strikethrough(self, strikethrough):
        self.strikethrough = strikethrough
        return self

    def set_bold(self, bold):
        self.bold = bold
        return self

    def set_underline(self, underline):
        self.underline = underline
        return self

    def set_foreground_color(self, foreground_color):
        self.foreground_color = foreground_color
        return self

    def set_background_color(self, background_color):

        self.background_color = background_color
        return self

    def run(self, text):
        t = ""
        if self.bold:
            t += f"\x1b[1m"
        if self.italic:
            t += f"\x1b[3m"
        if self.underline:
            t += f"\x1b[4m"
        if self.strikethrough:
            t += f"\x1b[9m"
        if self.background_color:
            r, g, b = self.background_color
            c = f"2;{r};{g};{b}"
            t += f"\x1b[48;{c}m"

        if self.foreground_color:
            r, g, b = self.foreground_color
            c = f"2;{r};{g};{b}"
            t += f"\x1b[38;{c}m"
        if self.reset:
            reset_code = "\x1b[0m"
            t = f"{reset_code}{t}"
        return f"{t}{text}\x1b[0m"

    __call__ = run


class CustomPrint:
    def __init__(self, custom_printer_state_transformer):
        self.state_transformer = custom_printer_state_transformer

    def run(self, text):
        p = ColorPyState(
                         italic=False,
                         bold=False,
                         underline=False,
                         strikethrough=False,
                         background_color=None,
                         foreground_color=None

                         )
        return self.state_transformer(p)
