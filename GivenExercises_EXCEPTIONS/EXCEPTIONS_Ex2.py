
"""
Create a program which opens a file and writes some data into it. Handle exceptions that can be generated during the
                                                                                                     I/O operations."""


try:
    text_file = open("exceptions.txt", "w")

    raise IOError
except IOError:
    print "Error"
