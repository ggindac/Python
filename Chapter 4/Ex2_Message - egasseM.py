# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

""" Chapter 4 Ex.2

Ex.2 Create a program that gets a message from the user and then prints it out backwards."""

# Ex.2 Message backwards
storage = []

message = raw_input("Enter your message here: ")

for i in range(len(message), 0, -1):
    storage.append(message[i - 1])

for x in range(len(storage)):
    print storage[x]




