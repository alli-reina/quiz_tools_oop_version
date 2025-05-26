from question import Question

class QuizDataManager:
    def __init__(self, filename="quiz.txt"):
        self.filename = filename

    def save_question(self, question: Question):
        if not question.is_valid():
            raise ValueError("Invalid question data.")
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(question.format_for_saving())
