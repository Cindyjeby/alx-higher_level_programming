#!/usr/bin/python3

"""defines a function read_file"""

def write_file(filename="", text=""):
    """writes a string to a text file"""

    with open(filename, "w", encoding = "UTF -8") as myFile:
        return myFile.write(text)
