import tkinter as tk
from tkinter import messagebox, ttk

# Function to handle fund transfer
def transfer_funds():
    sender = sender_account_entry.get()
    recipient = recipient_account_entry.get()
    amount = amount_entry.get()
    transfer_type = transfer_type_var.get()
    notes = notes_entry.get("1.0", tk.END).strip()
    confirmed = confirm_var.get()
    
    # Check if all required fields are filled and amount is valid
    if not sender or not recipient or not amount or not confirmed:
        messagebox.showwarning("Input Error", "Please fill in all fields and confirm the transfer.")
        return
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Amount", "Please enter a valid amount greater than 0.")
        return
    
    # Simulate a successful transfer
    messagebox.showinfo("Transfer Successful", f"Transferred ${amount:.2f} from {sender} to {recipient} via {transfer_type}.\n\nNotes: {notes}")
    
    # Clear fields after transfer
    clear_fields()

# Function to clear all input fields
def clear_fields():
    sender_account_entry.delete(0, tk.END)
    recipient_account_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    transfer_type_var.set("Bank Transfer")
    notes_entry.delete("1.0", tk.END)
    confirm_var.set(0)

# Create main window
root = tk.Tk()
root.title("Enhanced Fund Transfer")
root.geometry("450x450")
root.resizable(False, False)

# Frame for Sender Information
sender_frame = tk.Frame(root)
sender_frame.pack(pady=10)
sender_account_label = tk.Label(sender_frame, text="Sender Account Number:")
sender_account_label.grid(row=0, column=0, padx=5, pady=5)
sender_account_entry = tk.Entry(sender_frame, width=30)
sender_account_entry.grid(row=0, column=1, padx=5, pady=5)

# Frame for Recipient Information
recipient_frame = tk.Frame(root)
recipient_frame.pack(pady=10)
recipient_account_label = tk.Label(recipient_frame, text="Recipient Account Number:")
recipient_account_label.grid(row=0, column=0, padx=5, pady=5)
recipient_account_entry = tk.Entry(recipient_frame, width=30)
recipient_account_entry.grid(row=0, column=1, padx=5, pady=5)

# Frame for Transfer Details
details_frame = tk.Frame(root)
details_frame.pack(pady=10)

# Transfer Type Dropdown
transfer_type_var = tk.StringVar(value="Bank Transfer")
transfer_type_label = tk.Label(details_frame, text="Transfer Type:")
transfer_type_label.grid(row=0, column=0, padx=5, pady=5)
transfer_type_menu = ttk.Combobox(details_frame, textvariable=transfer_type_var, values=["Bank Transfer", "Mobile Transfer", "Wire Transfer"])
transfer_type_menu.grid(row=0, column=1, padx=5, pady=5)

# Transfer Amount
amount_label = tk.Label(details_frame, text="Amount to Transfer ($):")
amount_label.grid(row=1, column=0, padx=5, pady=5)
amount_entry = tk.Entry(details_frame, width=30)
amount_entry.grid(row=1, column=1, padx=5, pady=5)

# Notes/Description
notes_label = tk.Label(details_frame, text="Transfer Notes:")
notes_label.grid(row=2, column=0, padx=5, pady=5, sticky="n")
notes_entry = tk.Text(details_frame, width=23, height=4)
notes_entry.grid(row=2, column=1, padx=5, pady=5)

# Confirmation Checkbox
confirm_var = tk.IntVar()
confirm_check = tk.Checkbutton(root, text="I confirm the above transfer details", variable=confirm_var)
confirm_check.pack(pady=10)

# Frame for Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)
transfer_button = tk.Button(button_frame, text="Transfer Funds", command=transfer_funds, bg="green", fg="white", width=15)
transfer_button.grid(row=0, column=0, padx=10)
clear_button = tk.Button(button_frame, text="Clear", command=clear_fields, bg="gray", fg="white", width=15)
clear_button.grid(row=0, column=1, padx=10)

# Run the GUI application
root.mainloop()
