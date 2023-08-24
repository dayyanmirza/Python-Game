from tkinter import *
from tkmacosx import Button
import tkinter as tk

window = tk.Tk()
window.title("Test")

label = tk.Label(
    text="Hello, Tkinter!",
    fg="red",
    bg="blue",
    width=40,
    height=20
    )
label.pack() # adds label widget to window

button = tk.Button( # https://pypi.org/project/ttwidgets/
    text="Click me!",
    width=25, 
    height=5,
    background="blue",
    foreground="red"
) 
button.pack() # adds button widget to window

window.mainloop()
