import tkinter as tk
from tkinter import *
from tkmacosx import Button # https://pypi.org/project/tkmacosx/ Fixes the issue w/ button bg color, so it actually shows the color.

window = tk.Tk()
window.title("Test")
window.geometry("400x400")

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
    height=50,
    bg="blue",
    fg="red"
) 
button.pack() # adds button widget to window

window.mainloop()
