# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

""" Chapter 3 Ex.1

Ex.1 Write a program that simulates a fortune cookie. The program should display one of five unique
fortunes, at random, each time it's run. """

# Ex.1
import random

print("Your fortune for today is:")

fortune = random.randrange(4)                                                 # Creates a random number
if fortune == 1:
    print("Some pursue happiness; you create it")
elif fortune == 2:
    print('''I see money in your future... 
                    It it's not yours tho''')
elif fortune == 3:
    print("Never forget that half of the truth is a whole lie")
elif fortune == 4:
    print("Everyone agrees. You are the best.")
else:
    print("Keep your eye out for someone special.")
