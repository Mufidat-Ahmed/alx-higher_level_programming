#!/usr/bin/python3
"""inserts a line of text to a file, after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """
    Args:
        filename: name of file used
        search_string: string to be found in the file
        new_string: string to be added
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as w:
        w.write(text)
