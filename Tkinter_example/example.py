import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter",
                    width=20,
                    height=10)
button = tk.Button(
    text="Click me!",
    width=25,
    height=5)

entry = tk.Entry(width=50)
entry.insert(0, "Python")
name = entry.get()

greeting.pack()
entry.pack()
button.pack()



window.mainloop()

print(name)
