import tkinter as tk
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedStyle
from tkinter import messagebox, END
import sys
import os


class MenuBar(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master)
        self.master = master

        # Create a Menu Item for Teachers
        teachers_menu = tk.Menu(self, tearoff=False)

        # Create a Menu Item for Groups
        groups_menu = tk.Menu(self, tearoff=False)

        # Create a Menu Item for Students
        students_menu = tk.Menu(self, tearoff=False)

        # Create a Menu Item for Info --EightSoft dev
        info_menu = tk.Menu(self, tearoff=False)

        # Add the cascades for menu bar
        self.add_cascade(label="Ўқитувчилар", menu=teachers_menu)
        self.add_cascade(label="Гуруҳ", menu=groups_menu)
        self.add_cascade(label="Ўқувчилар", menu=students_menu)
        self.add_cascade(label="Инфо", menu=info_menu)

        # Teachers
        teachers_menu.add_command(label="Қўшиш", command=self.teachers_add)
        teachers_menu.add_command(label="Янгилаш", command=self.teachers_edit)
        teachers_menu.add_command(label="Ўчириш", command=self.teachers_delete)

        # Groups
        groups_menu.add_command(label="Қўшиш", command=self.groups_add)
        groups_menu.add_command(label="Янгилаш", command=self.groups_edit)
        groups_menu.add_command(label="Ўчириш", command=self.groups_delete)

        # Students
        students_menu.add_command(label="Mаълумотлар базаси", command=self.students_db)

        # Info
        info_menu.add_command(label="Илова ҳақида", command=self.info_about)
        info_menu.add_separator()

        # Create frames for each new window --MenuBar-Cascade-Commands
        self.teachers_add_frame = ttk.Frame(master)
        self.teachers_edit_frame = ttk.Frame(master)
        self.teachers_delete_frame = ttk.Frame(master)

        self.groups_add_frame = ttk.Frame(master)
        self.groups_edit_frame = ttk.Frame(master)
        self.groups_delete_frame = ttk.Frame(master)

        self.students_db_frame = ttk.Frame(master)

        self.info_about_frame = ttk.Frame(master)

    # Hide the frames when you switch the menu
    def hide_all_frames(self):
        """Cleans the screen after pressing the menu item"""
        for widget in self.teachers_add_frame.winfo_children():
            widget.destroy()

        for widget in self.teachers_edit_frame.winfo_children():
            widget.destroy()

        for widget in self.teachers_delete_frame.winfo_children():
            widget.destroy()

        for widget in self.groups_add_frame.winfo_children():
            widget.destroy()

        for widget in self.groups_edit_frame.winfo_children():
            widget.destroy()

        for widget in self.groups_delete_frame.winfo_children():
            widget.destroy()

        for widget in self.students_db_frame.winfo_children():
            widget.destroy()

        for widget in self.info_about_frame.winfo_children():
            widget.destroy()

        self.teachers_add_frame.pack_forget()
        self.teachers_edit_frame.pack_forget()
        self.teachers_delete_frame.pack_forget()
        self.groups_add_frame.pack_forget()
        self.groups_edit_frame.pack_forget()
        self.groups_delete_frame.pack_forget()
        self.students_db_frame.pack_forget()
        self.info_about_frame.pack_forget()

    # Create methods for Teachers
    def teachers_add(self):
        self.hide_all_frames()
        self.teachers_add_frame.pack(fill="both", expand=1)

        # Creating a Notebook
        teachers_notebook = ttk.Notebook(self.teachers_add_frame)
        teachers_notebook.pack(pady=10, padx=10)

        # initialize frames for notebooks
        instructors_frame = ttk.Frame(teachers_notebook)
        others_frame = ttk.Frame(teachers_notebook)

        # place frames in the screen
        instructors_frame.pack(fill="both", expand=1)
        others_frame.pack(fill="both", expand=1)

        # add the notebooks
        teachers_notebook.add(instructors_frame, text="Усталap")
        teachers_notebook.add(others_frame, text="Ўқитувчилар")

        # =========== Create Main Form To Enter Teachers Form ===========
        # Усталap -- First notebook
        first_name_label = ttk.Label(instructors_frame, text="Исм").grid(row=1, column=0, padx=10)
        middle_name_label = ttk.Label(instructors_frame, text="Фамилия").grid(row=2, column=0, padx=10)
        last_name_label = ttk.Label(instructors_frame, text="Отчество").grid(row=3, column=0, padx=10)
        license_number_label = ttk.Label(instructors_frame, text="Х/Г №").grid(row=4, column=0, padx=10)
        garage_number_label = ttk.Label(instructors_frame, text="Гар. №").grid(row=5, column=0, padx=10)
        car_label = ttk.Label(instructors_frame, text="Марка").grid(row=6, column=0, padx=10)
        car_number_label = ttk.Label(instructors_frame, text="Гос. №").grid(row=7, column=0, padx=10)

        application_label = ttk.Label(instructors_frame, text="Заявка учун маълумотлар: ").grid(row=8, column=0,
                                                                                                padx=10, columnspan=2)
        education_label = ttk.Label(instructors_frame, text="Маълумоти").grid(row=9, column=0, padx=10)
        type_license_label = ttk.Label(instructors_frame, text="Tоифа").grid(row=10, column=0, padx=10)
        internship_label = ttk.Label(instructors_frame, text="Стаж").grid(row=11, column=0, padx=10)

        # Create Entry Box for the first notebook
        first_name_box = ttk.Entry(instructors_frame)
        first_name_box.grid(row=1, column=1, pady=3, padx=7)
        middle_name_box = ttk.Entry(instructors_frame)
        middle_name_box.grid(row=2, column=1, pady=3)
        last_name_box = ttk.Entry(instructors_frame)
        last_name_box.grid(row=3, column=1, pady=3)
        license_number_box = ttk.Entry(instructors_frame)
        license_number_box.grid(row=4, column=1, pady=3)
        garage_number_box = ttk.Entry(instructors_frame)
        garage_number_box.grid(row=5, column=1, pady=3)
        car_box = ttk.Entry(instructors_frame)
        car_box.grid(row=6, column=1, pady=3)
        car_number_box = ttk.Entry(instructors_frame)
        car_number_box.grid(row=7, column=1, pady=3)

        education_box = ttk.Entry(instructors_frame)
        education_box.grid(row=9, column=1, pady=3)
        type_license_box = ttk.Entry(instructors_frame)
        type_license_box.grid(row=10, column=1, pady=3)
        internship_box = ttk.Entry(instructors_frame)
        internship_box.grid(row=11, column=1, pady=3)

        # Ўқитувчилар -- Second notebook
        t_first_name_label = ttk.Label(others_frame, text="Исм").grid(row=1, column=0, padx=10)
        t_middle_name_label = ttk.Label(others_frame, text="Фамилия").grid(row=2, column=0, padx=10)
        t_last_name_label = ttk.Label(others_frame, text="Отчество").grid(row=3, column=0, padx=10)
        t_education_label = ttk.Label(others_frame, text="Маълумоти").grid(row=4, column=0, padx=10)
        t_specialization_label = ttk.Label(others_frame, text="Мутахасислиги").grid(row=5, column=0, padx=10)

        OptionList = [
            "Aвто. туз.",
            "Taurus",
            "Gemini",
            "Cancer"
        ]

        # Create Entry Box for the first notebook
        t_first_name_box = ttk.Entry(others_frame)
        t_first_name_box.grid(row=1, column=1, pady=3, padx=7)
        t_middle_name_box = ttk.Entry(others_frame)
        t_middle_name_box.grid(row=2, column=1, pady=3)
        t_last_name_box = ttk.Entry(others_frame)
        t_last_name_box.grid(row=3, column=1, pady=3)
        t_education_box = ttk.Entry(others_frame)
        t_education_box.grid(row=4, column=1, pady=3)
        t_specialization_box = ttk.Entry(others_frame)
        t_specialization_box.grid(row=5, column=1, pady=3)

        # function which add a teacher to db
        def db_teachers_add():
            entry_list = [child for child in instructors_frame.winfo_children()
                          if isinstance(child, ttk.Entry)]

            # checking whether all entries are full
            if len(first_name_box.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(middle_name_box.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(last_name_box.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(license_number_box.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(garage_number_box.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(car_box.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(car_number_box.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(education_box.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(type_license_box.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(internship_box.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            else:
                messagebox.showinfo("Муваффақият хабари", "Ўқитувчи маълумотлар базасига муваффақиятли қўшилди!")

            # removing the old data from cells
            first_name_box.delete(0, END)
            middle_name_box.delete(0, END)
            last_name_box.delete(0, END)
            license_number_box.delete(0, END)
            garage_number_box.delete(0, END)
            car_box.delete(0, END)
            car_number_box.delete(0, END)
            education_box.delete(0, END)
            type_license_box.delete(0, END)
            internship_box.delete(0, END)

            # if len(entry_list) == 10:
            #     messagebox.showinfo("Success message", "Teacher has been added in database successfully!")
            # else:
            #     messagebox.showwarning("Warning message!", "Please fill all entries!")

        def db_others_add():
            # checking whether all entries are full
            if len(t_first_name_box.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(t_middle_name_box.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(t_last_name_box.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(t_education_box.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(t_specialization_box.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            else:
                messagebox.showinfo("Муваффақият хабари", "Ўқитувчи маълумотлар базасига муваффақиятли қўшилди!")

            # removing the old data from cells
            t_first_name_box.delete(0, END)
            t_middle_name_box.delete(0, END)
            t_last_name_box.delete(0, END)
            t_education_box.delete(0, END)
            t_specialization_box.delete(0, END)

        # =========== Create Buttons ===========
        # Button for saving the info into db
        instructors_add = ttk.Button(instructors_frame, text="Маълумотлар базасига қўшиш", command=db_teachers_add)
        instructors_add.grid(row=12, column=0, columnspan=2, pady=5)
        instructors_add = ttk.Button(others_frame, text="Маълумотлар базасига қўшиш", command=db_others_add)
        instructors_add.grid(row=6, column=0, columnspan=2, pady=5)

    def teachers_edit(self):
        self.hide_all_frames()
        self.teachers_edit_frame.pack(fill="both", expand=1)
        p2 = ttk.Label(self.teachers_edit_frame, text="Teachers Edit")
        p2.pack()

    def teachers_delete(self):
        self.hide_all_frames()
        self.teachers_delete_frame.pack(fill="both", expand=1)
        p3 = ttk.Label(self.teachers_delete_frame, text="Ўчирмоқчи бўлган ўқитувчини танланг: ")
        p3.pack(padx=10, pady=10)

        OptionList = [
            "Aries",
            "Taurus",
            "Gemini",
            "Cancer"
        ]

        variable = tk.StringVar(self.teachers_delete_frame)
        variable.set(OptionList[0])

        opt = ttk.OptionMenu(self.teachers_delete_frame, variable, OptionList[0], *OptionList)
        opt.config(width=50)
        opt.pack(side="top")

        labelTest = ttk.Label(self.teachers_delete_frame, text="Танланган элемент - {}".format(OptionList[0]))
        labelTest.pack(side="top", pady=10, padx=10)

        def callback(*args):
            labelTest.configure(text="Танланган элемент - {}".format(variable.get()))

        variable.trace("w", callback)

        def delete():
            messagebox.showinfo("Муваффақият хабари", "Ўқитувчи маълумотлар базасидан муваффақиятли ўчирилди!")

        # Create a Delete Button
        delete_btn = ttk.Button(self.teachers_delete_frame, text="Ўчириш", command=delete)
        delete_btn.pack()

        # Create methods for Groups
    def groups_add(self):
        self.hide_all_frames()
        self.groups_add_frame.pack(fill="both", expand=1)
        p4 = ttk.Label(self.groups_add_frame, text="Groups Add")
        p4.pack()

    def groups_edit(self):
        self.hide_all_frames()
        self.groups_edit_frame.pack(fill="both", expand=1)
        p5 = ttk.Label(self.groups_edit_frame, text="Groups Edit")
        p5.pack()

    def groups_delete(self):
        self.hide_all_frames()
        self.groups_delete_frame.pack(fill="both", expand=1)
        p1 = ttk.Label(self.groups_delete_frame, text="Groups Delete")
        p1.pack()

    # Create methods for Students
    def students_db(self):
        self.hide_all_frames()
        self.students_db_frame.pack(fill="both", expand=1)
        p1 = ttk.Label(self.students_db_frame, text="Students Database")
        p1.pack()

    def info_about(self):
        self.hide_all_frames()
        self.info_about_frame.pack(fill="both", expand=1)
        p1 = ttk.Label(self.info_about_frame, text="About")
        p1.pack()

    #     teachers_menu = tk.Menu(self, tearoff=False)
    #     self.add_cascade(label="File", underline=0, menu=teachers_menu)
    #     teachers_menu.add_command(label="Press-1", underline=1, command=self.press1)
    #
    #     groups_menu = tk.Menu(self, tearoff=False)
    #     self.add_cascade(label="New", underline=0, menu=groups_menu)
    #     groups_menu.add_command(label="Press-2", underline=1, command=self.press2)
    #
    # def press1(self):
    #     p1 = ttk.Label(self.parent, text="Press-1")
    #     p1.pack()
    #
    # def press2(self):
    #     p2 = ttk.Label(self.parent, text="Press-2")
    #     p2.pack()
    #
    # def quit(self):
    #     sys.exit(0)


class App(tk.Tk):
    def __init__(self, master):
        tk.Tk.__init__(self)
        self.master = master

        menubar = MenuBar(self)
        self.config(menu=menubar)


if __name__ == "__main__":
    app = App(None)
    app.title("AutoRoad")
    app.geometry("500x500+250+100")
    style = ThemedStyle(app)
    style.set_theme("breeze")
    app.mainloop()
