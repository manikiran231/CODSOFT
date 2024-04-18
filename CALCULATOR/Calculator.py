import tkinter as tk
from tkinter import messagebox

def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_entry.delete(0, tk.END)
        result_entry.insert(0, str(result))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        result_entry.delete(0, tk.END)
        result_entry.insert(0, str(result))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_entry.delete(0, tk.END)
        result_entry.insert(0, str(result))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            raise ZeroDivisionError
        result = num1 / num2
        result_entry.delete(0, tk.END)
        result_entry.insert(0, str(result))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_entry.delete(0, tk.END)


window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x300")
input1_label = tk.Label(window, text="Input 1:")
input1_label.pack(pady=5)  
entry1 = tk.Entry(window)
entry1.pack(pady=5)  

input2_label = tk.Label(window, text="Input 2:")
input2_label.pack(pady=5)  
entry2 = tk.Entry(window)
entry2.pack(pady=5)  

button_frame = tk.Frame(window, bg="#f0f0f0") 
button_frame.pack()

add_button = tk.Button(button_frame, text="Add", command=add, bg="orange")
add_button.pack(side=tk.LEFT, padx=5) 
subtract_button = tk.Button(button_frame, text="Sub", command=subtract, bg="orange")
subtract_button.pack(side=tk.LEFT, padx=5) 
multiply_button = tk.Button(button_frame, text="Mul", command=multiply, bg="orange")
multiply_button.pack(side=tk.LEFT, padx=5)
divide_button = tk.Button(button_frame, text="Div", command=divide, bg="orange")
divide_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(window, text="Clear", command=clear, bg="red", fg="white")
clear_button.pack(pady=5)

result_label = tk.Label(window, text="Result:", bg="#f0f0f0")
result_label.pack(pady=5)  

result_entry = tk.Entry(window, font=("Arial", 12))
result_entry.pack(pady=5)

window.mainloop()
