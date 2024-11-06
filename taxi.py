import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def book_ride():
    pickup = pickup_entry.get()
    dropoff = dropoff_entry.get()
    contact = contact_entry.get()
    cab_type = cab_type_var.get()
    payment_mode = payment_var.get()
    
    # Validate that required fields are filled
    if not pickup or not dropoff or not contact or not cab_type or not payment_mode:
        messagebox.showwarning("Input Error", "Please fill in all required fields.")
        return
    
    # Display booking confirmation
    messagebox.showinfo(
        "Booking Confirmed",
        f"Pick-Up Location: {pickup}\nDrop-Off Location: {dropoff}\nContact Number: {contact}\n"
        f"Cab Type: {cab_type}\nPayment Mode: {payment_mode}\n\nThank you for booking with us!"
    )
    
    # Clear fields after submission
    clear_form()

# Function to clear all input fields
def clear_form():
    pickup_entry.delete(0, tk.END)
    dropoff_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    cab_type_var.set("")
    payment_var.set("")

# Main window
root = tk.Tk()
root.title("Cab/Auto Booking App")
root.geometry("500x500")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="Cab/Auto Booking", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Pick-Up Location
pickup_label = tk.Label(root, text="Pick-Up Location:")
pickup_label.pack(pady=5, anchor="w")
pickup_entry = tk.Entry(root, width=40)
pickup_entry.pack(pady=5)

# Drop-Off Location
dropoff_label = tk.Label(root, text="Drop-Off Location:")
dropoff_label.pack(pady=5, anchor="w")
dropoff_entry = tk.Entry(root, width=40)
dropoff_entry.pack(pady=5)

# Contact Number
contact_label = tk.Label(root, text="Contact Number:")
contact_label.pack(pady=5, anchor="w")
contact_entry = tk.Entry(root, width=40)
contact_entry.pack(pady=5)

# Cab Type (Radio Buttons)
cab_type_label = tk.Label(root, text="Select Cab Type:")
cab_type_label.pack(pady=5, anchor="w")
cab_type_var = tk.StringVar()
auto_radio = tk.Radiobutton(root, text="Auto", variable=cab_type_var, value="Auto")
mini_radio = tk.Radiobutton(root, text="Mini", variable=cab_type_var, value="Mini")
sedan_radio = tk.Radiobutton(root, text="Sedan", variable=cab_type_var, value="Sedan")
suv_radio = tk.Radiobutton(root, text="SUV", variable=cab_type_var, value="SUV")
auto_radio.pack(anchor="w")
mini_radio.pack(anchor="w")
sedan_radio.pack(anchor="w")
suv_radio.pack(anchor="w")

# Payment Mode (Radio Buttons)
payment_label = tk.Label(root, text="Payment Mode:")
payment_label.pack(pady=5, anchor="w")
payment_var = tk.StringVar()
cash_radio = tk.Radiobutton(root, text="Cash", variable=payment_var, value="Cash")
card_radio = tk.Radiobutton(root, text="Credit/Debit Card", variable=payment_var, value="Credit/Debit Card")
upi_radio = tk.Radiobutton(root, text="UPI", variable=payment_var, value="UPI")
cash_radio.pack(anchor="w")
card_radio.pack(anchor="w")
upi_radio.pack(anchor="w")

# Submit and Clear Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)
submit_button = tk.Button(button_frame, text="Book Now", command=book_ride, bg="green", fg="white", width=15)
submit_button.grid(row=0, column=0, padx=10)
clear_button = tk.Button(button_frame, text="Clear", command=clear_form, bg="gray", fg="white", width=15)
clear_button.grid(row=0, column=1, padx=10)

# Run the GUI application
root.mainloop()
