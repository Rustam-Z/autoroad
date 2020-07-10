from tkinter import *

window = tkinter.Tk()

# to rename the title of the window window.title("GUI")

# pack is used to show the object in the window

label = tkinter.Label(window, text="Hello World!").pack()

window.mainloop()