
""" Chapter 6 Ex. 2 Pag 195
Modify the Guess My Number chapter project from Chapter 3 by reusing the function ask_number()"""


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


the_number = random.randrange(1,10)
ask_number("Guess the number (must be between 0 - 100): ", the_number)

