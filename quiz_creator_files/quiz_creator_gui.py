import tkinter as tk
from tkinter import messagebox
from quiz_creator.question_saver import QuestionSaver

class QuizCreatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz Creator Tool")
        self.root.geometry("400x600")
        self.root.configure(bg="#ffe6f7")

    def run(self):
        self.root.mainloop()
