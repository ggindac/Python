# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

""" Chapter 5 Ex.3

Write a Who's Your Daddy? program that lets the user enter the name of a male and produces the
name of his father. (You can use celebrities, fictional characters, or even historical figures for fun.)
Allow the user to add, replace, and delete son-father pairs. The program should also allow the user to
get a list of all sons, or fathers, or son-father pairs."""

# Ex.3
Daddy = {
    "Fermin Portela-Matos" : "Oliver Skyes"
}

option = None

while option != 0:

    print "Choose an option:"
    print " 0. Exit\n 1. Who's Your Daddy?\n 2. Add a new entry\n 3. Delete an existing entry\n"

    option = int(input("Option: "))

    if option == 1:

        Son = raw_input("Enter your name: ")

        if Son in Daddy:
            print Daddy[Son]
        else:
            print("Name doesn't exist.")


    elif option == 2:

        Son = raw_input("Enter the name of the son: ")
        Father = raw_input("Enter the name of the dad: ")

        Daddy[Son] = Father

    elif option == 3:

        Son = raw_input("Enter the name of the son you want to delete: ")
        Daddy.pop(Son)

    else:
        print("Exit")