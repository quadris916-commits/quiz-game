import tkinter as tk
from tkinter import messagebox
import random


QUESTION_BANK = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is used for Python programs?",
        "options": ["Python", "Java", "C++", "HTML"],
        "answer": "Python"
    },
    {
        "question": "How many days are there in a week?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["10", "11", "12", "13"],
        "answer": "12"
    },
    {
        "question": "Which animal is called the King of the Jungle?",
        "options": ["Tiger", "Elephant", "Lion", "Leopard"],
        "answer": "Lion"
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "Pacific"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Computer Power Unit", "Central Print Unit", "Control Processing Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which gas do plants take in?",
        "options": ["Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "How many continents are there?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Shakespeare", "Dickens", "Tagore", "Tolstoy"],
        "answer": "Shakespeare"
    },
    {
        "question": "Which is the national bird of India?",
        "options": ["Parrot", "Peacock", "Eagle", "Crow"],
        "answer": "Peacock"
    },
    {
        "question": "What is 9 x 3?",
        "options": ["18", "27", "21", "24"],
        "answer": "27"
    },
    {
        "question": "Which instrument measures temperature?",
        "options": ["Barometer", "Thermometer", "Speedometer", "Ammeter"],
        "answer": "Thermometer"
    },
    {
        "question": "Which country is famous for the pyramids?",
        "options": ["India", "Greece", "Egypt", "Mexico"],
        "answer": "Egypt"
    },
    {
        "question": "Which part of the plant conducts photosynthesis?",
        "options": ["Root", "Stem", "Leaf", "Flower"],
        "answer": "Leaf"
    },
    {
        "question": "Which is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": "2"
    },
    {
        "question": "What is the boiling point of water?",
        "options": ["50°C", "100°C", "120°C", "90°C"],
        "answer": "100°C"
    },
    {
        "question": "Which device is used to point on a computer screen?",
        "options": ["Keyboard", "Mouse", "Monitor", "Printer"],
        "answer": "Mouse"
    },
    {
        "question": "Which festival is known as the festival of lights?",
        "options": ["Holi", "Eid", "Diwali", "Christmas"],
        "answer": "Diwali"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["6", "7", "8", "9"],
        "answer": "8"
    },
    {
        "question": "Which blood group is known as the universal donor?",
        "options": ["A", "B", "AB", "O negative"],
        "answer": "O negative"
    },
    {
        "question": "Which is the fastest land animal?",
        "options": ["Horse", "Tiger", "Cheetah", "Deer"],
        "answer": "Cheetah"
    },
    {
        "question": "Who invented the light bulb?",
        "options": ["Newton", "Tesla", "Edison", "Galileo"],
        "answer": "Edison"
    },
    {
        "question": "Which is the largest mammal?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "answer": "Blue Whale"
    }
]


class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("700x500")
        self.root.configure(bg="#1e1e1e")

        self.score = 0
        self.question_number = 0
        self.selected_questions = random.sample(QUESTION_BANK, 10)

        self.score_label = tk.Label(
            root,
            text="Score: 0/10",
            font=("Arial", 16, "bold"),
            bg="#1e1e1e",
            fg="white"
        )
        self.score_label.pack(pady=10)

        self.progress_label = tk.Label(
            root,
            text="Question 1 of 10",
            font=("Arial", 12),
            bg="#1e1e1e",
            fg="#bbbbbb"
        )
        self.progress_label.pack()

        self.question_label = tk.Label(
            root,
            text="",
            font=("Arial", 18, "bold"),
            wraplength=650,
            justify="left",
            bg="#1e1e1e",
            fg="white"
        )
        self.question_label.pack(pady=30)

        self.selected_option = tk.StringVar()
        self.option_buttons = []

        for i in range(4):
            btn = tk.Radiobutton(
                root,
                text="",
                variable=self.selected_option,
                value="",
                font=("Arial", 14),
                wraplength=600,
                justify="left",
                anchor="w",
                padx=20,
                bg="#2d2d2d",
                fg="white",
                selectcolor="#444444",
                activebackground="#2d2d2d",
                activeforeground="white",
                width=45
            )
            btn.pack(pady=5, fill="x", padx=40)
            self.option_buttons.append(btn)

        self.next_button = tk.Button(
            root,
            text="Next",
            font=("Arial", 14, "bold"),
            bg="#4CAF50",
            fg="white",
            command=self.next_question
        )
        self.next_button.pack(pady=30)

        self.load_question()

    def load_question(self):
        self.selected_option.set("")
        current = self.selected_questions[self.question_number]

        self.question_label.config(text=current["question"])
        self.progress_label.config(text=f"Question {self.question_number + 1} of 10")

        for i, option in enumerate(current["options"]):
            self.option_buttons[i].config(text=option, value=option)

    def next_question(self):
        if self.selected_option.get() == "":
            messagebox.showwarning("No Selection", "Please choose an answer.")
            return

        current = self.selected_questions[self.question_number]

        if self.selected_option.get() == current["answer"]:
            self.score += 1

        self.question_number += 1
        self.score_label.config(text=f"Score: {self.score}/10")

        if self.question_number < 10:
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        for btn in self.option_buttons:
            btn.pack_forget()
        self.next_button.pack_forget()

        self.question_label.config(
            text=f"Quiz Finished!\nYour final score is {self.score}/10"
        )
        self.progress_label.config(text="Completed")
        self.score_label.config(text=f"Final Score: {self.score}/10")

        restart_button = tk.Button(
            self.root,
            text="Play Again",
            font=("Arial", 14, "bold"),
            bg="#2196F3",
            fg="white",
            command=self.restart_quiz
        )
        restart_button.pack(pady=20)

    def restart_quiz(self):
        self.score = 0
        self.question_number = 0
        self.selected_questions = random.sample(QUESTION_BANK, 10)

        for widget in self.root.winfo_children():
            widget.destroy()

        self.__init__(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()