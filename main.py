import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        use_lower = lower_var.get()
        use_upper = upper_var.get()
        use_digits = digit_var.get()
        use_symbols = symbol_var.get()

        character_set = ''
        if use_lower:
            character_set += string.ascii_lowercase
        if use_upper:
            character_set += string.ascii_uppercase
        if use_digits:
            character_set += string.digits
        if use_symbols:
            character_set += string.punctuation

        if character_set == '':
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        password = ''.join(random.choice(character_set) for _ in range(length))
        password_var.set(password)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x250")  # Set window size

# Password length input
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Character type checkboxes
lower_var = tk.BooleanVar()
upper_var = tk.BooleanVar()
digit_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()

lower_check = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var)
lower_check.pack(pady=2)

upper_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var)
upper_check.pack(pady=2)

digit_check = tk.Checkbutton(root, text="Include Digits", variable=digit_var)
digit_check.pack(pady=2)

symbol_check = tk.Checkbutton(root, text="Include Symbols", variable=symbol_var)
symbol_check.pack(pady=2)

# Buttons for generating and copying password
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

generate_button = tk.Button(button_frame, text="Generate Password", command=generate_password)
generate_button.pack(side="left", padx=5)

copy_button = tk.Button(button_frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(side="left", padx=5)

# Password output display
password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, font=("Arial", 12), fg="blue")
password_label.pack(pady=10)

# Start the main event loop
root.mainloop()
