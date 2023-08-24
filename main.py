import tkinter as tk

window = tk.Tk()

label = tk.Label(
    text="Hello, Tkinter!",
    fg="red",
    bg="#34A2FE",
    width=40,
    height=20
    )
label.pack() # adds label widget to window

button = tk.Button(
    text="Click me!",
    width=25, 
    height=5,
    background="blue",
    foreground="red"
) 
button.pack() # adds button widget to window

window.mainloop()

