# -*- coding: utf-8 -*-
# pong.py
# A simple 1972 PONG rip off in python
#
# Two players game, move the rigth paddle with w,s and the left with up arrow and down arrow.
#
# author: Leonardo Chirivì
# (c) 2016

import pygame, os, sys, math
from pygame.locals import *
from paddle import Paddle

#setting window position
os.environ['SDL_VIDEO_CENTERED'] = "1"

pygame.init()

#screen set up
WIDTH = 1300
HEIGHT = 600
SURFACE = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('PONG')

#colours set up
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle objects
leftPaddle = Paddle( 13, HEIGHT/5, 15, (2*HEIGHT)/5.0 )
rightPaddle = Paddle( 13, HEIGHT/5, WIDTH-15-13, (2*HEIGHT)/5.0 )

#####ball specs##############
BALL_X = WIDTH/2
BALL_Y = HEIGHT/2
BALL_RADIUS = 13
BALL_X_VEL = 12
BALL_Y_VEL = 12
#############################

#players score
rightScore = 0
leftScore = 0
scored = False

#score font
font = pygame.font.Font( None, 150 )

FPS = 60
clock = pygame.time.Clock()
run = True

pygame.mouse.set_visible(False)

while run:

    SURFACE.fill(BLACK)

    #handling quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or ( event.type == KEYUP and event.key == K_ESCAPE ):
            run = False

    keys = pygame.key.get_pressed()

    #move right paddle up
    if keys[K_w]:
        if leftPaddle.ypos > 0:
            leftPaddle.move_up()

    #move left paddle down
    if keys[K_s]:
        if (leftPaddle.ypos + leftPaddle.height) < HEIGHT:
            leftPaddle.move_down()

    #move right paddle up
    if keys[K_UP]:
        if rightPaddle.ypos > 0:
            rightPaddle.move_up()

    #move right paddle down
    if keys[K_DOWN]:
        if (rightPaddle.ypos + leftPaddle.height) < HEIGHT:
            rightPaddle.move_down()

    #handling ball motion
    if BALL_X <= 0:
        BALL_X = WIDTH/2
        BALL_Y = HEIGHT/2
        rightScore += 1
        scored = True

    elif BALL_X >= WIDTH - BALL_RADIUS:
        BALL_X = WIDTH/2
        BALL_Y = HEIGHT/2
        leftScore += 1
        scored = True

    if BALL_Y <= 0 or BALL_Y >= HEIGHT - BALL_RADIUS:
        BALL_Y_VEL = -BALL_Y_VEL

    #ball - paddle collision detection
    if (  rightPaddle.left() < (BALL_X + BALL_RADIUS) and rightPaddle.right() > (BALL_X - BALL_RADIUS) ) and ( rightPaddle.top() < (BALL_Y + BALL_RADIUS) and rightPaddle.bottom() > (BALL_Y - BALL_RADIUS) ):
        v = 10

        # theta is the angle the ball hits the paddle
        theta = math.pi/2 - (math.atan2( BALL_X, BALL_Y))

        thetaReflection = theta + math.pi/4 * ( ( BALL_Y - leftPaddle.top()/leftPaddle.bottom() ) / ( leftPaddle.height / 2.0 ) )

        # simple trig calcoulates the bouncing trajectory
        if BALL_Y_VEL < 0:
            BALL_Y_VEL = -abs(math.sin( thetaReflection )) * v
        else:
            BALL_Y_VEL = abs(math.sin( thetaReflection )) * v

        BALL_X_VEL = -BALL_X_VEL

    if (  leftPaddle.left() < (BALL_X + BALL_RADIUS) and leftPaddle.right() > (BALL_X - BALL_RADIUS) ) and ( leftPaddle.top() < (BALL_Y + BALL_RADIUS) and leftPaddle.bottom() > (BALL_Y - BALL_RADIUS) ):
        v = 10
        theta = math.pi/2 - (math.atan2( BALL_X, BALL_Y ))
        thetaReflection = theta + math.pi/4 * ( ( BALL_Y - rightPaddle.top()/rightPaddle.bottom() ) / ( rightPaddle.height / 2.0 ) )

        if BALL_Y_VEL < 0:
            BALL_Y_VEL = -abs(math.sin( thetaReflection )) * v
        else:
            BALL_Y_VEL = abs(math.sin( thetaReflection )) * v

        BALL_X_VEL = -BALL_X_VEL

    #render half-field line
    pygame.draw.line( SURFACE, WHITE, ( WIDTH/2, 0 ), ( WIDTH/2, HEIGHT  ) )

    #render the paddles
    leftPaddle.render(SURFACE)
    rightPaddle.render(SURFACE)

    #render the ball
    BALL_X += BALL_X_VEL
    BALL_Y += BALL_Y_VEL
    if scored:
        pygame.time.wait(2000)
        scored = False
    pygame.draw.circle( SURFACE, WHITE, ( int(BALL_X), int(BALL_Y) ), BALL_RADIUS )

    #display players score
    rightScoreDisplay = font.render( "{0}".format(leftScore), 1, WHITE )
    leftScoreDisplay = font.render( "{0}".format(rightScore), 1, WHITE )
    SURFACE.blit( rightScoreDisplay, ( 450, 50 ) )
    SURFACE.blit( leftScoreDisplay, ( 780, 50 ) )

    clock.tick(FPS)
    pygame.display.update()

###########end of game loop#############

pygame.quit()
sys.exit()
