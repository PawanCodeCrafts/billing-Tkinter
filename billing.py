#Tkinter Python ka built-in library hai jo GUI (Graphical User Interface) banane ke liye use hota hai.
import tkinter as Tk

# create main application window
root = Tk.Tk()
# make label
a = Tk.Label(text="Hello, Tkinter!")
# display label using pack (is se label ko display krte hain)
a.pack()

b = Tk.Label(text="Welcome to Python programming.")
b.pack()

c = Tk.Label(text="I am Pawanpreet")
c.pack()


root.mainloop()