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

L_HEADING = tk.Label(root, text="NAME")
L_HEADING.place(x=20, y = 40)

L_SOFTDRINK = tk.Label(root, text="SoftDrink")
L_SOFTDRINK.place(x=20, y=80)

L_NAMKEEN = tk.Label(root, text="Namkeen")
L_NAMKEEN.place(x=20, y=120)

L_CHIPS = tk.Label(root, text="Chips")
L_CHIPS.place(x=20, y=160)

L_CHOCOLATE = tk.Label(root, text="Chocolate")
L_CHOCOLATE.place(x=20, y=200)

## prices
P_HEADING = tk.Label(root, text="PRICE")
P_HEADING.place(x=100, y = 40)

P_SOFTDRINK = tk.Label(root, text="Rs 20")
P_SOFTDRINK.place(x=100, y=80)

P_NAMKEEN = tk.Label(root, text="Rs 10")
P_NAMKEEN.place(x=100, y=120)

P_CHIPS = tk.Label(root, text="Rs 15")
P_CHIPS.place(x=100, y=160)

P_CHOCOLATE = tk.Label(root, text="Rs 25")
P_CHOCOLATE.place(x=100, y=200)     

## entries

E_HEADING = tk.Label(root, text="QUANTITY")
E_HEADING.place(x=160, y = 40)

E_SOFTDRINK = tk.Entry(root)
E_SOFTDRINK.place(x=160, y=80)

E_NAMKEEN = tk.Entry(root)
E_NAMKEEN.place(x=160, y=120)

E_CHIPS = tk.Entry(root)
E_CHIPS.place(x=160, y=160)

E_CHOCOLATE = tk.Entry(root)
E_CHOCOLATE.place(x=160, y=200)

## calculate bill

CALC_BILL =  tk.Label(root, text="CALCULATE BILL")
CALC_BILL.place(x=350,y=200)








# running the window
root.mainloop()