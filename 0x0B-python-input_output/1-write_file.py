#!/usr/bin/python3
"""writes a string to a text file (UTF8)"""

def write_file(filename="", text=""):
    """
    Args:
        filename: name of file used
        text: content of file
    Return: number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
