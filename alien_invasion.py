import sys
import pygame
import settings

def run_game():
    """Game initilisation and create object game"""
    pygame.init()
    ai_setting=settings.Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_high))
    pygame.display.set_caption('Alien Invasion')

    #Basic circle run

    while True:
        #Tracking Keyboard and Mouse Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.K_ESCAPE:
                sys.exit()
        screen.fill(ai_setting.bg_color)
        pygame.display.flip()

run_game()