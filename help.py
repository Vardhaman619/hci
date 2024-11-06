import tkinter as tk
from tkinter import messagebox

# Function to display a message for contacting support
def contact_support():
    messagebox.showinfo("Contact Support", "For support, email us at support@example.com or call 1-800-123-4567.")

# Main window
root = tk.Tk()
root.title("Help - App Name")
root.geometry("500x600")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="Help", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Section Label: Getting Started
getting_started_label = tk.Label(root, text="Getting Started", font=("Helvetica", 14, "bold"))
getting_started_label.pack(anchor="w", padx=20, pady=(10, 5))

# Getting Started Content
getting_started_text = (
    "1. Download the app and install it on your device.\n"
    "2. Open the app and create an account using your email.\n"
    "3. Log in and complete your profile to get started.\n\n"
    "That's it! You are now ready to explore the app's features."
)
getting_started_label = tk.Label(root, text=getting_started_text, justify="left", wraplength=450)
getting_started_label.pack(anchor="w", padx=20)

# Section Label: Features
features_label = tk.Label(root, text="Features", font=("Helvetica", 14, "bold"))
features_label.pack(anchor="w", padx=20, pady=(10, 5))

# Features Content
features_text = (
    "1. Dashboard: View your activity and recent updates.\n"
    "2. Notifications: Stay updated with real-time notifications.\n"
    "3. Settings: Customize the app according to your preferences.\n"
    "4. Profile: Manage your personal information and preferences."
)
features_label = tk.Label(root, text=features_text, justify="left", wraplength=450)
features_label.pack(anchor="w", padx=20)

# Section Label: FAQs
faqs_label = tk.Label(root, text="FAQs", font=("Helvetica", 14, "bold"))
faqs_label.pack(anchor="w", padx=20, pady=(10, 5))

# Scrollable FAQ Content
faq_content = (
    "Q: How do I reset my password?\n"
    "A: Go to the login screen, click 'Forgot Password' and follow the instructions.\n\n"
    "Q: How do I change my account email?\n"
    "A: Go to Profile > Settings > Account Information to update your email.\n\n"
    "Q: Can I use the app offline?\n"
    "A: Some features are available offline, but most require an internet connection.\n\n"
    "Q: How do I delete my account?\n"
    "A: Contact support to permanently delete your account.\n\n"
)

# Text widget for FAQs
faq_text = tk.Text(root, wrap="word", height=10)
faq_text.insert(tk.END, faq_content)
faq_text.config(state="disabled")  # Make it read-only
faq_text.pack(padx=20, pady=5)

# Contact Support Button
contact_button = tk.Button(root, text="Contact Support", command=contact_support, bg="blue", fg="white", width=15)
contact_button.pack(pady=10)

# Close Help Button
close_button = tk.Button(root, text="Close Help", command=root.destroy, bg="gray", fg="white", width=15)
close_button.pack(pady=10)

# Run the GUI application
root.mainloop()
