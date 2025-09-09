#Tkinter Python ka built-in library hai jo GUI (Graphical User Interface) banane ke liye use hota hai.
# importing libraries
import tkinter as tk

# creating main application window
root = tk.Tk()

###############################################
################# ROOT FUNCTIONS ##############
###############################################


#resizing the window (in pixels)
root.geometry("300x300")
#changing title of the window -- we can also change icon of the window
root.title("Billing system")



###############################################
################# Label FUNCTIONS #############
###############################################
# make label
# a = tk.Label(text="Hello, Tkinter!")
# # display label using pack (is se label ko display krte hain)
# a.pack()

d = tk.Label(text="raman")
d.grid(column=1, row=1)

b = tk.Label(text="raman")
b.grid(column=1, row=2)










# no resizing
root.resizable(True, False)
# running the window
root.mainloop()