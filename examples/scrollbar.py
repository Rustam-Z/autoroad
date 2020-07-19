from tkinter import *

root = Tk()
root.geometry("400x400")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

my_list = Listbox(root, yscrollcommand=scrollbar.set)
for line in range(100):
    my_list.insert(END, "This is line number " + str(line))

my_list.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=my_list.yview)

mainloop()
