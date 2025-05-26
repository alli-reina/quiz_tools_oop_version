import tkinter as tk
from quiz_data_manager import QuizDataManager
from quiz_creator_gui import QuizCreatorGUI

if __name__ == "__main__":
    root = tk.Tk()
    data_manager = QuizDataManager()
    app = QuizCreatorGUI(root, data_manager)
    root.mainloop()
