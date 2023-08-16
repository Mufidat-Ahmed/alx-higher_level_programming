#!/usr/bin/python3
"""appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """
    Args:
        filename: name of the file
        text: text to be added
    Return: returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
