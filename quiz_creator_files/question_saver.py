class QuestionSaver:
    def __init__(self, file_path="quiz.txt"):
        self.file_path = file_path

    def save_to_file(self, question_text, choices, correct_answer):
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(f"Question: {question_text}\n")
            file.write(f"A) {choices[0]}\n")
            file.write(f"B) {choices[1]}\n")
            file.write(f"C) {choices[2]}\n")
            file.write(f"D) {choices[3]}\n")
            file.write(f"Answer: {correct_answer}\n")
            file.write("---\n")
