

""" Chapter 8 Ex. 1
Improve the Critter Caretaker program by allowing the user to specify how much food he or she feeds
the critter and how long he or she plays with the critter. Have these values affect how quickly the
critter's hunger and boredom levels drop. """


class Critter(object):
    """A virtual pet"""

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print " Hello! I'm", self.name, "\n Right now I feel", self.mood, "\n My hunger is", self.hunger
        self.__pass_time()

    def eat(self, food):
        print("Brruppp.  Thank you.")

        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0

        self.__pass_time()

    def play(self, fun):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = raw_input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print \
            ("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)

        choice = raw_input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()

        # feed your critter
        elif choice == "2":
            food = 0
            print("1. Snack\n2. Normal Meal\n3. Big Feast")
            food_choice = int(input("\nChoose food ---> "))
            if food_choice is 1:
                food = 1
            if food_choice is 2:
                food = 5
            if food_choice is 3:
                food = 10
            crit.eat(food)

        # play with your critter
        elif choice == "3":
            fun = 0
            print("1. 10 min\n2. 30 min\n3. 1 hour\n4. 3 hour")
            play_time = int(input("\nChoose play time ---> "))
            if play_time is 1:
                fun = 1
            if play_time is 2:
                fun = 2
            if play_time is 3:
                fun = 4
            if play_time is 4:
                fun = 10
            crit.play(fun)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")


main()

input("\n\nPress the enter key to exit.")
