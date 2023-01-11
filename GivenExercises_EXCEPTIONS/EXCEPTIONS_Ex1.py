

""" Ex.1
Write a python script that request the user to choose a number. If the number is positive or zero print it,
if the number is negative raise an exception."""




try:
    num = int(raw_input("Please enter a number: "))
    if num >= 0:
        print ("Your number is", num)
    else:
        raise ValueError
except (TypeError, ValueError):
    print "Error! Enter a positive number"
