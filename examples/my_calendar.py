# Images, icons, and exit button

from tkinter import *
from tkcalendar import *

root = Tk()
root.title('EightSoft Academy')

cal = Calendar(root, selectmode="day", year=2020, month=5, day=22)
cal.pack()


def grab_date():
    my_label.config(text=cal.get_date())


my_btn = Button(root, text="Get Date", command=grab_date).pack()

my_label = Label(root, text="")


root.mainloop()
