import tkinter as tk
from tkinter import messagebox

# Sample questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Human"],
        "answer": "Blue Whale"
    }
]

# Quiz state variables
current_question = 0
score = 0
selected_answer = tk.StringVar()

# Function to display the current question and options
def display_question():
    global current_question
    selected_answer.set(None)  # Reset the selected answer
    question_label.config(text=f"Q{current_question + 1}: {questions[current_question]['question']}")
    
    # Update the options text for checkbuttons
    for i, option in enumerate(questions[current_question]["options"]):
        option_buttons[i].config(text=option, variable=selected_answer, value=option)

# Function to submit the answer and go to the next question
def submit_answer():
    global current_question, score
    selected = selected_answer.get()
    if selected == questions[current_question]["answer"]:
        score += 1
    current_question += 1
    
    # Check if there are more questions
    if current_question < len(questions):
        display_question()
    else:
        messagebox.showinfo("Quiz Completed", f"You scored {score}/{len(questions)}")
        root.quit()  # Exit the quiz

# Function to reset the quiz
def restart_quiz():
    global current_question, score
    current_question = 0
    score = 0
    display_question()

# Main window
root = tk.Tk()
root.title("Online Quiz")
root.geometry("500x400")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="Online Quiz", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

# Question Label
question_label = tk.Label(root, text="", font=("Helvetica", 14), wraplength=450, justify="left")
question_label.pack(pady=20)

# Options (Checkbuttons)
selected_answer = tk.StringVar()
option_buttons = []
for i in range(4):
    option_button = tk.Checkbutton(root, text="", variable=selected_answer, font=("Helvetica", 12), onvalue="", offvalue="")
    option_button.pack(anchor="w", padx=20, pady=5)
    option_buttons.append(option_button)

# Button frame for navigation buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Submit button
submit_button = tk.Button(button_frame, text="Submit", command=submit_answer, bg="blue", fg="white", width=12)
submit_button.grid(row=0, column=0, padx=10)

# Restart button
restart_button = tk.Button(button_frame, text="Restart Quiz", command=restart_quiz, bg="green", fg="white", width=12)
restart_button.grid(row=0, column=1, padx=10)

# Display the first question
display_question()

# Run the GUI application
root.mainloop()
