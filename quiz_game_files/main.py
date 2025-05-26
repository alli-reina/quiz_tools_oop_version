import pygame
import sys
from quiz_engine import QuizEngine

pygame.init()

window_size = (1080, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("QUIZ GAME")
game_font = pygame.font.Font("minecraft.ttf", 26)

intro_background_image = pygame.transform.scale(pygame.image.load("intro_background.png"), window_size)
start_button_image = pygame.transform.scale(pygame.image.load("start_button.png"), (200, 80))
start_button_rectangle = start_button_image.get_rect(topleft=(445, 340))

game_clock = pygame.time.Clock()

# Intro screen
is_intro_running = True
while is_intro_running:
    game_clock.tick(60)
    window.blit(intro_background_image, (0, 0))
    window.blit(start_button_image, start_button_rectangle.topleft)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_intro_running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if start_button_rectangle.collidepoint(mouse_position):
                is_intro_running = False

quiz_game = QuizEngine(window, game_font)
quiz_game.run()
pygame.quit()
