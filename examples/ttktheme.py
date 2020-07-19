# pip install ttktheme
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk

window = ThemedTk(theme="breeze")
ttk.Label(window, text="hello").pack()
ttk.Button(window, text="Quit", command=window.destroy).pack()
window.mainloop()
