import os

__version__ = "3.0.2.1"


def include_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "include"))


def lib_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "lib"))
