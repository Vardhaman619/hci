import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    contact = contact_entry.get()
    selected_sport = sports_listbox.get(tk.ACTIVE)
    skill_level = skill_var.get()
    has_equipment = equipment_var.get()
    
    # Validate that required fields are filled
    if not name or not age or not gender or not contact or not selected_sport:
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
    equipment_status = "Yes" if has_equipment else "No"
    messagebox.showinfo(
        "Registration Successful",
        f"Name: {name}\nAge: {age}\nGender: {gender}\nContact: {contact}\n"
        f"Sport: {selected_sport}\nSkill Level: {skill_level}\nOwn Equipment: {equipment_status}"
    )
    
    # Clear fields after submission
    clear_form()

# Function to clear all input fields
def clear_form():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set("")
    contact_entry.delete(0, tk.END)
    sports_listbox.selection_clear(0, tk.END)
    skill_var.set("Beginner")
    equipment_var.set(0)

# Main window
root = tk.Tk()
root.title("Sports Academy Registration Form")
root.geometry("500x600")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="Sports Academy Registration Form", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Participant Name
name_label = tk.Label(root, text="Full Name:")
name_label.pack(pady=5, anchor="w")
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

# Age
age_label = tk.Label(root, text="Age:")
age_label.pack(pady=5, anchor="w")
age_entry = tk.Entry(root, width=40)
age_entry.pack(pady=5)

# Gender (Radio Buttons)
gender_label = tk.Label(root, text="Gender:")
gender_label.pack(pady=5, anchor="w")
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
other_radio = tk.Radiobutton(root, text="Other", variable=gender_var, value="Other")
male_radio.pack(anchor="w")
female_radio.pack(anchor="w")
other_radio.pack(anchor="w")

# Contact Number
contact_label = tk.Label(root, text="Contact Number:")
contact_label.pack(pady=5, anchor="w")
contact_entry = tk.Entry(root, width=40)
contact_entry.pack(pady=5)

# Sport Selection (Listbox)
sport_label = tk.Label(root, text="Select Sport:")
sport_label.pack(pady=5, anchor="w")
sports_listbox = tk.Listbox(root, height=5)
sports = ["Football", "Basketball", "Tennis", "Swimming", "Cricket"]
for sport in sports:
    sports_listbox.insert(tk.END, sport)
sports_listbox.pack(pady=5)

# Skill Level (Radio Buttons)
skill_label = tk.Label(root, text="Skill Level:")
skill_label.pack(pady=5, anchor="w")
skill_var = tk.StringVar(value="Beginner")
beginner_radio = tk.Radiobutton(root, text="Beginner", variable=skill_var, value="Beginner")
intermediate_radio = tk.Radiobutton(root, text="Intermediate", variable=skill_var, value="Intermediate")
advanced_radio = tk.Radiobutton(root, text="Advanced", variable=skill_var, value="Advanced")
beginner_radio.pack(anchor="w")
intermediate_radio.pack(anchor="w")
advanced_radio.pack(anchor="w")

# Equipment Checkbox
equipment_var = tk.IntVar()
equipment_check = tk.Checkbutton(root, text="I have my own equipment", variable=equipment_var)
equipment_check.pack(pady=10)

# Submit and Clear Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)
submit_button = tk.Button(button_frame, text="Submit", command=submit_form, bg="green", fg="white", width=15)
submit_button.grid(row=0, column=0, padx=10)
clear_button = tk.Button(button_frame, text="Clear", command=clear_form, bg="gray", fg="white", width=15)
clear_button.grid(row=0, column=1, padx=10)

# Run the GUI application
root.mainloop()
