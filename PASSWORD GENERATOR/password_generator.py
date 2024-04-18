import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    length = length_var.get()
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)

    window.clipboard_clear()
    window.clipboard_append(password)

    strength = evaluate_strength(password)
    strength_var.set(strength)

def evaluate_strength(password):
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if length >= 12 and has_uppercase and has_lowercase and has_digit and has_special:
        return "Strong"
    elif length >= 8 and (has_uppercase or has_lowercase) and (has_digit or has_special):
        return "Medium"
    else:
        return "Weak"

window = tk.Tk()
window.title("Password Generator")

frame = ttk.Frame(window, padding="20")
frame.grid(row=0, column=0, sticky="nsew")

length_label = ttk.Label(frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
length_var = tk.IntVar(value=12)  
length_entry = ttk.Entry(frame, textvariable=length_var)
length_entry.grid(row=0, column=1, padx=5, pady=5)

generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
result_label = ttk.Label(frame, text="Generated Password:")
result_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
result_entry = ttk.Entry(frame, textvariable=result_var, state="readonly")
result_entry.grid(row=2, column=1, padx=5, pady=5)

strength_var = tk.StringVar()
strength_label = ttk.Label(frame, text="Password Strength:")
strength_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
strength_entry = ttk.Entry(frame, textvariable=strength_var, state="readonly")
strength_entry.grid(row=3, column=1, padx=5, pady=5)

window.mainloop()
