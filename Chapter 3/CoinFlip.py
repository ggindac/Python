# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

""" Chapter 3  EX.2
Ex.2 Write a program that flips a coin 100 times and then tells you the number of heads and tails.
Modify the Guess My Number game so that the player has a limited number of guesses. If the player
fails to guess in time, the program should display an appropriately chastising message. """

# Ex.2 Coin Flip
import random

tail = 0
head = 0
flip = 0

while flip < 100:

    coin = random.randrange(2)

    if coin is 0:           # Coin is tail
        tail += 1
    elif coin is 1:         # Coin is head
        head += 1
    flip += 1               # Increment

print("You flipped", tail, "tails and", head, "heads")
