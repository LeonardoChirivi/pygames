import pygame, os, sys
from pygame.locals import *

os.environ['SDL_VIDEO_CENTERED'] = "1"

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 800
SURFACE = pygame.display.set_mode([ SCREEN_WIDTH, SCREEN_HEIGHT ])
pygame.display.set_caption('Breakout')

FPS = 60
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

def game():

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or ( event.type == KEYUP and event.key == K_ESCAPE ):
                quit_game()

        clock.tick(FPS)
        pygame.display.update()

def quit_game():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    game()
