# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

""" Chapter 4 Ex.4

Create a game where the computer picks a random word and the player has to guess that word. The
computer tells the player how many letters are in the word. Then the player gets five chances to ask if a
letter is in the word. The computer can only respond with "yes" or "no". Then, the player must guess the
word."""

# Ex.4 Random Word Guesser
import random

option = None

word_list = ("lucky", "shabby", "crystal", "quartz", "rhythmic", "hamburger", "snorlax", "slowbro", "wyvern")


def guess_letter(r_word):
    no_chances = 0

    while no_chances < 5:
        found = 0
        letter = raw_input("Guess a letter from the word: ")  # Ask the user to guess the letter

        for i in range(0, len(r_word)):
            if letter == r_word[i]:
                found = 1

        no_chances = no_chances + 1

        if found == 1:
            print "Yes"
        if found == 0:
            print "No"


def word_guesser(r_word):
    g_word = raw_input("Enter the word: ")
    ok = 1

    if len(g_word) == len(r_word):
        for i in range(0, len(r_word)):
            if r_word[i] == g_word[i]:
                ok = 1
            else:
                ok = 0
                break
    else:
        ok = 0

    if ok == 1:
        print ("Correct!")
    else:
        print ("Wrong!")

    print ("Your guess: ", g_word)
    print ("Correct answer: ", r_word)


while option != 0:
    print "Choose an option:"
    print " 0. Exit\n 1. Start new game"

    option = int(input("Option: "))
    if option == 1:
        random_word = random.choice(word_list)            # Assign a random word from the tuple

        guess_letter(random_word)
        word_guesser(random_word)
    else:
        print("Exit")