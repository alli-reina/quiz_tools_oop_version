class Question:
    def __init__(self, question_text, choice_a, choice_b, choice_c, choice_d, correct_answer):
        self.question_text = question_text.strip()
        self.choices = {
            "a": choice_a.strip(),
            "b": choice_b.strip(),
            "c": choice_c.strip(),
            "d": choice_d.strip()
        }
        self.correct_answer = correct_answer.strip().lower()

    def is_valid(self):
        if not self.question_text:
            return False
        if not all(self.choices.values()):
            return False
        if self.correct_answer not in self.choices:
            return False
        return True

    def format_for_saving(self):
        return (
            f"Question: {self.question_text}\n"
            f"A) {self.choices['a']}\n"
            f"B) {self.choices['b']}\n"
            f"C) {self.choices['c']}\n"
            f"D) {self.choices['d']}\n"
            f"Answer: {self.correct_answer}\n"
            "---\n"
        )
