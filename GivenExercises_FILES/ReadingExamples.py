# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

""" Chapter 7
Examples of reading a file      """


print "\nReading characters from the file."
text_file = open("Text.txt", "r")
print text_file.read(1)
print text_file.read(5)
text_file.close()

print "\nReading the entire file at once."
text_file = open("Text.txt", "r")
whole_thing = text_file.read()
print whole_thing
text_file.close()


print "\nReading characters from a line."
text_file = open("Text.txt", "r")
print text_file.readline(1)
print text_file.readline(5)
text_file.close()


print "\nReading one line at a time."
text_file = open("Text.txt", "r")
print text_file.readline()
print text_file.readline()
print text_file.readline()
text_file.close()

print "\nReading the first line."
text_file = open("Text.txt", "r")
print text_file.readline()
text_file.close()


print "\nReading the entire file into a list."
text_file = open("Text.txt", "r")
lines = text_file.readlines()
print lines
print len(lines)
for line in lines:
    print line
text_file.close()


print "\nLooping through the file, line by line."
text_file = open("Text.txt", "r")
for line in text_file:
    print line
text_file.close()



