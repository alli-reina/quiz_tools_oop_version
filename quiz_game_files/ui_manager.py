import pygame

class UIManager:
    def __init__(self, window, font):
        self.window = window
        self.font = font

    def draw_intro_screen(self, background, button_image, button_rect):
        self.window.blit(background, (0, 0))
        self.window.blit(button_image, button_rect.topleft)
        pygame.display.flip()

    def draw_score_screen(self, background, score, total_questions):
        self.window.blit(background, (0, 0))
        score_text = self.font.render(f"You got {score} out of {total_questions} correct!", True, (0, 0, 0))
        x = self.window.get_width() // 2 - score_text.get_width() // 2
        self.window.blit(score_text, (x, 510))

    def draw_question_and_choices(self, question_lines, current_question, positions, choice_hitboxes):
        for i, line in enumerate(question_lines):
            line_surface = self.font.render(line, True, (0, 0, 0))
            self.window.blit(line_surface, (200, 190 + i * 30))

        for letter in ["a", "b", "c", "d"]:
            choice_text = f"{letter.upper()}) {current_question[letter]}"
            choice_surface = self.font.render(choice_text, True, (0, 0, 0))
            rect = choice_surface.get_rect(topleft=positions[letter])
            self.window.blit(choice_surface, rect)
            choice_hitboxes[letter] = rect

    def draw_feedback(self, feedback_background, message, color):
        self.window.blit(feedback_background, (0, 0))
        feedback_surface = self.font.render(message, True, color)
        x = self.window.get_width() // 2 - feedback_surface.get_width() // 2
        self.window.blit(feedback_surface, (x, 230))
