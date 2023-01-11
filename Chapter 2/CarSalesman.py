

""" Chapter 2   Ex.4
Write a Car Salesman program where the user enters the base price of a car. The program should add
on a bunch of extra fees such as tax, license, dealer prep, and destination charge. Make tax and
license a percent of the base price. The other fees should be set values. Display the actual price of the
car once all the extras are applied."""


# Ex.4 Car Salesman
base_costs = int(input("Enter the base price of a car: "))

tax = 0.30*base_costs        # tax is 30% of bace price of a car
license = 0.15*base_costs    # license is 15% of base price of a car

dealer_prep = 25
destination_charge = 50

print("The actual price of the car is: ", base_costs+tax+license+dealer_prep+destination_charge)