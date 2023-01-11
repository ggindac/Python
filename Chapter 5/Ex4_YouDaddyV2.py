# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""  Chapter 5 Ex.4

Ex.4 Improve the Who's Your Daddy program by adding a choice that lets the user enter a name and get
back a grandfather. Your program should still only use one dictionary of son-father pairs. Make sure to
include several generations in your dictionary so that a match can be found."""

# Ex.4
option = None
position = 'n'

Daddy = {
            "Son": ["Marius", "Ionut"],
            "Father": ["Vlad", "Marcel"],
            "Grandfather": ["Traian", "Leonidas"]
}


while option != 0:

    print "Choose an option:"
    print " 0. Exit\n 1. Who's Your Daddy?\n 2. Who's Your GranDaddy?\n 3. Add a new entry\n 4. Delete an existing entry\n"

    option = int(input("Option: "))

    if option == 1:

        name = raw_input("Enter your name: ")
        results_Son = Daddy["Son"]

        for i in range(0, len(results_Son)):
            if results_Son[i] == name:
                position = i

        if position != 'n':
            results_Daddy = Daddy["Father"]
            print("Your Daddy is: " + results_Daddy[position])
        else:
            print("Name doesn't exist.")
        del position

    elif option == 2:

        name = raw_input("Enter your name: ")
        results_Son = Daddy["Son"]

        for i in range(0, len(results_Son)):
            if results_Son[i] == name:
                position = i

        if position != 'n':
            results_GranDaddy = Daddy["Grandfather"]
            print("Your GranDaddy is: " + results_GranDaddy[position])
        else:
            print("Name doesn't exist.")
        del position

    elif option == 3:

        name = raw_input("Enter the name of the Son you want to remove: ")
        Daddy["Son"].append(name)

        name_Daddy = raw_input("Enter the name of the Daddy you want to remove: ")
        Daddy["Father"].append(name_Daddy)

        name_GranDaddy = raw_input("Enter the name of the GranDaddy you want to remove: ")
        Daddy["Grandfather"].append(name_GranDaddy)

    elif option == 4:

        name = raw_input("Enter the name of the Son you want to add: ")

        results_Son = Daddy["Son"]

        for i in range(0, len(results_Son)):
            if results_Son[i] == name:
                position = i

        Daddy["Son"].pop(position)
        Daddy["Father"].pop(position)
        Daddy["Grandfather"].pop(position)

        del position
        for key, value in Daddy.items():
            print key, ':', value

    else:
        print("Exit")
