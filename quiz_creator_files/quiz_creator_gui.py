import tkinter as tk
from tkinter import messagebox
from question import Question
from quiz_data_manager import QuizDataManager


class QuizCreatorGUI:
    def __init__(self, root_window, data_manager: QuizDataManager):
        self.root_window = root_window
        self.data_manager = data_manager
        self.root_window.title("Quiz Creator Tool")
        self.root_window.geometry("400x600")
        self.root_window.configure(bg="#ffe6f7")

        self.create_widgets()

    def create_widgets(self):
        # Title and Instructions
        tk.Label(
            self.root_window,
            text="✨Quiz Creator✨",
            font=("Comic Sans MS", 20, "bold"),
            bg="#ffe6f7",
            fg="#9933cc"
        ).pack(pady=10)

        tk.Label(
            self.root_window,
            text="Enter your question below",
            font=("Helvetica", 12),
            bg="#ffe6f7",
            fg="#cc66ff"
        ).pack()

        # Question Entry
        self.entry_question = tk.Entry(self.root_window, width=50, bg="white", fg="#660066")
        self.entry_question.pack(pady=8)

        # Choices
        self.entry_choice_a = self.create_labeled_entry("Choice A:")
        self.entry_choice_b = self.create_labeled_entry("Choice B:")
        self.entry_choice_c = self.create_labeled_entry("Choice C:")
        self.entry_choice_d = self.create_labeled_entry("Choice D:")

        # Correct Answer
        tk.Label(
            self.root_window,
            text="Correct Answer (a/b/c/d):",
            bg="#ffe6f7",
            fg="#cc66ff"
        ).pack(pady=10)

        self.correct_answer_var = tk.StringVar()
        tk.Entry(self.root_window, textvariable=self.correct_answer_var, width=10, bg="white", fg="#660066").pack()

        # Buttons
        tk.Button(
            self.root_window,
            text="💾 Save Question",
            command=self.save_question,
            bg="#cc66ff",
            fg="white",
            font=("Arial", 11, "bold")
        ).pack(pady=15)

        tk.Button(
            self.root_window,
            text="❌ Exit",
            command=self.exit_app,
            bg="#ff6699",
            fg="white",
            font=("Arial", 10, "bold")
        ).pack(pady=5)

    def create_labeled_entry(self, label_text):
        tk.Label(self.root_window, text=label_text, bg="#ffe6f7", fg="#cc66ff").pack()
        entry_field = tk.Entry(self.root_window, width=40, bg="white", fg="#660066")
        entry_field.pack(pady=2)
        return entry_field

    def save_question(self):
        question_text = self.entry_question.get().strip()
        choice_a = self.entry_choice_a.get().strip()
        choice_b = self.entry_choice_b.get().strip()
        choice_c = self.entry_choice_c.get().strip()
        choice_d = self.entry_choice_d.get().strip()
        correct_answer = self.correct_answer_var.get().strip().lower()

        if not all([question_text, choice_a, choice_b, choice_c, choice_d]) or correct_answer not in 'abcd':
            messagebox.showerror("Oops!", "Complete all the fields and use a, b, c or d for the correct answer.")
            return

        question_object = Question(
            question_text=question_text,
            choice_a=choice_a,
            choice_b=choice_b,
            choice_c=choice_c,
            choice_d=choice_d,
            correct_answer=correct_answer
        )

        self.data_manager.save_question(question_object)
        messagebox.showinfo("Saved", "Your question is saved!")
        self.clear_fields()

    def clear_fields(self, event=None):
        self.entry_question.delete(0, tk.END)
        self.entry_choice_a.delete(0, tk.END)
        self.entry_choice_b.delete(0, tk.END)
        self.entry_choice_c.delete(0, tk.END)
        self.entry_choice_d.delete(0, tk.END)
        self.correct_answer_var.set("")

    def exit_app(self):
        confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if confirm:
            self.root_window.destroy()
