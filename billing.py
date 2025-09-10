#Tkinter Python ka built-in library hai jo GUI (Graphical User Interface) banane ke liye use hota hai.
# importing libraries
import tkinter as tk

def sayHello():
    print("Hello World")

# creating main application window
root = tk.Tk()



# buttons
a = tk.Button(text="click me",command=sayHello)
a.grid(column=1,row=1)

c =tk.Label(text="enter data")
c.grid(column=1,row=2)

b = tk.Entry()
b.grid(column=2,row=2)


#resizing window (in pixels)
root.geometry("300x300")

#changing title 
root.title("Billing system")
# no resizing
root.resizable(True, False)
# running the window
root.mainloop()