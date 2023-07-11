#!/usr/bin/python3

"""search and update"""

def append_after(finename="", search_string="", new_string=""):
    """function that inserts a line of text to a file"""
    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fo:
        string = ""
        for line in text:
            string += line
            if search_string in line:
                string += new_string
        fo.write(string)
