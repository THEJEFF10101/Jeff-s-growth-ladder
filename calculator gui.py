import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("calculator")
# Create an entry widget for display
Entry = tk.Entry(root, width=16, font=('arial', 24), borderwidth=2, relief="solid")
Entry.grid(row=0, column=0, columnspan=4)


# Global variable to store the operator and the first number
Operator = ""
First_number = 0


# Function to update the entry widget when a number or operator is pressed
def button_click(value):
    current = Entry.get()
    Entry.delete(0, tk.END)
    Entry.insert(0, current + str(value))


# Function to clear the entry widget
def button_clear():
    Entry.delete(0, tk.END)


# Function to handle the operation
def button_operation(op):
    global Operator
    global First_number
    First_number = float(Entry.get())

    Operator = op
    Entry.delete(0, tk.END)


# Function to calculate the result


def button_equal():
    Second_number = float(Entry.get())
    Entry.delete(0, tk.END)
    if Operator == "+":
        Entry.insert(0, First_number + Second_number)
    elif Operator == "-":
        Entry.insert(0, First_number - Second_number)
    elif Operator == "*":
        Entry.insert(0, First_number * Second_number)
    elif Operator == "/":
        if Second_number != 0:
            Entry.insert(0, First_number / Second_number)
        else:
            Entry.insert(0, "ERROR")



# Define buttons
Button_1 = tk.Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1))
Button_2 = tk.Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2))
Button_3 = tk.Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3))
Button_4 = tk.Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4))
Button_5 = tk.Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5))
Button_6 = tk.Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6))
Button_7 = tk.Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7))
Button_8 = tk.Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8))
Button_9 = tk.Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9))
Button_0 = tk.Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0))
Button_add = tk.Button(root, text="+", padx=20, pady=20, command=lambda: button_operation("+"))
Button_subtract = tk.Button(root, text="-", padx=20, pady=20, command=lambda: button_operation("-"))
Button_multiply = tk.Button(root, text="*", padx=20, pady=20, command=lambda: button_operation("*"))
Button_divide = tk.Button(root, text="/", padx=20, pady=20, command=lambda: button_operation("/"))
Button_equal = tk.Button(root, text="=", padx=20, pady=20, command=button_equal)
Button_clear = tk.Button(root, text="C", padx=20, pady=20, command=button_clear)
# Place buttons on the grid
Button_1.grid(row=3, column=0)
Button_2.grid(row=3, column=1)
Button_3.grid(row=3, column=2)
Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)
Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)
Button_0.grid(row=4, column=0)
Button_add.grid(row=1, column=3)
Button_subtract.grid(row=2, column=3)
Button_multiply.grid(row=3, column=3)
Button_divide.grid(row=4, column=3)
Button_equal.grid(row=4, column=2)
Button_clear.grid(row=4, column=1)
# Start the Tkinter event loop
root.mainloop()
