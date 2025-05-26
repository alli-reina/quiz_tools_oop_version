import pygame
import random
from quiz_loader import QuizLoader
from text_wrapper import TextWrapper
from ui_manager import UIManager

class QuizEngine:
    def __init__(self, window, font):
        self.window = window
        self.font = font
        self.clock = pygame.time.Clock()
        self.quiz_data = []
        self.current_question_index = 0
        self.player_score = 0
        self.feedback_message = ""
        self.feedback_start_time = 0
        self.show_feedback = False
        self.choice_hitboxes = {}
        self.ui_manager = UIManager(window, font)
        self.text_wrapper = TextWrapper()

    def load_assets(self):
        self.quiz_background = pygame.transform.scale(pygame.image.load("quiz_template.png"), self.window.get_size())
        self.feedback_background = pygame.transform.scale(pygame.image.load("feedback_template.png"), self.window.get_size())
        self.score_background = pygame.transform.scale(pygame.image.load("score_template.png"), self.window.get_size())

    def run(self):
        self.quiz_data = QuizLoader().load_quiz_data("quiz.txt")
        random.shuffle(self.quiz_data)
        self.load_assets()

        quiz_running = True
        while quiz_running:
            self.clock.tick(60)
            self.window.blit(self.quiz_background, (0, 0))

            if self.current_question_index >= len(self.quiz_data):
                self.ui_manager.draw_score_screen(self.score_background, self.player_score, len(self.quiz_data))
            else:
                current_question = self.quiz_data[self.current_question_index]
                self.choice_hitboxes.clear()

                question_lines = self.text_wrapper.wrap_text_to_fit(current_question["question"], self.font, 600)
                choice_positions = {
                    "a": (179, 390),
                    "b": (593, 390),
                    "c": (179, 490),
                    "d": (599, 490),
                }

                self.ui_manager.draw_question_and_choices(question_lines, current_question, choice_positions, self.choice_hitboxes)

                if self.show_feedback:
                    color = (0, 150, 0) if "Correct" in self.feedback_message else (200, 0, 0)
                    self.ui_manager.draw_feedback(self.feedback_background, self.feedback_message, color)

                    if pygame.time.get_ticks() - self.feedback_start_time > 2000:
                        self.current_question_index += 1
                        self.show_feedback = False

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quiz_running = False
                    pygame.quit()
                    sys.exit()

                if (event.type == pygame.MOUSEBUTTONDOWN
                    and not self.show_feedback
                    and self.current_question_index < len(self.quiz_data)):

                    mouse_position = pygame.mouse.get_pos()
                    for choice_letter, hitbox_rect in self.choice_hitboxes.items():
                        if hitbox_rect.collidepoint(mouse_position):
                            correct_answer = self.quiz_data[self.current_question_index]["answer"]
                            if choice_letter == correct_answer:
                                self.feedback_message = "Correct!"
                                self.player_score += 1
                            else:
                                self.feedback_message = f"WRONG! CORRECT ANSWER IS: {correct_answer.upper()}"
                            self.feedback_start_time = pygame.time.get_ticks()
                            self.show_feedback = True
