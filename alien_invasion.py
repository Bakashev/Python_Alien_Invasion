import sys
import pygame

def run_game():
    """Game initilisation and create object game"""
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    bg_color=(230,230,230)
    pygame.display.set_caption('Alien Invasion')

    #Basic circle run

    while True:
        #Tracking Keyboard and Mouse Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.BUTTON_LEFT:
                pass
        screen.fill(bg_color)
        pygame.display.flip()

run_game()