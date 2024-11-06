import tkinter as tk
from tkinter import messagebox, ttk

# Function to handle form submission
def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    contact = contact_entry.get()
    address = address_entry.get("1.0", tk.END).strip()
    department = department_listbox.get(tk.ACTIVE)
    is_emergency = emergency_var.get()
    
    # Validate that required fields are filled
    if not name or not age or not gender or not contact or not department:
        messagebox.showwarning("Input Error", "Please fill in all required fields.")
        return
    try:
        age = int(age)
        if age <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Age", "Please enter a valid age.")
        return
    
    # Display submitted information
    emergency_status = "Yes" if is_emergency else "No"
    messagebox.showinfo(
        "Registration Successful",
        f"Name: {name}\nAge: {age}\nGender: {gender}\nContact: {contact}\n"
        f"Department: {department}\nEmergency: {emergency_status}\nAddress: {address}"
    )
    
    # Clear fields after submission
    clear_form()

# Function to clear all input fields
def clear_form():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set("")
    contact_entry.delete(0, tk.END)
    address_entry.delete("1.0", tk.END)
    department_listbox.selection_clear(0, tk.END)
    emergency_var.set(0)

# Main window
root = tk.Tk()
root.title("Patient Registration Form")
root.geometry("500x600")
root.resizable(False, False)

# Patient Name
name_label = tk.Label(root, text="Patient Name:")
name_label.pack(pady=5, anchor="w")
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

# Age
age_label = tk.Label(root, text="Age:")
age_label.pack(pady=5, anchor="w")
age_entry = tk.Entry(root, width=40)
age_entry.pack(pady=5)

# Gender (using Checkbuttons)
gender_label = tk.Label(root, text="Gender:")
gender_label.pack(pady=5, anchor="w")
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
other_radio = tk.Radiobutton(root, text="Other", variable=gender_var, value="Other")
male_radio.pack(pady=2, anchor="w")
female_radio.pack(pady=2, anchor="w")
other_radio.pack(pady=2, anchor="w")

# Contact Number
contact_label = tk.Label(root, text="Contact Number:")
contact_label.pack(pady=5, anchor="w")
contact_entry = tk.Entry(root, width=40)
contact_entry.pack(pady=5)

# Address
address_label = tk.Label(root, text="Address:")
address_label.pack(pady=5, anchor="w")
address_entry = tk.Text(root, width=40, height=4)
address_entry.pack(pady=5)

# Department Listbox
department_label = tk.Label(root, text="Department:")
department_label.pack(pady=5, anchor="w")
department_listbox = tk.Listbox(root, height=5)
departments = ["General Medicine", "Pediatrics", "Orthopedics", "Cardiology", "Neurology"]
for dept in departments:
    department_listbox.insert(tk.END, dept)
department_listbox.pack(pady=5)

# Emergency Checkbutton
emergency_var = tk.IntVar()
emergency_check = tk.Checkbutton(root, text="Emergency", variable=emergency_var)
emergency_check.pack(pady=10)

# Submit and Clear Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)
submit_button = tk.Button(button_frame, text="Submit", command=submit_form, bg="green", fg="white", width=15)
submit_button.grid(row=0, column=0, padx=10)
clear_button = tk.Button(button_frame, text="Clear", command=clear_form, bg="gray", fg="white", width=15)
clear_button.grid(row=0, column=1, padx=10)

# Run the GUI application
root.mainloop()
