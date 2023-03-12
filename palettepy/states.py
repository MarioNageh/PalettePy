# Author: Mario Nageh
# Date: March 12, 2023

import types
from palettepy.palettepy import ColorPyState
from palettepy.utils import extract_rgb_from_color


def color_style_background(color):
    c = extract_rgb_from_color(color)

    def run_color(state=None):
        if type(state) == str:
            r, g, b = c
            return f"\x1b[48;2;{r};{g};{b}m{state}\x1b[0m"


        else:
            if type(state) == types.FunctionType:
                state = state()
            if state:
                state.background_color = c
            else:
                state = ColorPyState(background_color=c)
            return state

    return run_color


def color_style_foreground(color):
    c = extract_rgb_from_color(color)

    def run_color(state=None):
        if type(state) == str:
            r, g, b = c
            return f"\x1b[38;2;{r};{g};{b}m{state}\x1b[0m"
        else:
            if type(state) == types.FunctionType:
                state = state()
            if state:
                state.foreground_color = c
            else:
                state = ColorPyState(foreground_color=c)
            return state

    return run_color


def general_style(attr, value):
    def run_style(state=None):
        if type(state) != ColorPyState:
            if type(state) == str:
                s = ColorPyState()
                if hasattr(s, attr):
                    setattr(s, attr, value)
                return s.run(state)

        if type(state) == types.FunctionType:
            state = state()

        if not state:
            state = ColorPyState()

        if hasattr(state, attr):
            setattr(state, attr, value)
        else:
            raise Exception("Attr Not Found")
        return state

    return run_style


bold = general_style("bold", True)
italic = general_style("italic", True)
strikethrough = general_style("strikethrough", True)
underline = general_style("underline", True)
reset = general_style("reset", True)
