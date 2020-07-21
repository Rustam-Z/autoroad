from tkinter import *
from tkinter import messagebox
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk
import os


class Root:
    def __init__(self, master):
        self.my_menu = Menu(master)
        master.config(menu=self.my_menu)
        self.master = master

        # Create a Menu Item for Teachers
        self.file_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Укитувчи", menu=self.file_menu)
        self.file_menu.add_command(label="Кошиш", command=self.command_file_new)
        self.file_menu.add_command(label="Янгилаш", command=self.master.quit)
        self.file_menu.add_command(label="Учириш", command=self.master.quit)

        # Create a Menu Item Groups
        self.edit_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Гуруҳ", menu=self.edit_menu)
        self.edit_menu.add_command(label="Кошиш", command=self.command_edit_cut)
        self.edit_menu.add_command(label="Янгилаш", command=self.master.quit)
        self.edit_menu.add_command(label="Учириш", command=self.master.quit)

        # Create a Menu Item for Students
        self.edit_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Укивчилар", menu=self.edit_menu)
        self.edit_menu.add_command(label="База", command=self.command_edit_cut)

        # Create a Menu Item for Info
        self.edit_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Инфо", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.command_edit_cut)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Question", command=self.master.quit)

        # Create some frames
        self.file_new_frame = ttk.Frame(self.master, width=400, height=400)
        self.edit_cut_frame = ttk.Frame(self.master, width=400, height=400)

        # Showing the list of groups
        files_list = os.listdir('groups')
        files_list_box = Listbox(self.master)
        files_list_box.pack(side=TOP, anchor=NW)
        # THE ITEMS INSERTED WITH A LOOP
        for item in files_list:
            item = item[:-5]
            files_list_box.insert(END, item)

        # files_list = os.listdir('groups')
        # item_count = 0
        # for item in files_list:
        #     btn = ttk.Button(master, text=item[:-5], )
        #     btn.pack(side=TOP, anchor=NW)
        #     item_count += 1

    def hide_all_frames(self):
        """Clears the screen after pressing the menu item"""
        for widget in self.file_new_frame.winfo_children():
            widget.destroy()

        for widget in self.edit_cut_frame.winfo_children():
            widget.destroy()

        self.file_new_frame.pack_forget()
        self.edit_cut_frame.pack_forget()

    # Create a functions for commands
    def command_file_new(self):
        """When you press File->New ... the following function code will work"""
        self.hide_all_frames()
        self.file_new_frame.pack(fill="both", expand=1)
        lab0 = ttk.Label(self.file_new_frame, text="it is just for checking New->File")
        btn0 = ttk.Button(self.file_new_frame, text="asdf", command=self.test)
        btn0.pack()
        lab0.pack()

    def test(self):
        ttk.Label(self.file_new_frame, text="asdf").pack()

    def command_edit_cut(self):
        self.hide_all_frames()
        self.edit_cut_frame.pack(fill="both", expand=1)
        lab1 = ttk.Label(self.edit_cut_frame, text="it is just for checking Edit->Cut")
        lab1.pack()


def main():
    root = ThemedTk(theme="breeze")
    root.geometry("500x500+250+100")
    app = Root(root)
    root.mainloop()


if __name__ == '__main__':
    main()


