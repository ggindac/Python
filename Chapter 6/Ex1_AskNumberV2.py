# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

""" Chapter 6 Ex. 1 Pag 195
Improve the function ask_number() so that the function can be called with a step value. Make the
default value of step 1.

def ask_number(question, low, high):   #Ask for a number within a range.
 response = None
 while response not in range(low, high):
    response = int(raw_input(question))
 return response

"""


# Ex.AskNumberV2
def ask_number(question, low, high, step):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(raw_input(question)) + step
    return response


step = 1
x = ask_number("Enter a number within the range (0-10): ", 1, 10, step)
print x
