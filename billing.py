#Tkinter Python ka built-in library hai jo GUI (Graphical User Interface) banane ke liye use hota hai.
# importing libraries
import tkinter as tk

WINDOW_SIZE_X = 500
WINDOW_SIZE_Y = 300
center = WINDOW_SIZE_X // 2


# creating main application window
root = tk.Tk()

#resizing window (in pixels)
root.geometry(f"{WINDOW_SIZE_X}x{WINDOW_SIZE_Y}")

#changing title 
root.title("Billing system")

# no resizing
root.resizable(True, False)

# label center me 
SOFTWARE_TITLE = "BILLING SYSTEM"
myTitle = tk.Label(text=SOFTWARE_TITLE)
myTitle.place(x=center-50, y=10)


## labels
L_SOFTDRINK = tk.Label(root, text="SoftDrink")
L_SOFTDRINK.place(x=15, y=40)

L_NAMKEEN = tk.Label(root, text="Namkeen")
L_NAMKEEN.place(x=15, y=80)

L_CHIPS = tk.Label(root, text="Chips")
L_CHIPS.place(x=15, y=120)

L_CHOCOLATE = tk.Label(root, text="Chocolate")
L_CHOCOLATE.place(x=15, y=160)

## prices

P_SOFTDRINK = tk.Label(root, text="Rs 20")
P_SOFTDRINK.place(x=150, y=40)

P_NAMKEEN = tk.Label(root, text="Rs 10")
P_NAMKEEN.place(x=150, y=80)

P_CHIPS = tk.Label(root, text="Rs 15")
P_CHIPS.place(x=150, y=120)

P_CHOCOLATE = tk.Label(root, text="Rs 25")
P_CHOCOLATE.place(x=150, y=160)     






# running the window
root.mainloop()