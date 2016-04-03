# -*- coding: utf-8 -*-
# pong.py
# A simple 1972 PONG rip off in python
#
# author: Leonardo Chirivì
# (c) 2016

import pygame, os, sys, time
from pygame.locals import *

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

#####paddles specs###########
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 130
LEFT_PADDLE_X = 50
LEFT_PADDLE_Y = 150
RIGHT_PADDLE_X = 1250
RIGHT_PADDLE_Y = 150
PADDLE_SPEED = 7
#############################

#creating the two paddle object
leftPaddle = pygame.Rect( LEFT_PADDLE_X, LEFT_PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT )
rightPaddle = pygame.Rect( RIGHT_PADDLE_X, RIGHT_PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT )

#####ball specs##############
BALL_X = WIDTH/2
BALL_Y = HEIGHT/2
BALL_RADIUS = 13
BALL_X_VEL = 10
BALL_Y_VEL = 10
difficoulty = 0
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
        if leftPaddle.top > 0:
            leftPaddle.top -= PADDLE_SPEED

    #move left paddle down
    if keys[K_s]:
        if leftPaddle.bottom < ( HEIGHT - PADDLE_HEIGHT ) :
            leftPaddle.bottom += PADDLE_SPEED

    #move right paddle up
    if keys[K_UP]:
        if rightPaddle.top > 0:
            rightPaddle.top -= PADDLE_SPEED

    #move right paddle down
    if keys[K_DOWN]:
        if rightPaddle.bottom < ( HEIGHT - PADDLE_HEIGHT ):
            rightPaddle.bottom += PADDLE_SPEED

    #handling ball motion
    if BALL_X == 0:
        #BALL_X_VEL = -BALL_X_VEL
        BALL_X = WIDTH/2
        BALL_Y = HEIGHT/2
        leftScore += 1
        scored = True
    elif BALL_X == WIDTH:
        #BALL_X_VEL = -BALL_X_VEL
        BALL_X = WIDTH/2
        BALL_Y = HEIGHT/2
        rightScore += 1
        scored = True
    if BALL_Y == 0 or BALL_Y == HEIGHT:
        BALL_Y_VEL = -BALL_Y_VEL

    #ball- paddle collision detection
    if leftPaddle.collidepoint( BALL_X, BALL_Y ) or rightPaddle.collidepoint( BALL_X, BALL_Y ):
        BALL_X_VEL = -BALL_X_VEL
        #BALL_Y_VEL = -BALL_Y_VEL

    #render half-field line
    pygame.draw.line( SURFACE, WHITE, ( WIDTH / 2, 0 ), ( WIDTH / 2, HEIGHT  ) )

    #render the paddles
    pygame.draw.rect( SURFACE, WHITE, leftPaddle )
    pygame.draw.rect( SURFACE, WHITE, rightPaddle )

    #render the ball
    BALL_X += BALL_X_VEL
    BALL_Y += BALL_Y_VEL
    if scored:
        pygame.time.wait(2000)
        scored = False
    pygame.draw.circle( SURFACE, WHITE, ( BALL_X, BALL_Y ), BALL_RADIUS )

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
