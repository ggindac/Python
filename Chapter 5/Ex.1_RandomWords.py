# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""  Chapter 3

Ex.1 Create a program that prints a list of words in random order. The program should print all the words and
not repeat any. """

# Ex.1 Random Oder List
import random
i = 0
words = ['munte', 'lac', 'apa', 'ceata', 'padure', 'copaci']

print("The normal list is: ", words)
print("The elements of the list in a random order :", random.sample(words, len(words)))

