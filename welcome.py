import tkinter as tk
from tkinter import messagebox

# Functions for buttons
def open_login():
    messagebox.showinfo("Login", "Proceeding to Login...")

def open_signup():
    messagebox.showinfo("Sign Up", "Proceeding to Sign Up...")

# Main window
root = tk.Tk()
root.title("Welcome Screen")
root.geometry("500x400")
root.resizable(False, False)

# Background Color
root.config(bg="#f0f0f0")

# Welcome Message
welcome_label = tk.Label(root, text="Welcome to Our App!", font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#333333")
welcome_label.pack(pady=20)

# Description
description_label = tk.Label(
    root, 
    text="Your all-in-one solution for managing your daily tasks.\nStay organized and improve your productivity!",
    font=("Helvetica", 12),
    bg="#f0f0f0",
    fg="#555555",
    justify="center"
)
description_label.pack(pady=10)

# Logo (Optional: Placeholder Image)
# Uncomment below lines if you'd like to add an image as a logo
# from tkinter import PhotoImage
# logo = PhotoImage(file="logo.png")  # Replace with your image path
# logo_label = tk.Label(root, image=logo, bg="#f0f0f0")
# logo_label.pack(pady=10)

# Buttons for Login and Sign Up
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

login_button = tk.Button(
    button_frame, 
    text="Login", 
    command=open_login, 
    font=("Helvetica", 14),
    width=15, 
    bg="#4CAF50", 
    fg="white"
)
login_button.grid(row=0, column=0, padx=10)

signup_button = tk.Button(
    button_frame, 
    text="Sign Up", 
    command=open_signup, 
    font=("Helvetica", 14),
    width=15, 
    bg="#2196F3", 
    fg="white"
)
signup_button.grid(row=0, column=1, padx=10)

# Footer Label (Optional)
footer_label = tk.Label(root, text="Powered by Your Company", font=("Helvetica", 10), bg="#f0f0f0", fg="#999999")
footer_label.pack(side="bottom", pady=20)

# Run the GUI application
root.mainloop()
