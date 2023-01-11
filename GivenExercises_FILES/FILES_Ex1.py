
""" Chapter 7 Ex.2
Write a Python program to read first n lines of a file. Write a Python program to read last n lines of a file."""


print "\nReading first n lines of a file. (Version 1)"
text_file = open("Text.txt", "r")

n = int(raw_input("Enter the number of lines you want to read: "))
for i in range(1, n+1):
    print text_file.readline()
text_file.close()

""" #Reading from a specific line

print "\nReading first n lines of a file. (Version 2)"
text_file = open("Text.txt", "r")

n = int(raw_input("Enter the number of line you want to read from: "))
for line in (text_file.readlines()[n:n+2]):
    print(line)
text_file.close()"""


print "\nReading the last n lines of a file."
text_file = open("Text.txt", "r")

n = int(raw_input("Enter the number of lines you want to read: "))
for line in (text_file.readlines()[-n:]):
    print(line)
text_file.close()