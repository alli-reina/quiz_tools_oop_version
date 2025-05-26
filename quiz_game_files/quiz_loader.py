class QuizLoader:
    def load_quiz_data(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        quiz_list = []
        current_quiz = {}

        for line in lines:
            line = line.strip()
            if line.startswith("Question:"):
                current_quiz["question"] = line.replace("Question:", "").strip()
            elif line.startswith(("A)", "B)", "C)", "D)")):
                prefix, choice_text = line.split(")", 1)
                choice_key = prefix.strip().lower()
                current_quiz[choice_key] = choice_text.strip()
            elif line.startswith("Answer:"):
                current_quiz["answer"] = line.replace("Answer:", "").strip().lower()
            elif line == "---":
                quiz_list.append(current_quiz)
                current_quiz = {}
        return quiz_list
