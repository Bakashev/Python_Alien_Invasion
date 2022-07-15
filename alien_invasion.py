import sys
import pygame

def run_game():
    """Game initilisation and create object game"""
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Alien Invasion')

    """Basic circle run"""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.BUTTON_LEFT:
                pass
        pygame.display.flip()

run_game()