
""" Chapter 10. Given Exercise
Write a Python GUI program to create a user interface which should contain:
- two buttons exit and hello
- a Combobox with three options using tkinter module
- a Checkbutton widget using tkinter module
- two text box to accept values from the user and then display sum, difference, multiplication and division of them"""

# GUI program

vlist = ["Option1", "Option2", "Option3"]

from tkinter import *
from tkinter import ttk

root = Tk()                         # creating the main window and storing the window object in 'root'
root.title('Welcome')               # setting title of the window

root.geometry('500x350')

# Dropdown list
Combo = ttk.Combobox(root, values = vlist)
Combo.set("Pick an Option")
Combo.grid(row=1, sticky=W)

# Checkbutton
cb_var1 = IntVar()
Checkbutton(root, text='Checkbutton', variable=cb_var1, onvalue=1, offvalue=0, height=5, width=20).grid(row=0,
                                                                                                        sticky=W)

# Writing Boxes
ent1 = Entry(root)
ent1.grid(row=3, column=0)

ent2 = Entry(root)
ent2.grid(row=4, column=0)


root.mainloop()                     # running the loop that works as a trigger

