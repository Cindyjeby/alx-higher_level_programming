#!/usr/bin/python3

"""defines a function that appends_file"""

def append_write(filename="", text=""):
    """writes a string to a text file"""

    with open(filename, "a", encoding = "UTF -8") as myFile:
        return myFile.write(text)
