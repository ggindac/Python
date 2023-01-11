# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""  Chapter 5 Ex.2

Ex.2 Write a Character Creator program for a role-playing game. The player should be given a pool of 30
points to spend on four attributes: Strength, Health, Wisdom, and Dexterity. The player should be able
to spend points from the pool on any attribute and should also be able to take points from an attribute
and put them back into the pool."""

# Ex.2 Character Creator
option = None
points = 30

CharacterCreator ={
    "Strength":  0,
    "Health":    0,
    "Wisdom":    0,
    "Dexterity": 0
}

while option != 0:
    print "Choose an option:"
    print " 0. Exit\n 1. View skill points\n 2. Add skill points\n 3. Reduce skill points"
    option = int(input("Option: "))

    if option == 1:
        for key, value in CharacterCreator.items():
            print key, ':', value
        print "You have ", points, " points left\n"

    elif option == 2:

        name = raw_input("Choose an attribute to level up:")                    # Reading the attribute that we want to change

        current_points = CharacterCreator[name]                                 # Finding the current points that we have on the said attribute

        skill_points = raw_input("Number of points you want to add: ")          # Asking the number of points to be added to this attribute

        new_points = int(skill_points) + int(current_points)
        CharacterCreator.update({name: new_points})                              # Updating the dictionary with the new number of points


        print ("Your", name, "now has", int(current_points) + int(skill_points),"points")

        points -= int(skill_points)                                               # Updating the number of points left
        print ("Your remaining points are: ", points)


    elif option == 3:

        name = raw_input("Choose an attribute to level up:")                      # Reading the attribute that we want to change

        current_points = CharacterCreator[name]                                   # Finding the current points that we have on the said attribute

        if current_points == 0:
            print ("You currently have no points in ", name)

        else:

            skill_points = raw_input("Number of points you want to reduce: ")     # Asking the number of points to be reduced from this attribute

            if current_points < skill_points:
                print ("Your", name, "has less points than you want to reduce")

                points += current_points
                print ("Your remaining points are: ", points)

                CharacterCreator.update({name: 0})

            elif current_points >= skill_points:

                    new_points = int(current_points) - int(skill_points)
                    CharacterCreator.update({name: new_points})                     # Updating the dictionary with the new number of points

                    print ("Your", name, "now has", int(current_points) - int(skill_points), "points")

                    points += int(skill_points)  # Updating the number of points left
                    print ("Your remaining points are: ", points)
    else:
        print(exit)
        #exit()

