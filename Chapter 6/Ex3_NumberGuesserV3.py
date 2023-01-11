
""" Chapter 6 Ex. 3 Pag 195
Modify the new version of Guess My Number you created in the last challenge so that the program's
code is in a function called main(). Don't forget to call main() so that you can play the game"""

import random


def ask_number(question, the_number):

    guess = None
    tries = 0

    while guess != the_number:
        if guess < the_number:
            print("The number to guess is Higher")
            guess = int(raw_input(question))
            tries += 1
        else:
            print("The number to guess is Lower")
            guess = int(raw_input(question))
            tries += 1

    if guess == the_number:
        print "And it only took you", tries, "tries!\n"
        print "You guessed it! The number was", the_number


def main():
    the_number = random.randrange(1, 10)
    ask_number("Guess the number (must be between 0 - 100): ", the_number)


main()

