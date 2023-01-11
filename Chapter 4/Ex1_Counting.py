# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

""" Chapter 4 Ex.1

Ex.1 Write a program that counts for the user. Let the user enter the starting number, the ending number,
and the amount by which to count."""

# Ex.1 Counting
starting_number = input("Introduce the starting number: ")
ending_number = input("Introduce the ending number: ")

step = input("Introduce the step you want in your counting: ")

x = starting_number
while x <= ending_number:
    print x
    x += step
