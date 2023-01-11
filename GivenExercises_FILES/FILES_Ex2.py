

""" Chapter 7 Ex.2
Write a Python program to append text to a file and display the text."""

print "\nAppend text to a file"
text_file = open("Text.txt", "a")


text_file.write(raw_input("Introduce the text you want to append: "))
text_file.close()

text_file = open("Text.txt", "r")
whole_thing = text_file.read()
print whole_thing
text_file.close()

