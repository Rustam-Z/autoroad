import tkinter as tk
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedStyle
from tkinter import messagebox, END, TOP, RIGHT, NW, Y
from tkcalendar import DateEntry
import xlwings as xw
import os

class MenuBar(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master)
        self.master = master

        # Create a Menu Item for Database 
        database_menu = tk.Menu(self, tearoff=False)

        # Create a Menu Item for Teachers
        teachers_menu = tk.Menu(self, tearoff=False)

        # Create a Menu Item for Groups
        groups_menu = tk.Menu(self, tearoff=False)

        # Create a Menu Item for Info --EightSoft dev
        info_menu = tk.Menu(self, tearoff=False)

        # Add the cascades for menu bar
        self.add_cascade(label="Mаълумотлар базаси", menu=database_menu)
        self.add_cascade(label="Ўқитувчилар", menu=teachers_menu)
        self.add_cascade(label="Гуруҳ", menu=groups_menu)
        self.add_cascade(label="Инфо", menu=info_menu)

        # Database
        database_menu.add_command(label="Барча гуруҳлар рўйхати", command=self.db_groups)
        database_menu.add_command(label="Барча ўқувчилар рўйхати", command=self.db_students)
        database_menu.add_command(label="Барча ўқитувчилар рўйхати", command=self.db_teachers)

        # Teachers
        teachers_menu.add_command(label="Қўшиш", command=self.teachers_add)
        teachers_menu.add_command(label="Янгилаш", command=self.teachers_edit)
        teachers_menu.add_command(label="Ўчириш", command=self.teachers_delete)

        # Groups
        groups_menu.add_command(label="Қўшиш", command=self.groups_add)
        # groups_menu.add_command(label="Янгилаш", command=self.groups_edit)
        groups_menu.add_command(label="Ўчириш", command=self.groups_delete)

        # Info
        info_menu.add_command(label="Илова ҳақида", command=self.info_about)
        info_menu.add_separator()

        # Create frames for each new window --MenuBar-Cascade-Commands
        self.db_groups_frame = ttk.Frame(master)
        self.db_students_frame = ttk.Frame(master)
        self.db_teachers_frame = ttk.Frame(master)

        self.teachers_add_frame = ttk.Frame(master)
        self.teachers_edit_frame = ttk.Frame(master)
        self.teachers_delete_frame = ttk.Frame(master)

        self.groups_add_frame = ttk.Frame(master)
        self.groups_edit_frame = ttk.Frame(master)
        self.groups_delete_frame = ttk.Frame(master)

        self.info_about_frame = ttk.Frame(master)

    # Hide the frames when you switch the menu
    def hide_all_frames(self):
        """Cleans the screen after pressing the menu item"""
        for widget in self.db_groups_frame.winfo_children():
            widget.destroy()

        for widget in self.db_students_frame.winfo_children():
            widget.destroy()

        for widget in self.db_teachers_frame.winfo_children():
            widget.destroy()

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

        for widget in self.info_about_frame.winfo_children():
            widget.destroy()

        self.db_groups_frame.pack_forget()
        self.db_students_frame.pack_forget()
        self.db_teachers_frame.pack_forget()
        self.teachers_add_frame.pack_forget()
        self.teachers_edit_frame.pack_forget()
        self.teachers_delete_frame.pack_forget()
        self.groups_add_frame.pack_forget()
        self.groups_edit_frame.pack_forget()
        self.groups_delete_frame.pack_forget()
        self.info_about_frame.pack_forget()

    # Create methods for Teachers
    def teachers_add(self):
        self.hide_all_frames()
        self.teachers_add_frame.pack(fill="both", expand=1)

        # Creating a Notebook
        teachers_notebook = ttk.Notebook(self.teachers_add_frame)
        teachers_notebook.pack(pady=10, padx=10)

        # Initialize frames for notebooks
        instructors_frame = ttk.Frame(teachers_notebook)
        others_frame = ttk.Frame(teachers_notebook)

        # Place the frames on the screen
        instructors_frame.pack(fill="both", expand=1)
        others_frame.pack(fill="both", expand=1)

        # Add the notebooks
        teachers_notebook.add(instructors_frame, text="Усталap Қўшиш")
        teachers_notebook.add(others_frame, text="Ўқитувчилар Қўшиш")

        # Create main form to enter teachers - Frontend Part

        # "Усталap" - First notebook
        first_name_label = ttk.Label(instructors_frame, text="Исм").grid(row=1, column=0, padx=10, pady=5)
        middle_name_label = ttk.Label(instructors_frame, text="Фамилия").grid(row=2, column=0, padx=10)
        last_name_label = ttk.Label(instructors_frame, text="Отчество").grid(row=3, column=0, padx=10)
        license_number_label = ttk.Label(instructors_frame, text="Х/Г №").grid(row=4, column=0, padx=10)
        garage_number_label = ttk.Label(instructors_frame, text="Гар. №").grid(row=5, column=0, padx=10)
        car_label = ttk.Label(instructors_frame, text="Марка").grid(row=6, column=0, padx=10)
        car_number_label = ttk.Label(instructors_frame, text="Гос. №").grid(row=7, column=0, padx=10)
        application_label = ttk.Label(instructors_frame, text="Заявка учун маълумотлар: ").grid(row=8, column=0, padx=10, columnspan=2)
        education_label = ttk.Label(instructors_frame, text="      Маълумоти     ").grid(row=9, column=0)
        type_license_label = ttk.Label(instructors_frame, text="Tоифа").grid(row=10, column=0, padx=10)
        internship_label = ttk.Label(instructors_frame, text="Стаж").grid(row=11, column=0, padx=10)

        # Create Entry Box for the First notebook
        first_name_box = ttk.Entry(instructors_frame)
        first_name_box.grid(row=1, column=1, pady=3)
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

        # "Ўқитувчилар" - Second notebook
        OptionList_1 = ["Авто.туз & ЙХК", "Тиббий ёрдам"]
        variable_1 = tk.StringVar(others_frame)
        variable_1.set(OptionList_1[0])
        opt_1 = ttk.OptionMenu(others_frame, variable_1, OptionList_1[0], *OptionList_1)
        opt_1.config(width=24)
        opt_1.grid(row=0, column=0, pady=5, columnspan=2)

        t_first_name_label = ttk.Label(others_frame, text="Исм").grid(row=1, column=0, padx=10)
        t_middle_name_label = ttk.Label(others_frame, text="Фамилия").grid(row=2, column=0, padx=10)
        t_last_name_label = ttk.Label(others_frame, text="Отчество").grid(row=3, column=0, padx=10)
        t_education_label = ttk.Label(others_frame, text="Маълумоти").grid(row=4, column=0, padx=10)
        t_specialization_label = ttk.Label(others_frame, text="Мутахасислиги").grid(row=5, column=0, padx=10)

        # Create Entry Box for the Second notebook
        t_first_name_box = ttk.Entry(others_frame)
        t_first_name_box.grid(row=1, column=1, pady=3, padx=10)
        t_middle_name_box = ttk.Entry(others_frame)
        t_middle_name_box.grid(row=2, column=1, pady=3)
        t_last_name_box = ttk.Entry(others_frame)
        t_last_name_box.grid(row=3, column=1, pady=3)
        t_education_box = ttk.Entry(others_frame)
        t_education_box.grid(row=4, column=1, pady=3)
        t_specialization_box = ttk.Entry(others_frame)
        t_specialization_box.grid(row=5, column=1, pady=3)

        # Function which add a teacher to db
        def db_teachers_add():
            # Opening Excel File
            # wbDataBase = xw.Book('DataBase.xlsm')
            wsDataBase = wbDataBase.sheets['TEACHERS']

            # Checking whether all entries are entered
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
                Condition = True
                num = 5
                while Condition:
                    if wsDataBase.cells(num, "B").value is None:
                        wsDataBase.cells(num, "B").value = [
                            middle_name_box.get() + " " + first_name_box.get() + " " + last_name_box.get(),
                            license_number_box.get(), garage_number_box.get(), car_box.get(), car_number_box.get(),
                            middle_name_box.get() + " " + first_name_box.get() + "- маълумоти " + education_box.get() + ", <" +
                            type_license_box.get() + "> тоифадаги автотранспорт хайдовчиси бўлиб, иш стажи " + internship_box.get() +
                            " йил, " + car_box.get() + " русумли, давлат рақами " + car_number_box.get()+
                             " . Ўқитиш хуқуқи берилган гувохномаси бор. "]
                        Condition = False
                    else:
                        num += 1

                messagebox.showinfo("Муваффақият хабари", "Ўқитувчи маълумотлар базасига муваффақиятли қўшилди!")

            # Removing the old data from cells
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

        def db_others_add():
             # Opening Excel File
            # wbDataBase = xw.Book('DataBase.xlsm')
            wsDataBase = wbDataBase.sheets['TEACHERS']

            # checking whether all entries are entered
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
                Condition = True
                num = 5
                while Condition:
                    if wsDataBase.cells(num, "I").value is None:
                        wsDataBase.cells(num, "I").value = [
                            t_middle_name_box.get()+" "+t_first_name_box.get()+" "+t_last_name_box.get(),
                            "Автотранспорт воситаларининг тузилиши ва техник хизмат кўрсатиш фанидан: " +
                            t_middle_name_box.get()+" "+t_first_name_box.get()+" маълумоти "+
                            t_education_box.get()+" , мутахасислиги - "+ t_specialization_box.get()+
                            ", автомобил эксплуатацияси мухандиси."
                        ]
                        Condition = False
                    else:
                        num += 1

                # Variables for auto or first aid
                if variable_1.get() == "Авто.туз & ЙХК":
                    wsDataBase.cells(num,"K").value = ["Йўл харакати қоидалари ва харакат  хафсизлиги,  асосларидан: "+
                    t_middle_name_box.get()+" "+t_first_name_box.get() +" маълумоти "+t_education_box.get()+
                    ", мутахасислиги - "+t_specialization_box.get() + ", автомобил эксплуатацияси мухандиси. "
                    ]
                elif variable_1.get() == "Тиббий ёрдам":
                    wsDataBase.cells(num,"L").value = ["Тиббий ёрдам кўрсатишдан: "+
                    t_middle_name_box.get()+" "+t_first_name_box.get() +" маълумоти "+t_education_box.get()]
                    wsDataBase.cells(num,"J").value = None


                messagebox.showinfo("Муваффақият хабари", "Ўқитувчи маълумотлар базасига муваффақиятли қўшилди!")
                
            # Removing the old data from cells
            t_first_name_box.delete(0, END)
            t_middle_name_box.delete(0, END)
            t_last_name_box.delete(0, END)
            t_education_box.delete(0, END)
            t_specialization_box.delete(0, END)

        # Button for adding the teachers info into db
        instructors_add = ttk.Button(instructors_frame, text="Маълумотлар базасига қўшиш", command=db_teachers_add)
        instructors_add.grid(row=12, column=0, columnspan=2, pady=5)
        others_add = ttk.Button(others_frame, text="Маълумотлар базасига қўшиш", command=db_others_add)
        others_add.grid(row=6, column=0, columnspan=2, pady=5)

    def teachers_edit(self):
        self.hide_all_frames()
        self.teachers_edit_frame.pack(fill="both", expand=1)

        # Creating a Notebook
        teachers_edit_notebook = ttk.Notebook(self.teachers_edit_frame)
        teachers_edit_notebook.pack(pady=10, padx=10)

        # Initialize frames for notebooks
        instructors_edit_frame = ttk.Frame(teachers_edit_notebook)
        others_edit_frame = ttk.Frame(teachers_edit_notebook)

        # Place frames in the screen
        instructors_edit_frame.pack(fill="both", expand=1)
        others_edit_frame.pack(fill="both", expand=1)

        # Add the notebooks
        teachers_edit_notebook.add(instructors_edit_frame, text="Усталapни Янгилаш")
        teachers_edit_notebook.add(others_edit_frame, text="Ўқит-ни Янгилаш")

        # Opening Excel File
        # wbDataBase = xw.Book('DataBase.xlsm')
        wsDataBase = wbDataBase.sheets['TEACHERS']

        # Take the data from excel as python list
        Condition = True
        num = 5
        master = []
        while Condition:
            if wsDataBase.cells(num, "B").value is not None:
                master.append(wsDataBase.cells(num, "B").value)
                master.append(wsDataBase.cells(num, "C").value)
                master.append(wsDataBase.cells(num, "D").value)
                master.append(wsDataBase.cells(num, "E").value)
                master.append(wsDataBase.cells(num, "F").value)
                num += 1
            else:
                Condition = False

        masters = [master[x:x + 5] for x in range(0, len(master), 5)]
        # print("Masters: " + str(masters))
    
        # "Усталap" - First notebook 
        # global function for the Option Menu
        def option_menu_test(*args):
            # Remove the old data from cells
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
            # print(variable_master.get())

            record_selected = []
            for records in masters:
                if records[0] == variable_master.get():
                    record_selected = records
            # print("Records: " + str(record_selected))

            first_name_box.insert(0, record_selected[0].split()[0])
            middle_name_box.insert(0, record_selected[0].split()[1])
            last_name_box.insert(0, record_selected[0].split()[2])
            license_number_box.insert(0, (record_selected[1]))
            garage_number_box.insert(0, (record_selected[2]))
            car_box.insert(0, (record_selected[3]))
            car_number_box.insert(0, (record_selected[4]))
            education_box.insert(0, "-")
            type_license_box.insert(0, "-")
            internship_box.insert(0, "-")

        OptionListForInstructors = []
        for pos in range(len(masters)):
            OptionListForInstructors.append(masters[pos][0])
        # print(OptionListForInstructors)

        # Cheack whether the list is empty
        if len(OptionListForInstructors) == 0:
            messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, аввал ўқитувчиларни маълумотлар базасига қўшинг!")

        variable_master = tk.StringVar(instructors_edit_frame)
        variable_master.set(OptionListForInstructors[0])

        opt_i = ttk.OptionMenu(instructors_edit_frame, variable_master, OptionListForInstructors[0], *OptionListForInstructors, command=option_menu_test)
        opt_i.config(width=30)
        opt_i.grid(row=0, column=0, columnspan=2, pady=5)

        # Labels for the first notebook
        first_name_label = ttk.Label(instructors_edit_frame, text="Исм").grid(row=1, column=0, padx=10)
        middle_name_label = ttk.Label(instructors_edit_frame, text="Фамилия").grid(row=2, column=0, padx=10)
        last_name_label = ttk.Label(instructors_edit_frame, text="Отчество").grid(row=3, column=0, padx=10)
        license_number_label = ttk.Label(instructors_edit_frame, text="Х/Г №").grid(row=4, column=0, padx=10)
        garage_number_label = ttk.Label(instructors_edit_frame, text="Гар. №").grid(row=5, column=0, padx=10)
        car_label = ttk.Label(instructors_edit_frame, text="Марка").grid(row=6, column=0, padx=10)
        car_number_label = ttk.Label(instructors_edit_frame, text="Гос. №").grid(row=7, column=0, padx=10)
        application_label = ttk.Label(instructors_edit_frame, text="Заявка учун маълумотлар: ").grid(row=8, column=0, padx=10,columnspan=2)
        education_label = ttk.Label(instructors_edit_frame, text="Маълумоти ").grid(row=9, column=0, padx=20)
        type_license_label = ttk.Label(instructors_edit_frame, text="Tоифа").grid(row=10, column=0, padx=10)
        internship_label = ttk.Label(instructors_edit_frame, text="Стаж").grid(row=11, column=0, padx=10)

        # Create entry boxes for the first notebook
        first_name_box = ttk.Entry(instructors_edit_frame)
        first_name_box.grid(row=1, column=1, pady=3, padx=7)
        middle_name_box = ttk.Entry(instructors_edit_frame)
        middle_name_box.grid(row=2, column=1, pady=3)
        last_name_box = ttk.Entry(instructors_edit_frame)
        last_name_box.grid(row=3, column=1, pady=3)
        license_number_box = ttk.Entry(instructors_edit_frame)
        license_number_box.grid(row=4, column=1, pady=3)
        garage_number_box = ttk.Entry(instructors_edit_frame)
        garage_number_box.grid(row=5, column=1, pady=3)
        car_box = ttk.Entry(instructors_edit_frame)
        car_box.grid(row=6, column=1, pady=3)
        car_number_box = ttk.Entry(instructors_edit_frame)
        car_number_box.grid(row=7, column=1, pady=3)

        education_box = ttk.Entry(instructors_edit_frame)
        education_box.grid(row=9, column=1, pady=3)
        type_license_box = ttk.Entry(instructors_edit_frame)
        type_license_box.grid(row=10, column=1, pady=3)
        internship_box = ttk.Entry(instructors_edit_frame)
        internship_box.grid(row=11, column=1, pady=3)

        # "Ўқитувчилар" -- Second notebook
                # Ikkinchi Notebook
        Condition_2 = True
        num = 5
        master_2 = []
        while Condition_2:
            if wsDataBase.cells(num, "I").value is not None:
                master_2.append(wsDataBase.cells(num, "I").value)
                master_2.append(wsDataBase.cells(num, "G").value)
                master_2.append(wsDataBase.cells(num, "K").value)
                master_2.append(wsDataBase.cells(num, "L").value)
                num += 1
            else:
                Condition_2 = False

        masters_2 = [master_2[x:x + 4] for x in range(0, len(master_2), 4)]

        def option_menu_test2(*args):
            # Remove the old data from cells
            t_first_name_box.delete(0, END)
            t_middle_name_box.delete(0, END)
            t_last_name_box.delete(0, END)
            t_education_box.delete(0, END)
            t_specialization_box.delete(0, END)
            # print(variable_master.get())

            record_selected = []
            for records in masters_2:
                if records[0] == variable_others.get():
                    record_selected = records
            # print("Records: " + str(record_selected))

            t_first_name_box.insert(0, record_selected[0].split()[0])
            t_middle_name_box.insert(0, record_selected[0].split()[1])
            t_last_name_box.insert(0, record_selected[0].split()[2])
            t_education_box.insert(0, "-")
            t_specialization_box.insert(0,'-')

        OptionListForOthers = []
        for pos in range(len(masters_2)):
            OptionListForOthers.append(masters_2[pos][0])

        # Cheack whether the list is empty
        if len(OptionListForOthers) == 0:
            messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, аввал ўқитувчиларни маълумотлар базасига қўшинг!")

        variable_others = tk.StringVar(others_edit_frame)
        variable_others.set(OptionListForOthers[0])

        opt_o = ttk.OptionMenu(others_edit_frame, variable_others, OptionListForOthers[0], *OptionListForOthers, command=option_menu_test2)
        opt_o.config(width=30)
        opt_o.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        # Create Lables for the second notebook
        t_first_name_label = ttk.Label(others_edit_frame, text="Исм").grid(row=1, column=0, padx=10)
        t_middle_name_label = ttk.Label(others_edit_frame, text="Фамилия").grid(row=2, column=0, padx=10)
        t_last_name_label = ttk.Label(others_edit_frame, text="Отчество").grid(row=3, column=0, padx=10)
        t_education_label = ttk.Label(others_edit_frame, text="Маълумоти").grid(row=4, column=0, padx=10)
        t_specialization_label = ttk.Label(others_edit_frame, text="Мутахасислиги").grid(row=5, column=0, padx=10)

        # Create Entry Box for the second notebook
        t_first_name_box = ttk.Entry(others_edit_frame)
        t_first_name_box.grid(row=1, column=1, pady=3, padx=7)
        t_middle_name_box = ttk.Entry(others_edit_frame)
        t_middle_name_box.grid(row=2, column=1, pady=3)
        t_last_name_box = ttk.Entry(others_edit_frame)
        t_last_name_box.grid(row=3, column=1, pady=3)
        t_education_box = ttk.Entry(others_edit_frame)
        t_education_box.grid(row=4, column=1, pady=3)
        t_specialization_box = ttk.Entry(others_edit_frame)
        t_specialization_box.grid(row=5, column=1, pady=3)

        # Functions which add a teacher to db
        def db_teachers_edit():
            record_selected = []
            for records in masters:
                if records[0] == variable_master.get():
                    record_selected = records

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
                Condition = True
                num = 5
                while Condition:
                    if wsDataBase.cells(num, "B").value == record_selected[0]:
                        wsDataBase.cells(num, "B").value = [
                            middle_name_box.get() + " " + first_name_box.get() + " " + last_name_box.get(),
                            license_number_box.get(), garage_number_box.get(), car_box.get(), car_number_box.get(),
                            middle_name_box.get() + " " + first_name_box.get() + "- маълумоти " + education_box.get() + ", <" +
                            type_license_box.get() + "> тоифадаги автотранспорт хайдовчиси бўлиб, иш стажи " + internship_box.get() +
                            " йил, " + car_box.get() + " русумли, давлат рақами " + car_number_box.get()]
                        Condition = False
                    else:
                        num += 1

                messagebox.showinfo("Муваффақият хабари", "Ўқитувчи маълумотлар базасидан муваффақиятли янгиланди!")

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

        def db_others_edit():
            record_selected = []
            for records in masters_2:
                if records[0] == variable_others.get():
                    record_selected = records

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
                Condition_2 = True
                num = 5
                while Condition_2:
                    if wsDataBase.cells(num, "I").value == record_selected[0]:
                        wsDataBase.cells(num, "I").value = [
                            t_middle_name_box.get()+" "+t_first_name_box.get()+" "+t_last_name_box.get(),
                            "Автотранспорт воситаларининг тузилиши ва техник хизмат кўрсатиш фанидан: " +
                            t_middle_name_box.get()+" "+t_first_name_box.get()+" маълумоти "+
                            t_education_box.get()+" , мутахасислиги - "+ t_specialization_box.get()+
                            ", автомобил эксплуатацияси мухандиси."
                        ]
                        Condition_2 = False
                    else:
                        num += 1
                if wsDataBase.cells(num,"K").value == None:
                    wsDataBase.cells(num,"L").value = ["Тиббий ёрдам кўрсатишдан: "+
                    t_middle_name_box.get()+" "+t_first_name_box.get() +" маълумоти "+t_education_box.get()]
                    wsDataBase.cells(num,"J").value = None
                else:
                    wsDataBase.cells(num,"K").value = ["Йўл харакати қоидалари ва харакат  хафсизлиги,  асосларидан: "+
                    t_middle_name_box.get()+" "+t_first_name_box.get() +" маълумоти "+t_education_box.get()+
                    ", мутахасислиги - "+t_specialization_box.get() + ", автомобил эксплуатацияси мухандиси. "
                    ]

                messagebox.showinfo("Муваффақият хабари", "Ўқитувчи маълумотлар базасидан муваффақиятли янгиланди!")

            # removing the old data from cells
            t_first_name_box.delete(0, END)
            t_middle_name_box.delete(0, END)
            t_last_name_box.delete(0, END)
            t_education_box.delete(0, END)
            t_specialization_box.delete(0, END)

        # Button for saving the info into db
        instructors_edit = ttk.Button(instructors_edit_frame, text="Маълумотлар базасини янгилаш",
                                     command=db_teachers_edit)
        instructors_edit.grid(row=12, column=0, columnspan=2, pady=5)
        others_edit = ttk.Button(others_edit_frame, text="Маълумотлар базасини янгилаш", command=db_others_edit)
        others_edit.grid(row=6, column=0, columnspan=2, pady=5)

    def teachers_delete(self):
        self.hide_all_frames()
        self.teachers_delete_frame.pack(fill="both", expand=1)

        param = ttk.Label(self.teachers_delete_frame, text="Ўчирмоқчи бўлган ўқитувчини танланг: ")
        param.pack(padx=10, pady=10)

        # Opening Excel File
        # wbDataBase = xw.Book('DataBase.xlsm')
        wsDataBase = wbDataBase.sheets['TEACHERS']

        # Taking data from excel as list
        Condition = True
        num = 5
        master = []
        while Condition:
            if wsDataBase.cells(num, "B").value is not None:
                master.append(wsDataBase.cells(num, "B").value)
                master.append(wsDataBase.cells(num, "C").value)
                master.append(wsDataBase.cells(num, "D").value)
                master.append(wsDataBase.cells(num, "E").value)
                master.append(wsDataBase.cells(num, "F").value)
                master.append(wsDataBase.cells(num, "G").value)
                num += 1
            else:
                Condition = False

        masters = [master[x:x + 6] for x in range(0, len(master), 6)]

        Condition_2 = True
        num_2 = 5
        master_2 = []
        while Condition_2:
            if wsDataBase.cells(num_2, "I").value is not None:
                master_2.append(wsDataBase.cells(num_2, "I").value)
                master_2.append(wsDataBase.cells(num_2, "J").value)
                master_2.append(wsDataBase.cells(num_2, "K").value)
                master_2.append(wsDataBase.cells(num_2, "L").value)
                num_2 += 1
            else:
                Condition_2 = False

        masters_2 = [master_2[x:x + 4] for x in range(0, len(master_2), 4)]
        # print(masters_2)
        
        OptionList = []
        for pos in range(len(masters)):
            OptionList.append(masters[pos][0])
        for pos in range(len(masters_2)):
            OptionList.append(masters_2[pos][0])

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
            num = 5
            wsDataBase.range("B5:G59").value = None
            for records in masters:
                if records[0] != variable.get():
                    wsDataBase.cells(num, "B").value = [
                        records[0], 
                        records[1],
                        records[2],
                        records[3],
                        records[4],
                        records[5]]
                    num += 1
            
            num_2 = 5
            wsDataBase.range("I5:L34").value = None
            for records in masters_2:
                if records[0] != variable.get():
                    wsDataBase.cells(num_2, "I").value = [
                        records[0], 
                        records[1],
                        records[2],
                        records[3] ]
                    num_2 += 1
    
            messagebox.showinfo("Муваффақият хабари", "Ўқитувчи маълумотлар базасидан муваффақиятли ўчирилди!")

        # Create a Delete Button
        delete_btn = ttk.Button(self.teachers_delete_frame, text="Ўчириш", command=delete)
        delete_btn.pack()

    # Create methods for Groups
    def groups_add(self):
        self.hide_all_frames()
        self.groups_add_frame.pack(fill="both", expand=1)

        # Create a Notebook
        groups_notebook = ttk.Notebook(self.groups_add_frame)
        groups_notebook.pack(pady=10, padx=10)

        # Initialize frames for notebooks
        groups_inside_frame = ttk.Frame(groups_notebook)
        groups_inside_frame.pack()

        # Add the notebook
        groups_notebook.add(groups_inside_frame, text="Гуруҳ Қўшиш")

        # "Guruhlar" - Labels, boxes, and OptionMenus
        group_number_label = ttk.Label(groups_inside_frame, text="Гуруҳ №").grid(row=0, column=0)
        groups_number_entry = ttk.Entry(groups_inside_frame)
        groups_number_entry.grid(row=0, column=1, padx=5, pady=10)

        first_name_label = ttk.Label(groups_inside_frame, text="Тоифа").grid(row=0, column=2, padx=10)
        OptionList_Typee = ["BC", "A", "B", "C", "D", "BE", "CE", "DE"]
        variable_type = tk.StringVar(groups_inside_frame)
        variable_type.set(OptionList_Typee[0])
        opt = ttk.OptionMenu(groups_inside_frame, variable_type, OptionList_Typee[0], *OptionList_Typee)
        opt.config(width=16)
        opt.grid(row=0, column=3, padx=10, pady=10)

        time_duration_label = ttk.Label(groups_inside_frame, text="  Ўқиш\nМуддати").grid(row=1, column=0)
        time_duration_entry = ttk.Entry(groups_inside_frame)
        time_duration_entry.grid(row=1, column=1, padx=5, pady=10)

        # Add a data picker
        groups_date_label = ttk.Label(groups_inside_frame, text="Сана").grid(row=1, column=2, padx=10)
        cal = DateEntry(groups_inside_frame, width=19, bg="darkblue", fg="white", locale="uz_UZ")
        cal.grid(row=1, column=3, padx=10, pady=10)
        # print(cal.get_date())

        lecture_duration_label = ttk.Label(groups_inside_frame, text="Назарий машғулот\n          соати").grid(row=2, column=0, padx=10)
        OptionList_L_start = ["6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "17", "18", "19", "20"]
        variable_l_start = tk.StringVar(groups_inside_frame)
        variable_l_start.set(OptionList_L_start[0])
        opt = ttk.OptionMenu(groups_inside_frame, variable_l_start, OptionList_L_start[0], *OptionList_L_start)
        opt.config(width=16)
        opt.grid(row=2, column=1, padx=10, pady=10)

        lecture_duration_label_2 = ttk.Label(groups_inside_frame, text="дан / гача").grid(row=2, column=2, padx=5)
        OptionList_L_finish = ["6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "17", "18", "19", "20"]
        variable_l_finish = tk.StringVar(groups_inside_frame)
        variable_l_finish.set(OptionList_L_finish[0])
        opt = ttk.OptionMenu(groups_inside_frame, variable_l_finish, OptionList_L_finish[0], *OptionList_L_finish)
        opt.config(width=16)
        opt.grid(row=2, column=3, padx=10, pady=10)

        practice_duration_label = ttk.Label(groups_inside_frame, text="Амалий машғулот\n         соати").grid(row=3, column=0, padx=10)
        OptionList_P_start = ["6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "17", "18", "19", "20"]
        variable_p_start = tk.StringVar(groups_inside_frame)
        variable_p_start.set(OptionList_P_start[0])
        opt = ttk.OptionMenu(groups_inside_frame, variable_p_start, OptionList_P_start[0], *OptionList_P_start)
        opt.config(width=16)
        opt.grid(row=3, column=1, padx=10, pady=10)

        practice_duration_label_2 = ttk.Label(groups_inside_frame, text="дан / гача").grid(row=3, column=2, padx=5)
        OptionList_P_finish = ["6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "17", "18", "19", "20"]
        variable_p_finish = tk.StringVar(groups_inside_frame)
        variable_p_finish.set(OptionList_P_finish[0])
        opt = ttk.OptionMenu(groups_inside_frame, variable_p_finish, OptionList_P_finish[0], *OptionList_P_finish)
        opt.config(width=16)
        opt.grid(row=3, column=3, padx=10, pady=10)

        # ================= Opening Excel ================ 
        # wbDataBase = xw.Book('DataBase.xlsm')
        wsDataBase = wbDataBase.sheets['TEACHERS']

        # Ustalar List from database
        Condition_2 = True
        num = 5
        master_2 = []
        while Condition_2:
            if wsDataBase.cells(num, "I").value is not None:
                master_2.append(wsDataBase.cells(num, "I").value)
                master_2.append(wsDataBase.cells(num, "G").value)
                master_2.append(wsDataBase.cells(num, "K").value)
                master_2.append(wsDataBase.cells(num, "L").value)
                num += 1
            else:
                Condition_2 = False
        masters_2 = [master_2[x:x + 4] for x in range(0, len(master_2), 4)]


        # O'qituvchilar List
        Condition = True
        num = 5
        master = []
        while Condition:
            if wsDataBase.cells(num, "B").value is not None:
                master.append(wsDataBase.cells(num, "B").value)
                master.append(wsDataBase.cells(num, "C").value)
                master.append(wsDataBase.cells(num, "D").value)
                master.append(wsDataBase.cells(num, "E").value)
                master.append(wsDataBase.cells(num, "F").value)
                master.append(wsDataBase.cells(num, "G").value)
                num += 1
            else:
                Condition = False
        masters = [master[x:x + 6] for x in range(0, len(master), 6)]
        


        teacher_name_label = ttk.Label(groups_inside_frame, text="    Ўқитувчи\nАвто.туз, ЙХК").grid(row=4, column=0)
        OptionList_Teacher = []
        for pos in range(len(masters_2)):
            OptionList_Teacher.append(masters_2[pos][0])


        variable_teacher_name = tk.StringVar(groups_inside_frame)
        variable_teacher_name.set(OptionList_Teacher[0])
        opt = ttk.OptionMenu(groups_inside_frame, variable_teacher_name, OptionList_Teacher[0], *OptionList_Teacher)
        opt.config(width=16)
        opt.grid(row=4, column=1, padx=10, pady=10)

        doctor_name_label = ttk.Label(groups_inside_frame, text="    Ўқитувчи\nТиббий ёрдам").grid(row=4, column=2)
        OptionList_doctor = []
        for pos in range(len(masters_2)):
            OptionList_doctor.append(masters_2[pos][0])

        variable_doctor_name = tk.StringVar(groups_inside_frame)
        variable_doctor_name.set(OptionList_doctor[0])
        opt = ttk.OptionMenu(groups_inside_frame, variable_doctor_name, OptionList_doctor[0], *OptionList_doctor)
        opt.config(width=16)
        opt.grid(row=4, column=3, padx=10, pady=10)

        # Masters
        OptionList_Masrer = []
        for pos in range(len(masters)):
            OptionList_Masrer.append(masters[pos][0])
        o_vars = []

        ttk.Label(groups_inside_frame, text="Уста Ўргатувчи").grid(row=5, column=0)

        for i in range(3):
            variable_masters = tk.StringVar(groups_inside_frame)
            variable_masters.set(OptionList_Masrer[0])
            o_vars.append(variable_masters)
            opt = ttk.OptionMenu(groups_inside_frame, variable_masters, OptionList_Masrer[0], *OptionList_Masrer)
            opt.config(width=16)
            opt.grid(row=5, column=1+i, pady=10)
        
        def db_groups_add():
            # masters_counter = 0

            # for i, var in enumerate(o_vars):
            #     masters_counter += 1
            #     # print(var.get())

            # checking whether all entries are full
            masters_counter = 1

            if len(groups_number_entry.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(variable_type.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(time_duration_entry.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(variable_l_start.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(variable_l_finish.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(variable_p_start.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(variable_p_finish.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(variable_teacher_name.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(variable_doctor_name.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif masters_counter == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            else:
                # ================= Opening Excel ================ 
                # wbDataBase = xw.Book('DataBase.xlsm')
                wsDataBaseGR = wbDataBase.sheets['DATABASE']
                # Group Datas
                wsDataBaseGR.range("B3").value = groups_number_entry.get()
                wsDataBaseGR.range("D3").value = variable_type.get()
                wsDataBaseGR.range("E3").value = time_duration_entry.get()
                wsDataBaseGR.range("F3").value = cal.get_date()
                wsDataBaseGR.range("H3").value = variable_l_start.get()
                wsDataBaseGR.range("I3").value = variable_l_finish.get()
                wsDataBaseGR.range("J3").value = variable_p_start.get()
                wsDataBaseGR.range("K3").value = variable_p_finish.get()

                # Ustalar
                record_selected = []
                for records in masters_2:
                    if records[0] == variable_teacher_name.get():
                        record_selected = records
                wsDataBaseGR.range("C6").value = [record_selected[0],
                record_selected[1], record_selected[2],record_selected[3]]
                
                record_selected = []
                for records in masters_2:
                    if records[0] == variable_doctor_name.get():
                        record_selected = records
                wsDataBaseGR.range("C7").value = [record_selected[0],
                " ", " ",record_selected[3]]
                
                # O'qituvchilar
                masters_counter = 0
                for i, var in enumerate(o_vars):
                    masters_counter += 1
                    
                    if masters_counter == 1:
                        for records in masters:
                            if records[0] == var.get():
                                record_selected = records
                                wsDataBaseGR.range("C10").value =[record_selected[0],
                                record_selected[1],record_selected[2],record_selected[3],record_selected[4],
                                record_selected[5]]

                    if masters_counter == 2:
                        for records in masters:
                            if records[0] == var.get():
                                record_selected = records
                                wsDataBaseGR.range("C11").value =[record_selected[0],
                                record_selected[1],record_selected[2],record_selected[3],record_selected[4],
                                record_selected[5]]

                    if masters_counter == 3:
                        for records in masters:
                            if records[0] == var.get():
                                record_selected = records
                                wsDataBaseGR.range("C12").value =[record_selected[0],
                                record_selected[1],record_selected[2],record_selected[3],record_selected[4],
                                record_selected[5]]

                
                # Saving File as new Excel
                wbnamedir = "Guruh " + str(groups_number_entry.get())
                wbDataBase.save('groups\{}.xlsm'.format(wbnamedir))
                wbDataBase.close()

                messagebox.showinfo("Муваффақият хабари", "Ўқитувчи маълумотлар базасига муваффақиятли қўшилди!")

            # Remove the old data from cells
            groups_number_entry.delete(0, END)
            time_duration_entry.delete(0, END)
        
        # Button for saving the info into db
        groups_add = ttk.Button(groups_inside_frame, text="Маълумотлар базасига қўшиш", command=db_groups_add)
        groups_add.grid(row=6, column=1, columnspan=2, pady=5)




    def groups_edit(self):
        self.hide_all_frames()
        self.groups_edit_frame.pack(fill="both", expand=1)

        # Create a Notebook
        groups_edit_notebook = ttk.Notebook(self.groups_edit_frame)
        groups_edit_notebook.pack(pady=10, padx=10)

        # Initialize frames for notebooks
        groups_edit_inside_frame = ttk.Frame(groups_edit_notebook)
        groups_edit_inside_frame.pack()

        # Add the notebook
        groups_edit_notebook.add(groups_edit_inside_frame, text="Гуруҳ Янгилаш")

        OptionListForGroupsEdit = [
            "Groups Edit",
            "Umarov",
            "Shavkatov",
            "Usmanov",
            "Rustamov"
        ]

        if len(OptionListForGroupsEdit) == 0:
            messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, аввал гуруҳларни маълумотлар базасига қўшинг!")

        variable_groups_edit = tk.StringVar(groups_edit_inside_frame)
        variable_groups_edit.set(OptionListForGroupsEdit[0])

        opt_g = ttk.OptionMenu(groups_edit_inside_frame, variable_groups_edit, OptionListForGroupsEdit[0], *OptionListForGroupsEdit)
        opt_g.config(width=30)
        opt_g.grid(row=0, column=0, columnspan=4, padx=10, pady=5)

        # "Guruhlar" - Labels, boxes, and OptionMenus
        group_number_label = ttk.Label(groups_edit_inside_frame, text="Гуруҳ №").grid(row=1, column=0)
        groups_number_entry = ttk.Entry(groups_edit_inside_frame)
        groups_number_entry.grid(row=1, column=1, padx=5, pady=10)

        first_name_label = ttk.Label(groups_edit_inside_frame, text="Тоифа").grid(row=1, column=2, padx=10)
        OptionList_Type = ["BC", "A", "B", "C", "D", "BE", "CE", "DE"]
        variable_type = tk.StringVar(groups_edit_inside_frame)
        variable_type.set(OptionList_Type[0])
        opt = ttk.OptionMenu(groups_edit_inside_frame, variable_type, OptionList_Type[0], *OptionList_Type)
        opt.config(width=16)
        opt.grid(row=1, column=3, padx=10, pady=10)

        time_duration_label = ttk.Label(groups_edit_inside_frame, text="  Ўқиш\nМуддати").grid(row=2, column=0)
        time_duration_entry = ttk.Entry(groups_edit_inside_frame)
        time_duration_entry.grid(row=2, column=1, padx=5, pady=10)

        # Add a data picker
        groups_date_label = ttk.Label(groups_edit_inside_frame, text="Сана").grid(row=2, column=2, padx=10)
        cal = DateEntry(groups_edit_inside_frame, width=19, bg="darkblue", fg="white", locale="uz_UZ")
        cal.grid(row=2, column=3, padx=10, pady=10)
        # print(cal.get_date())

        lecture_duration_label = ttk.Label(groups_edit_inside_frame, text="Назарий машғулот\n          соати").grid(row=3, column=0, padx=10)
        OptionList_L_start = ["6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "17", "18", "19", "20"]
        variable_l_start = tk.StringVar(groups_edit_inside_frame)
        variable_l_start.set(OptionList_L_start[0])
        opt = ttk.OptionMenu(groups_edit_inside_frame, variable_l_start, OptionList_L_start[0], *OptionList_L_start)
        opt.config(width=16)
        opt.grid(row=3, column=1, padx=10, pady=10)

        lecture_duration_label_2 = ttk.Label(groups_edit_inside_frame, text="дан / гача").grid(row=3, column=2, padx=5)
        OptionList_L_finish = ["6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "17", "18", "19", "20"]
        variable_l_finish = tk.StringVar(groups_edit_inside_frame)
        variable_l_finish.set(OptionList_L_finish[0])
        opt = ttk.OptionMenu(groups_edit_inside_frame, variable_l_finish, OptionList_L_finish[0], *OptionList_L_finish)
        opt.config(width=16)
        opt.grid(row=3, column=3, padx=10, pady=10)

        practice_duration_label = ttk.Label(groups_edit_inside_frame, text="Амалий машғулот\n         соати").grid(row=4, column=0, padx=10)
        OptionList_P_start = ["6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "17", "18", "19", "20"]
        variable_p_start = tk.StringVar(groups_edit_inside_frame)
        variable_p_start.set(OptionList_P_start[0])
        opt = ttk.OptionMenu(groups_edit_inside_frame, variable_p_start, OptionList_P_start[0], *OptionList_P_start)
        opt.config(width=16)
        opt.grid(row=4, column=1, padx=10, pady=10)

        practice_duration_label_2 = ttk.Label(groups_edit_inside_frame, text="дан / гача").grid(row=4, column=2, padx=5)
        OptionList_P_finish = ["6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "17", "18", "19", "20"]
        variable_p_finish = tk.StringVar(groups_edit_inside_frame)
        variable_p_finish.set(OptionList_P_finish[0])
        opt = ttk.OptionMenu(groups_edit_inside_frame, variable_p_finish, OptionList_P_finish[0], *OptionList_P_finish)
        opt.config(width=16)
        opt.grid(row=4, column=3, padx=10, pady=10)

        teacher_name_label = ttk.Label(groups_edit_inside_frame, text="    Ўқитувчи\nАвто.туз, ЙХК").grid(row=5, column=0)
        OptionList_Teacher = [
            "Teacher", "Alimov", "Zokirov"
        ]
        variable_teacher_name = tk.StringVar(groups_edit_inside_frame)
        variable_teacher_name.set(OptionList_Teacher[0])
        opt = ttk.OptionMenu(groups_edit_inside_frame, variable_teacher_name, OptionList_Teacher[0], *OptionList_Teacher)
        opt.config(width=16)
        opt.grid(row=5, column=1, padx=10, pady=10)

        doctor_name_label = ttk.Label(groups_edit_inside_frame, text="    Ўқитувчи\nТиббий ёрдам").grid(row=5, column=2)
        OptionList_doctor = [
            "Doctor", "Alimov", "Zokirov"
        ]
        variable_doctor_name = tk.StringVar(groups_edit_inside_frame)
        variable_doctor_name.set(OptionList_doctor[0])
        opt = ttk.OptionMenu(groups_edit_inside_frame, variable_doctor_name, OptionList_doctor[0], *OptionList_doctor)
        opt.config(width=16)
        opt.grid(row=5, column=3, padx=10, pady=10)

        # Masters
        OptionList_Masrer = [
            "Master", "Alimov", "Zokirov", "1", "2", "3", "4"
        ]
        o_vars = []

        ttk.Label(groups_edit_inside_frame, text="Уста Ўргатувчи").grid(row=6, column=0)

        for i in range(3):
            variable_masters = tk.StringVar(groups_edit_inside_frame)
            variable_masters.set(OptionList_Masrer[0])
            o_vars.append(variable_masters)
            opt = ttk.OptionMenu(groups_edit_inside_frame, variable_masters, OptionList_Masrer[0], *OptionList_Masrer)
            opt.config(width=16)
            opt.grid(row=6, column=1+i, pady=10)

        def db_groups_edit():
            masters_counter = 0

            for i, var in enumerate(o_vars):
                masters_counter += 1
                # print(var.get())

            # checking whether all entries are full
            if len(groups_number_entry.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(variable_type.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(time_duration_entry.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(variable_l_start.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(variable_l_finish.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(variable_p_start.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(variable_p_finish.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(variable_teacher_name.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif len(variable_doctor_name.get()) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            elif masters_counter == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
            else:
                messagebox.showinfo("Муваффақият хабари", "Ўқитувчи маълумотлар базасига муваффақиятли қўшилди!")

            # Remove the old data from cells
            groups_number_entry.delete(0, END)
            time_duration_entry.delete(0, END)

        groups_edit = ttk.Button(groups_edit_inside_frame, text="Маълумотлар базасини янгилаш", command=db_groups_edit)
        groups_edit.grid(row=7, column=1, columnspan=2, pady=5)

    def groups_delete(self):
        self.hide_all_frames()
        self.groups_delete_frame.pack(fill="both", expand=1)

        param = ttk.Label(self.groups_delete_frame, text="Ўчирмоқчи бўлган гуруҳни танланг: ")
        param.pack(padx=10, pady=10)

        # Showing the list of groups
        OptionList = []
        files_list = os.listdir('groups')
        for item in files_list:
            OptionList.append(item)


        variable = tk.StringVar(self.groups_delete_frame)
        variable.set(OptionList[0])

        opt = ttk.OptionMenu(self.groups_delete_frame, variable, OptionList[0], *OptionList)
        opt.config(width=50)
        opt.pack(side="top")

        labelTest = ttk.Label(self.groups_delete_frame, text="Танланган элемент - {}".format(OptionList[0]))
        labelTest.pack(side="top", pady=10, padx=10)

        def callback(*args):
            labelTest.configure(text="Танланган элемент - {}".format(variable.get()))

        variable.trace("w", callback)

        def delete():
            os.remove("groups/{}".format(variable.get()))
            messagebox.showinfo("Муваффақият хабари", "Гуруҳ маълумотлар базасидан муваффақиятли ўчирилди!")

        # Create a Delete Button
        delete_btn = ttk.Button(self.groups_delete_frame, text="Ўчириш", command=delete)
        delete_btn.pack()

    # Create methods for Database
    def db_groups(self):
        self.hide_all_frames()
        self.db_groups_frame.pack(fill="both", expand=1)
        
        # Create a Notebook
        db_groups_notebook = ttk.Notebook(self.db_groups_frame)
        db_groups_notebook.pack(pady=10, padx=10)

        # Initialize frames for notebooks
        db_groups_frame_inner = ttk.Frame(db_groups_notebook)
        db_groups_frame_inner.pack()

        # Add the notebook
        db_groups_notebook.add(db_groups_frame_inner, text="Барча гуруҳларнинг рўйхати")

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(db_groups_frame_inner)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Showing the list of groups
        files_list = os.listdir('groups')
        files_list_box = tk.Listbox(db_groups_frame_inner, yscrollcommand=scrollbar.set, width=50, height=50, borderwidth=0, highlightthickness=0)
        files_list_box.pack(padx=10, pady=10, side=TOP, anchor=NW)
        # THE ITEMS INSERTED WITH A LOOP
        for item in files_list:
            item = item[:-5]
            files_list_box.insert(END, item)
        
        def show_content(event):
            # MAIN PART 
            # Create a Notebook
            top = tk.Tk()
            top.title("Гурух Инфо")
            top.geometry("600x700+250+150")
            style_top = ThemedStyle(top)
            style_top.set_theme("arc")

            # Creating a Notebook
            top_notebook = ttk.Notebook(top)
            top_notebook.pack(pady=10, padx=10)

            # Initialize frames for notebooks
            doc_frame = ttk.Frame(top_notebook)
            add_frame = ttk.Frame(top_notebook)
            edit_frame = ttk.Frame(top_notebook)
            delete_frame = ttk.Frame(top_notebook)

            # Place the frames on the screen
            doc_frame.pack(fill="both", expand=1)
            add_frame.pack(fill="both", expand=1)
            edit_frame.pack(fill="both", expand=1)
            delete_frame.pack(fill="both", expand=1)

            # Add the notebooks
            top_notebook.add(doc_frame, text="Барча Ҳужжатлар Рўйхати")
            top_notebook.add(add_frame, text="Ўқувчини Қўшиш")
            top_notebook.add(edit_frame, text="Ўқувчини Янгилаш")
            top_notebook.add(delete_frame, text="Ўқувчини Ўчириш")
            
            # ===================== 1-1-1 docs start ====================
            # Addding the widgets to the first doc frame
            # Printing functions - Conncect with Printer
            def print_doc1():
                messagebox.showwarning("Info!", "Printing ... !")

            # create listbox object
            ttk.Label(doc_frame, text="Doc 1").grid(row=0, column=0, padx=10, pady=5)
            doc1 = ttk.Button(doc_frame, text="Print", command=print_doc1)
            doc1.grid(row=0, column=1, padx=10, pady=5)
            # ===================== 1-1-1 docs end =======================

            # ======================= Getting File Dir ===================
            x = files_list_box.curselection()[0]
            # files_list_box.get(x) // Function for getting direction name 

            # ===================== 2-2-2 adding start ===================
            ttk.Label(add_frame, text="Исм").grid(row=1, column=0, padx=10, pady=5)
            ttk.Label(add_frame, text="Фамилия").grid(row=2, column=0, padx=10)
            ttk.Label(add_frame, text="Отчество").grid(row=3, column=0, padx=10)
            ttk.Label(add_frame, text="Тугилган йили").grid(row=4, column=0, padx=10)
            ttk.Label(add_frame, text="Маълумоти").grid(row=5, column=0, padx=10)
            ttk.Label(add_frame, text="Тугилган жойи").grid(row=6, column=0, padx=10)
            ttk.Label(add_frame, text="Турар жойи").grid(row=7, column=0, padx=10)
            ttk.Label(add_frame, text="Бириктирилган ўқитувчи").grid(row=8, column=0, padx=10)
            ttk.Label(add_frame, text="Тугилган жойи туман буйича").grid(row=9, column=0)
            ttk.Label(add_frame, text="Паспортнинг берилган жойи").grid(row=10, column=0, padx=10)
            ttk.Label(add_frame, text="Паспорт серияси").grid(row=11, column=0, padx=10)
            ttk.Label(add_frame, text="Паспортнинг берилган санаси").grid(row=12, column=0, padx=60)
            ttk.Label(add_frame, text="Тиббий кўрикдан ўтган жой").grid(row=13, column=0, padx=10)
            ttk.Label(add_frame, text="Тиб. маъл №").grid(row=14, column=0, padx=10)
            ttk.Label(add_frame, text="Тиб. маъл берилган сана").grid(row=15, column=0, padx=10)
            ttk.Label(add_frame, text="Гувохном серияси").grid(row=16, column=0, padx=10)
            ttk.Label(add_frame, text="Гувохнома № Автомактаб").grid(row=17, column=0, padx=10)
            ttk.Label(add_frame, text="Гувохнома №  РИБ").grid(row=18, column=0, padx=10)
            
            first_name_box = ttk.Entry(add_frame)
            first_name_box.grid(row=1, column=1, pady=3)
            middle_name_box = ttk.Entry(add_frame)
            middle_name_box.grid(row=2, column=1, pady=3)
            last_name_box = ttk.Entry(add_frame)
            last_name_box.grid(row=3, column=1, pady=3)
            cal = DateEntry(add_frame, width=19, bg="darkblue", fg="white", locale="uz_UZ")
            cal.grid(row=4, column=1, pady=3)
            edu_box = ttk.Entry(add_frame)
            edu_box.grid(row=5, column=1, pady=3)
            birth_place_box = ttk.Entry(add_frame)
            birth_place_box.grid(row=6, column=1, pady=3)
            living_place_box = ttk.Entry(add_frame)
            living_place_box.grid(row=7, column=1, pady=3)
            
            # =================== EXCEL OPEN ======================
            # Taking teachers from that Database
            wbDataBaseGR =  xw.Book('groups/{}.xlsm'.format(files_list_box.get(x)))
            wsDataBaseGR = wbDataBaseGR.sheets['DATABASE']

            # Taking Datas from Databse of Groups
            Condition_2 = True
            num = 6
            master_2 = []
            while Condition_2:
                if wsDataBaseGR.cells(num, "C").value is not None:
                    master_2.append(wsDataBaseGR.cells(num, "C").value)
                    master_2.append(wsDataBaseGR.cells(num, "D").value)
                    master_2.append(wsDataBaseGR.cells(num, "E").value)
                    master_2.append(wsDataBaseGR.cells(num, "F").value)
                    num += 1
                else:
                    Condition_2 = False

            masters_2 = [master_2[x:x + 4] for x in range(0, len(master_2), 4)]
            
            OptionList_T = []
            for pos in range(len(masters_2)):
                OptionList_T.append(masters_2[pos][0])
             
            # ====================== not Excel =======================

            variable_t = tk.StringVar(add_frame)
            variable_t.set(OptionList_T[0])
            opt_t = ttk.OptionMenu(add_frame, variable_t, OptionList_T[0], *OptionList_T)
            opt_t.config(width=16)
            opt_t.grid(row=8, column=1, pady=3)

            by_district_box = ttk.Entry(add_frame)
            by_district_box.grid(row=9, column=1, pady=3)
            passport_place_box = ttk.Entry(add_frame)
            passport_place_box.grid(row=10, column=1, pady=3)
            passport_box = ttk.Entry(add_frame)
            passport_box.grid(row=11, column=1, pady=3)
            passport_date_box = DateEntry(add_frame, width=19, bg="darkblue", fg="white", locale="uz_UZ")
            passport_date_box.grid(row=12, column=1, pady=3)
            med_place_box = ttk.Entry(add_frame)
            med_place_box.grid(row=13, column=1, pady=3)
            med_num_box = ttk.Entry(add_frame)
            med_num_box.grid(row=14, column=1, pady=3)
            med_date_box = DateEntry(add_frame, width=19, bg="darkblue", fg="white", locale="uz_UZ")
            med_date_box.grid(row=15, column=1, pady=3)
            doc_num_box = ttk.Entry(add_frame)
            doc_num_box.grid(row=16, column=1, pady=3)
            doc_num_auto_box = ttk.Entry(add_frame)
            doc_num_auto_box.grid(row=17, column=1, pady=3)
            doc_num_rib_box = ttk.Entry(add_frame)
            doc_num_rib_box.grid(row=18, column=1, pady=3)

            def db_students_add():

                # checking whether all entries are entered
                if len(first_name_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(middle_name_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(last_name_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(edu_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(birth_place_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(living_place_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(variable_t.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(by_district_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(passport_place_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(passport_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!") 
                elif len(med_place_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(med_num_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(doc_num_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                # elif len(doc_num_auto_box.get()) == 0:
                #     messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                # elif len(doc_num_rib_box.get()) == 0:
                #     messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                else:
                    Condition = True
                    num = 15
                    while Condition:
                        if wsDataBaseGR.cells(num, "C").value is None:
                            wsDataBaseGR.cells(num, "C").value = [
                                middle_name_box.get() + " " + first_name_box.get() + " " + last_name_box.get(),
                                cal.get_date(), edu_box.get(), birth_place_box.get(),living_place_box.get(),
                                variable_t.get(), by_district_box.get(), passport_place_box.get(),passport_box.get(),
                                passport_date_box.get(), med_place_box.get(),med_num_box.get(),med_date_box.get(),
                                doc_num_box.get(),doc_num_auto_box.get(),doc_num_rib_box.get()
                                ]
                            Condition = False
                        else:
                            num += 1
                    
                    wbDataBaseGR.save()

                    messagebox.showinfo("Муваффақият хабари", "Ўқитувчи маълумотлар базасига муваффақиятли қўшилди!")
                    
                # Removing the old data from cells
                first_name_box.delete(0, END)
                middle_name_box.delete(0, END)
                last_name_box.delete(0, END)
                edu_box.delete(0, END)
                birth_place_box.delete(0, END)
                living_place_box.delete(0, END)
                by_district_box.delete(0, END)
                passport_place_box.delete(0, END)
                passport_box.delete(0, END)
                med_place_box.delete(0, END)
                med_num_box.delete(0, END)
                doc_num_box.delete(0, END)
                doc_num_auto_box.delete(0, END)
                doc_num_rib_box.delete(0, END)
           
            students_add = ttk.Button(add_frame, text="Маълумотлар базасига қўшиш", command=db_students_add)
            students_add.grid(row=19, column=1, pady=5)

            # ===================== 2-2-2 adding end =====================

            # ===================== 3-3-3 editing start ==================
            # Data comes from Excel
            def option_menu_st(*args):
                # Remove the old data from cells
                e_first_name_box.delete(0, END)
                e_middle_name_box.delete(0, END)
                e_last_name_box.delete(0, END)
                e_edu_box.delete(0, END)
                e_birth_place_box.delete(0, END)
                e_living_place_box.delete(0, END)
                e_by_district_box.delete(0, END)
                e_passport_place_box.delete(0, END)
                e_passport_box.delete(0, END)
                e_med_place_box.delete(0, END)
                e_med_num_box.delete(0, END)
                e_doc_num_box.delete(0, END)
                e_doc_num_auto_box.delete(0, END)
                e_doc_num_rib_box.delete(0, END)

                record = []
                for records in masters_2:
                    if records[0] == variable_st.get():
                        record = records
                # print("Records: " + str(record_selected))
                
                e_first_name_box.insert(0, record[0].split()[1])
                e_middle_name_box.insert(0, record[0].split()[0])
                e_last_name_box.insert(0, record[0].split()[2])
                e_edu_box.insert(0, record[2])
                e_birth_place_box.insert(0, record[3])
                e_living_place_box.insert(0, record[4])
                e_by_district_box.insert(0, record[6])
                e_passport_place_box.insert(0, record[7])
                e_passport_box.insert(0, record[8])
                e_med_place_box.insert(0, record[10])
                e_med_num_box.insert(0, record[11])
                e_doc_num_box.insert(0, record[13])
                e_doc_num_auto_box.insert(0, record[14])
                e_doc_num_rib_box.insert(0, record[15])

            # =================== EXCEL OPEN ======================
            # Taking teachers from that Database
            wbDataBaseGR =  xw.Book('groups/{}.xlsm'.format(files_list_box.get(x)))
            wsDataBaseGR = wbDataBaseGR.sheets['DATABASE']

            # Taking Datas from Databse of Groups
            Condition_2 = True
            num = 15
            master_2 = []
            while Condition_2:
                if wsDataBaseGR.cells(num, "C").value is not None:
                    master_2.append(wsDataBaseGR.cells(num, "C").value)
                    master_2.append(wsDataBaseGR.cells(num, "D").value)
                    master_2.append(wsDataBaseGR.cells(num, "E").value)
                    master_2.append(wsDataBaseGR.cells(num, "F").value)
                    master_2.append(wsDataBaseGR.cells(num, "G").value)
                    master_2.append(wsDataBaseGR.cells(num, "H").value)
                    master_2.append(wsDataBaseGR.cells(num, "I").value)
                    master_2.append(wsDataBaseGR.cells(num, "J").value)
                    master_2.append(wsDataBaseGR.cells(num, "K").value)
                    master_2.append(wsDataBaseGR.cells(num, "L").value)
                    master_2.append(wsDataBaseGR.cells(num, "M").value)
                    master_2.append(wsDataBaseGR.cells(num, "N").value)
                    master_2.append(wsDataBaseGR.cells(num, "O").value)
                    master_2.append(wsDataBaseGR.cells(num, "P").value)
                    master_2.append(wsDataBaseGR.cells(num, "Q").value)
                    master_2.append(wsDataBaseGR.cells(num, "R").value)
                    num += 1
                else:
                    Condition_2 = False

            masters_2 = [master_2[x:x + 16] for x in range(0, len(master_2), 16)]

            OptionList_Students = []
            for pos in range(len(masters_2)):
                OptionList_Students.append(masters_2[pos][0])
            
            # ======================= not Excel ======================

            # Cheack whether the list is empty
            if len(OptionList_Students) == 0:
                messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, аввал ўқитувчиларни маълумотлар базасига қўшинг!")

            variable_st = tk.StringVar(edit_frame)
            variable_st.set(OptionList_Students[0])
            opt = ttk.OptionMenu(edit_frame, variable_st, OptionList_Students[0], *OptionList_Students, command=option_menu_st)
            opt.config(width=40)
            opt.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

            ttk.Label(edit_frame, text="Исм").grid(row=1, column=0, padx=10, pady=5)
            ttk.Label(edit_frame, text="Фамилия").grid(row=2, column=0, padx=10)
            ttk.Label(edit_frame, text="Отчество").grid(row=3, column=0, padx=10)
            ttk.Label(edit_frame, text="Тугилган йили").grid(row=4, column=0, padx=10)
            ttk.Label(edit_frame, text="Маълумоти").grid(row=5, column=0, padx=10)
            ttk.Label(edit_frame, text="Тугилган жойи").grid(row=6, column=0, padx=10)
            ttk.Label(edit_frame, text="Турар жойи").grid(row=7, column=0, padx=10)
            ttk.Label(edit_frame, text="Бириктирилган ўқитувчи").grid(row=8, column=0, padx=10)
            ttk.Label(edit_frame, text="Тугилган жойи туман буйича").grid(row=9, column=0)
            ttk.Label(edit_frame, text="Паспортнинг берилган жойи").grid(row=10, column=0, padx=10)
            ttk.Label(edit_frame, text="Паспорт серияси").grid(row=11, column=0, padx=10)
            ttk.Label(edit_frame, text="Паспортнинг берилган санаси").grid(row=12, column=0, padx=60)
            ttk.Label(edit_frame, text="Тиббий кўрикдан ўтган жой").grid(row=13, column=0, padx=10)
            ttk.Label(edit_frame, text="Тиб. маъл №").grid(row=14, column=0, padx=10)
            ttk.Label(edit_frame, text="Тиб. маъл берилган сана").grid(row=15, column=0, padx=10)
            ttk.Label(edit_frame, text="Гувохном серияси").grid(row=16, column=0, padx=10)
            ttk.Label(edit_frame, text="Гувохнома № Автомактаб").grid(row=17, column=0, padx=10)
            ttk.Label(edit_frame, text="Гувохнома №  РИБ").grid(row=18, column=0, padx=10)
            
            # e = edit
            e_first_name_box = ttk.Entry(edit_frame)
            e_first_name_box.grid(row=1, column=1, pady=3)
            e_middle_name_box = ttk.Entry(edit_frame)
            e_middle_name_box.grid(row=2, column=1, pady=3)
            e_last_name_box = ttk.Entry(edit_frame)
            e_last_name_box.grid(row=3, column=1, pady=3)
            e_cal = DateEntry(edit_frame, width=19, bg="darkblue", fg="white", locale="uz_UZ")
            e_cal.grid(row=4, column=1, pady=3)
            e_edu_box = ttk.Entry(edit_frame)
            e_edu_box.grid(row=5, column=1, pady=3)
            e_birth_place_box = ttk.Entry(edit_frame)
            e_birth_place_box.grid(row=6, column=1, pady=3)
            e_living_place_box = ttk.Entry(edit_frame)
            e_living_place_box.grid(row=7, column=1, pady=3)

            e_OptionList_T = ["teach","6", "7", "8"]
            e_variable_t = tk.StringVar(edit_frame)
            e_variable_t.set(OptionList_T[0])
            e_opt_t = ttk.OptionMenu(edit_frame, variable_t, OptionList_T[0], *OptionList_T)
            e_opt_t.config(width=16)
            e_opt_t.grid(row=8, column=1, pady=3)

            e_by_district_box = ttk.Entry(edit_frame)
            e_by_district_box.grid(row=9, column=1, pady=3)
            e_passport_place_box = ttk.Entry(edit_frame)
            e_passport_place_box.grid(row=10, column=1, pady=3)
            e_passport_box = ttk.Entry(edit_frame)
            e_passport_box.grid(row=11, column=1, pady=3)
            e_passport_date_box = DateEntry(edit_frame, width=19, bg="darkblue", fg="white", locale="uz_UZ")
            e_passport_date_box.grid(row=12, column=1, pady=3)
            e_med_place_box = ttk.Entry(edit_frame)
            e_med_place_box.grid(row=13, column=1, pady=3)
            e_med_num_box = ttk.Entry(edit_frame)
            e_med_num_box.grid(row=14, column=1, pady=3)
            e_med_date_box = DateEntry(edit_frame, width=19, bg="darkblue", fg="white", locale="uz_UZ")
            e_med_date_box.grid(row=15, column=1, pady=3)
            e_doc_num_box = ttk.Entry(edit_frame)
            e_doc_num_box.grid(row=16, column=1, pady=3)
            e_doc_num_auto_box = ttk.Entry(edit_frame)
            e_doc_num_auto_box.grid(row=17, column=1, pady=3)
            e_doc_num_rib_box = ttk.Entry(edit_frame)
            e_doc_num_rib_box.grid(row=18, column=1, pady=3)

            def db_students_edit():
                # checking whether all entries are entered
                if len(e_first_name_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(e_middle_name_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(e_last_name_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(e_edu_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(e_birth_place_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(e_living_place_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(e_variable_t.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(e_by_district_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(e_passport_place_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(e_passport_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!") 
                elif len(e_med_place_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(e_med_num_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                elif len(e_doc_num_box.get()) == 0:
                    messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                # elif len(doc_num_auto_box.get()) == 0:
                #     messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                # elif len(doc_num_rib_box.get()) == 0:
                #     messagebox.showwarning("Огоҳлантириш хабари!", "Илтимос, барча ёзувларни тўлдиринг!")
                else:
                    record = []
                    for records in masters_2:
                        if records[0] == variable_st.get():
                            record = records

                    Condition = True
                    num = 15
                    while Condition:
                        if wsDataBaseGR.cells(num, "C").value == record[0]:
                            wsDataBaseGR.cells(num, "C").value = [
                                e_middle_name_box.get() + " " + e_first_name_box.get() + " " + e_last_name_box.get(),
                                e_cal.get_date(), e_edu_box.get(), e_birth_place_box.get(),e_living_place_box.get(),
                                e_variable_t.get(), e_by_district_box.get(), e_passport_place_box.get(),e_passport_box.get(),
                                e_passport_date_box.get(), e_med_place_box.get(),e_med_num_box.get(),e_med_date_box.get(),
                                e_doc_num_box.get(),e_doc_num_auto_box.get(),e_doc_num_rib_box.get()
                                ]
                            Condition = False
                        else:
                            num += 1
                    
                    wbDataBaseGR.save()


                    messagebox.showinfo("Муваффақият хабари", "Ўқитувчи маълумотлар базасига муваффақиятли қўшилди!")
                    
                # Removing the old data from cells
                e_first_name_box.delete(0, END)
                e_middle_name_box.delete(0, END)
                e_last_name_box.delete(0, END)
                e_edu_box.delete(0, END)
                e_birth_place_box.delete(0, END)
                e_living_place_box.delete(0, END)
                e_by_district_box.delete(0, END)
                e_passport_place_box.delete(0, END)
                e_passport_box.delete(0, END)
                e_med_place_box.delete(0, END)
                e_med_num_box.delete(0, END)
                e_doc_num_box.delete(0, END)
                e_doc_num_auto_box.delete(0, END)
                e_doc_num_rib_box.delete(0, END)
           
            students_edit = ttk.Button(edit_frame, text="Маълумотлар базасини янгилаш", command=db_students_edit)
            students_edit.grid(row=19, column=1, pady=5, padx=10)          

            # ===================== 3-3-3 editing end ====================

            # ===================== 4-4-4 deleting start =================
            param = ttk.Label(delete_frame, text="Ўчирмоқчи бўлган ўқитувчини танланг: ")
            param.pack(padx=10, pady=10)

            OptionList_Del_St = ["St1", "St2", "St4"]

            variable_del_st = tk.StringVar(delete_frame)
            variable_del_st.set(OptionList_Del_St[0])

            opt = ttk.OptionMenu(delete_frame, variable_del_st, OptionList_Del_St[0], *OptionList_Del_St)
            opt.config(width=50)
            opt.pack(side="top")

            labelTest = ttk.Label(delete_frame, text="Танланган элемент - {}".format(OptionList_Del_St[0]))
            labelTest.pack(side="top", pady=10, padx=10)

            def callback(*args):
                labelTest.configure(text="Танланган элемент - {}".format(variable_del_st.get()))

            variable_del_st.trace("w", callback)

            def db_students_delete():        
                messagebox.showinfo("Муваффақият хабари", "Ўқитувчи маълумотлар базасидан муваффақиятли ўчирилди!")

            # Create a Delete Button
            delete_st_btn = ttk.Button(delete_frame, text="Ўчириш", command=db_students_delete)
            delete_st_btn.pack()


            # ===================== 4-4-4 deleting end ===================
    
        # Ending part - Opening a new window
        files_list_box.bind("<<ListboxSelect>>", show_content)
        scrollbar.config(command=files_list_box.yview)

    def db_students(self):
        self.hide_all_frames()
        self.db_students_frame.pack(fill="both", expand=1)
        p1 = ttk.Label(self.db_students_frame, text="Students Database")
        p1.pack()

    def db_teachers(self):
        self.hide_all_frames()
        self.db_teachers_frame.pack(fill="both", expand=1)
        p1 = ttk.Label(self.db_teachers_frame, text="Teachers Database")
        p1.pack()

# Info About us
    def info_about(self):
        self.hide_all_frames()
        self.info_about_frame.pack(fill="both", expand=1)
        p1 = ttk.Label(self.info_about_frame, text="About Us")
        p1.pack()


class App(tk.Tk):
    def __init__(self, master):
        tk.Tk.__init__(self)
        self.master = master

        menubar = MenuBar(self)
        self.config(menu=menubar)


# Function for killing excel
def closeFile():
    try:
        os.system('TASKKILL /F /IM excel.exe')
        os.system('TASKKILL /F /IM python.exe')

    except Exception:
        print("KU")


if __name__ == "__main__":
    # Opening Excel File
    #app_xl = xw.App(visible=False)
    wbDataBase = xw.Book('DataBase.xlsm')

    app = App(None)
    app.title("AutoRoad")
    app.geometry("650x550+250+100")
    style = ThemedStyle(app)
    style.set_theme("arc")

    app.mainloop()

    #closeFile() # Closing Excel