import ctypes
import platform
import sys

from palettepy.printer import PrinterConfiguration

major_version = sys.version_info[0]

if major_version == 2:
    import __builtin__
elif major_version == 3:
    import builtins as __builtin__

printer_config = PrinterConfiguration()


def init(config=None):
    if config:
        config = config.build_config()

    global printer_config

    enable_ansi(printer_config)
    printer_config = PrinterConfiguration() if not config else config


def print(*args, **kwargs):
    arguments = list(args)
    for i in range(len(args)):
        if type(args[i]) == str:
            arguments[i] = f"{printer_config.printer.run()}{arguments[i]}{printer_config.printer.reset()}"
    return __builtin__.print(*tuple(arguments), **kwargs)


def enable_ansi(printer_config):
    os_name = platform.system()
    if os_name == 'Windows':
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        printer_config.ansi_enabled = True
    elif os_name == 'Linux':
        printer_config.ansi_enabled = True
