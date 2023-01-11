
""" Chapter 7 Ex. 3
Write a function in python to count the number of lines from a text file "story.txt" which is not starting with an alphabet "T".
Example:
    If the file "story.txt" contains the following lines:
         A boy is playing there.
         There is a playground.
         An aeroplane is in the sky.
         The sky is pink.
         Alphabets and numbers are allowed in the password.
    The function should display the output as 3
"""
n = 0                                               #Variable used for counting

text_file = open("story.txt", "r")

lines = text_file.readlines()                       #Creating a string/list with all the lines and their elements

for i in range(len(lines)):                         #Looping through the list
    test = lines[i]                                 #Saving each line and and testing the first element
    if test[0] != 'T':
        n += 1
print n
text_file.close()
