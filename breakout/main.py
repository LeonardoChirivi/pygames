import pygame, os, sys
from pygame.locals import *
from paddle import Paddle
from ball import Ball
from brick import Brick

os.environ['SDL_VIDEO_CENTERED'] = "1"

pygame.init()

#color setup
BLACK = ( 0, 0, 0 )
WHITE = ( 255, 255, 255 )

#surface setup
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 650
SURFACE = pygame.display.set_mode([ SCREEN_WIDTH, SCREEN_HEIGHT ])
pygame.display.set_caption('Breakout')

#initialize players
#paddle:
#                   width        height                  xpos                            ypos
paddle = Paddle( SCREEN_WIDTH/4,   12,     (SCREEN_WIDTH/2)-(SCREEN_WIDTH/4)/2,    SCREEN_HEIGHT - 12 )

#bicks array:
bricks = []
for i in range( 120 ):
    brick = Brick( 13, 5 )
    bricks.append( brick )

FPS = 60
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

###############################################

def game():

    while True:

        SURFACE.fill( BLACK )

        for event in pygame.event.get():
            if event.type == pygame.QUIT or ( event.type == KEYUP and event.key == K_ESCAPE ):
                quit_game()

        keys = pygame.key.get_pressed()

        #handling paddle movement
        if keys[K_LEFT] and paddle.left() > 0:
            paddle.move_left()

        if keys[K_RIGHT] and paddle.right() < SCREEN_WIDTH:
            paddle.move_right()

        #render the briks
        x = 100
        y = 100
        for i in range( 6 ):
            for j in range( 20 ):
                bricks[ i*10 + j ].xpos = x
                bricks[ i*10 + j ].ypos = y
                bricks[ i*10 + j ].render( SURFACE )
                x += 23
            y += 15
            x = 100

        #render the paddle
        paddle.render(SURFACE)

        clock.tick(FPS)
        pygame.display.update()

###############################################

def show_start_screen():
    font = pygame.font.Font( 'freesansbold.ttf', 30 )
    msg = font.render( 'Press any key to play', 1, WHITE )

    while True:

        SURFACE.fill( BLACK )
        SURFACE.blit( msg, ( SCREEN_WIDTH/2+30, SCREEN_HEIGHT/2 ) )

        key_up = pygame.event.get(KEYUP)

        if len( key_up ) > 0:
            pygame.event.get()
            return

        clock.tick(FPS)
        pygame.display.update()

##############################################

def quit_game():
    pygame.quit()
    sys.exit()

#############################################

if __name__ == '__main__':
    #show_start_screen()
    game()
