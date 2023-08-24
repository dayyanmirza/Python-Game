import tkinter as tk
from tkinter import *
from tkmacosx import Button # https://pypi.org/project/tkmacosx/

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

# https://pypi.org/project/tkmacosx/
button = Button(
    text="Click me!",
    width=200, 
    height=500,
    background="blue",
    foreground="red"
) 
button.pack() # adds button widget to window

window.mainloop()
