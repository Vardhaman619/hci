import tkinter as tk
from tkinter import messagebox

# Function to submit feedback
def submit_feedback():
    name = name_entry.get()
    contact = contact_entry.get()
    taste_rating = taste_var.get()
    quality_rating = quality_var.get()
    presentation_rating = presentation_var.get()
    service_rating = service_var.get()
    comments = comments_text.get("1.0", tk.END).strip()
    
    # Validate that required fields are filled
    if not name or not contact or not taste_rating or not quality_rating or not presentation_rating or not service_rating:
        messagebox.showwarning("Input Error", "Please fill in all required fields.")
        return

    # Display thank you message
    feedback_text = (
        f"Thank you for your feedback, {name}!\n\n"
        f"Taste Rating: {taste_rating}\n"
        f"Quality Rating: {quality_rating}\n"
        f"Presentation Rating: {presentation_rating}\n"
        f"Service Rating: {service_rating}\n\n"
        f"Comments:\n{comments}"
    )
    messagebox.showinfo("Feedback Submitted", feedback_text)

    # Clear form fields after submission
    clear_form()

# Function to clear the form
def clear_form():
    name_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    taste_var.set("")
    quality_var.set("")
    presentation_var.set("")
    service_var.set("")
    comments_text.delete("1.0", tk.END)

# Main window
root = tk.Tk()
root.title("Hotel Food Feedback Form")
root.geometry("500x600")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="Food Feedback Form", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

# Customer Name
name_label = tk.Label(root, text="Full Name:")
name_label.pack(pady=5, anchor="w")
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

# Contact Number
contact_label = tk.Label(root, text="Contact Number:")
contact_label.pack(pady=5, anchor="w")
contact_entry = tk.Entry(root, width=40)
contact_entry.pack(pady=5)

# Ratings (Taste, Quality, Presentation, Service)
rating_frame = tk.Frame(root)
rating_frame.pack(pady=10)

# Taste Rating
taste_label = tk.Label(rating_frame, text="Taste Rating:")
taste_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
taste_var = tk.StringVar()
taste_good = tk.Radiobutton(rating_frame, text="Good", variable=taste_var, value="Good")
taste_avg = tk.Radiobutton(rating_frame, text="Average", variable=taste_var, value="Average")
taste_bad = tk.Radiobutton(rating_frame, text="Bad", variable=taste_var, value="Bad")
taste_good.grid(row=0, column=1, padx=5)
taste_avg.grid(row=0, column=2, padx=5)
taste_bad.grid(row=0, column=3, padx=5)

# Quality Rating
quality_label = tk.Label(rating_frame, text="Quality Rating:")
quality_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
quality_var = tk.StringVar()
quality_good = tk.Radiobutton(rating_frame, text="Good", variable=quality_var, value="Good")
quality_avg = tk.Radiobutton(rating_frame, text="Average", variable=quality_var, value="Average")
quality_bad = tk.Radiobutton(rating_frame, text="Bad", variable=quality_var, value="Bad")
quality_good.grid(row=1, column=1, padx=5)
quality_avg.grid(row=1, column=2, padx=5)
quality_bad.grid(row=1, column=3, padx=5)

# Presentation Rating
presentation_label = tk.Label(rating_frame, text="Presentation Rating:")
presentation_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
presentation_var = tk.StringVar()
presentation_good = tk.Radiobutton(rating_frame, text="Good", variable=presentation_var, value="Good")
presentation_avg = tk.Radiobutton(rating_frame, text="Average", variable=presentation_var, value="Average")
presentation_bad = tk.Radiobutton(rating_frame, text="Bad", variable=presentation_var, value="Bad")
presentation_good.grid(row=2, column=1, padx=5)
presentation_avg.grid(row=2, column=2, padx=5)
presentation_bad.grid(row=2, column=3, padx=5)

# Service Rating
service_label = tk.Label(rating_frame, text="Service Rating:")
service_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)
service_var = tk.StringVar()
service_good = tk.Radiobutton(rating_frame, text="Good", variable=service_var, value="Good")
service_avg = tk.Radiobutton(rating_frame, text="Average", variable=service_var, value="Average")
service_bad = tk.Radiobutton(rating_frame, text="Bad", variable=service_var, value="Bad")
service_good.grid(row=3, column=1, padx=5)
service_avg.grid(row=3, column=2, padx=5)
service_bad.grid(row=3, column=3, padx=5)

# Comments
comments_label = tk.Label(root, text="Additional Comments:")
comments_label.pack(pady=5, anchor="w")
comments_text = tk.Text(root, width=45, height=5)
comments_text.pack(pady=5)

# Submit and Clear Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)
submit_button = tk.Button(button_frame, text="Submit Feedback", command=submit_feedback, bg="blue", fg="white", width=15)
submit_button.grid(row=0, column=0, padx=10)
clear_button = tk.Button(button_frame, text="Clear", command=clear_form, bg="gray", fg="white", width=15)
clear_button.grid(row=0, column=1, padx=10)

# Run the GUI application
root.mainloop()
