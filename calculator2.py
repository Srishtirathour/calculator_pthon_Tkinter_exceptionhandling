import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("CALCULATOR")

label1 = tk.Label(root, text="Enter first number", pady=(10))
label1.pack()

first_number_entry = tk.Entry(root)
first_number_entry.pack()

label2 = tk.Label(root, text="Enter second number", pady=(10))
label2.pack()

second_number_entry = tk.Entry(root)
second_number_entry.pack()

operations = tk.Label(root, text="OPERATIONS", pady=(10))
operations.pack()

def addition():
    first, second = takeValueInput()
    result = first + second
    result_label.config(text='Operations result is:' + str(result))

addition_button = tk.Button(root, text="+", command=lambda: addition())
addition_button.pack()


def subtraction():
    first, second = takeValueInput()
    result = first - second
    result_label.config(text='Operations result is:' + str(result))

subtraction_button = tk.Button(root, text="-", command=lambda: subtraction())
subtraction_button.pack()


def multiplication():
    first, second = takeValueInput()

    result = first * second
    result_label.config(text='Operations result is:' + str(result))

multiplication_button = tk.Button(root, text="*", command=lambda: multiplication())
multiplication_button.pack()


def division():
    first, second = takeValueInput()

    if second ==  0:
        messagebox.showerror("Error", "cannot divide the value by zero")
    else:
        result = first / second
        result = round(result, 2)

    result_label.config(text='Operations result is:' + str(result))

division_button = tk.Button(root, text="/", command=lambda: division())
division_button.pack()

def takeValueInput():
    first = first_number_entry.get()
    second = second_number_entry.get()

    try:
        first = int(first)
        second = int(second)

        return first, second
    except ValueError:
        if ((len(first_number_entry.get()) ==0) or (len(second_number_entry.get()) == 0)):
            messagebox.showerror("Error",  "please enter a value")
        else:
            messagebox.showerror("Error", "enter only integer value")
    quit(0)

result_label = tk.Label(root, text="operation result is:")
result_label.pack()
root.mainloop()

