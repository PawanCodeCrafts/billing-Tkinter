#Tkinter Python ka built-in library hai jo GUI (Graphical User Interface) banane ke liye use hota hai.
# importing libraries
import tkinter as tk

def sayHello():
    data = b.get()
    # clear the entry box after getting data
    b.delete(0,tk.END)
    print(data)

# creating main application window
root = tk.Tk()



# buttons --- root matlab window ka naam ki kis window me rakha hai
a = tk.Button(root, text="click me",command=sayHello)
a.grid(column=1,row=3)

c =tk.Label(root, text="enter data")
c.grid(column=1,row=2)

b = tk.Entry(root,)
b.grid(column=2,row=2)




#resizing window (in pixels)
root.geometry("300x300")
#changing title 
root.title("Billing system")
# no resizing
root.resizable(True, False)
# running the window
root.mainloop()