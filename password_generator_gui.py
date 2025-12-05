#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
import random
import string


def get_charset_by_complexity(complexity: str) -> str:
    """
    Return character set based on password complexity level.
    Easy   -> lowercase letters only
    Medium -> lowercase + uppercase + digits
    Hard   -> lowercase + uppercase + digits + symbols
    """
    complexity = complexity.lower()

    if complexity == "easy":
        return string.ascii_lowercase
    elif complexity == "medium":
        return string.ascii_lowercase + string.ascii_uppercase + string.digits
    elif complexity == "hard":
        symbols = "!@#$%^&*()-_=+[]{};:,.?/"
        return string.ascii_lowercase + string.ascii_uppercase + string.digits + symbols
    else:
        return ""


def generate_password():
    
    try:
        length = int(length_var.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Password length must be a positive integer.")
        return

    
    complexity = complexity_var.get()
    charset = get_charset_by_complexity(complexity)

    if not charset:
        messagebox.showerror("Error", "Invalid complexity level.")
        return

    password = "".join(random.choice(charset) for _ in range(length))
    password_var.set(password)


def copy_to_clipboard():
    pwd = password_var.get()
    if not pwd:
        messagebox.showinfo("No Password", "Generate a password first.")
        return
    root.clipboard_clear()
    root.clipboard_append(pwd)
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard.")




root = tk.Tk()
root.title("Password Generator")

root.minsize(400, 220)


length_frame = tk.Frame(root)
length_frame.pack(pady=10)

tk.Label(length_frame, text="Password length:").pack(side=tk.LEFT, padx=5)

length_var = tk.StringVar(value="12")
length_entry = tk.Entry(length_frame, textvariable=length_var, width=10)
length_entry.pack(side=tk.LEFT)


complexity_frame = tk.Frame(root)
complexity_frame.pack(pady=5)

tk.Label(complexity_frame, text="Password complexity:").pack(side=tk.LEFT, padx=5)

complexity_var = tk.StringVar(value="Medium")
complexity_options = ["Easy", "Medium", "Hard"]
complexity_menu = tk.OptionMenu(complexity_frame, complexity_var, *complexity_options)
complexity_menu.pack(side=tk.LEFT)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

generate_button = tk.Button(button_frame, text="Generate Password", command=generate_password)
generate_button.pack()


output_frame = tk.Frame(root)
output_frame.pack(pady=10, padx=10, fill="x")

tk.Label(output_frame, text="Generated Password:").pack(anchor="w")

password_var = tk.StringVar()
password_entry = tk.Entry(output_frame, textvariable=password_var, width=45)
password_entry.pack(side=tk.LEFT, padx=(0, 5))

copy_button = tk.Button(output_frame, text="Copy", command=copy_to_clipboard)
copy_button.pack(side=tk.LEFT)


footer_frame = tk.Frame(root)
footer_frame.pack(pady=10)

footer_label = tk.Label(
    footer_frame,
    text="Created by Nawaf Alzanbaqi  |  GitHub: github.com/Nawafalzanbaqi",
    fg="gray"
)
footer_label.pack()

# =====================================================

if __name__ == "__main__":
    root.mainloop()
