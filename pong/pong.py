# -*- coding: utf-8 -*-
# pong.py
# A simple 1972 PONG rip off in python
#
# Two players game, move the rigth paddle with w,s and the left with up arrow and down arrow.
#
# author: Leonardo Chirivì
# (c) 2016

import pygame, os, sys
from pygame.locals import *
from paddle import Paddle
from ball import Ball

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

# Paddle objects and ball object
leftPaddle = Paddle( 13, HEIGHT/5, 15, (2*HEIGHT)/5.0 )
rightPaddle = Paddle( 13, HEIGHT/5, WIDTH-15-13, (2*HEIGHT)/5.0 )
ball = Ball( WIDTH/2, HEIGHT/2, 13 )

#players score
rightScore = leftScore = 0
scored = False

#score font
font = pygame.font.Font( None, 150 )

FPS = 60
clock = pygame.time.Clock()
run = True

pygame.mouse.set_visible(False)

###########game loop#############

while run:

    SURFACE.fill(BLACK)

    #handling quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or ( event.type == KEYUP and event.key == K_ESCAPE ):
            run = False

    keys = pygame.key.get_pressed()

    #move right paddle up
    if keys[K_w]:
        if leftPaddle.top() > 0:
            leftPaddle.move_up()

    #move left paddle down
    if keys[K_s]:
        if leftPaddle.bottom() < HEIGHT:
            leftPaddle.move_down()

    #move right paddle up
    if keys[K_UP]:
        if rightPaddle.top() > 0:
            rightPaddle.move_up()

    #move right paddle down
    if keys[K_DOWN]:
        if rightPaddle.bottom() < HEIGHT:
            rightPaddle.move_down()

    #handling ball motion
    if ball.x <= 0:
        ball.x, ball.y =  WIDTH/2, HEIGHT/2
        rightScore += 1
        scored = True

    elif ball.x >= WIDTH - ball.radius:
        ball.x, ball.y =  WIDTH/2, HEIGHT/2
        leftScore += 1
        scored = True

    if ball.y <= ball.radius or ball.y >= HEIGHT - ball.radius:
        ball.set_yspeed( -ball.yspeed )

    #ball - paddle collision detection
    if (  rightPaddle.left() < (ball.x + ball.radius) and rightPaddle.right() > (ball.x - ball.radius) ) and ( rightPaddle.top() < (ball.y + ball.radius) and rightPaddle.bottom() > (ball.y - ball.radius) ):
        ball.bounce( rightPaddle.top(), rightPaddle.bottom(), rightPaddle.height )

    if (  leftPaddle.left() < (ball.x + ball.radius) and leftPaddle.right() > (ball.x - ball.radius) ) and ( leftPaddle.top() < (ball.y + ball.radius) and leftPaddle.bottom() > (ball.y - ball.radius) ):
        ball.bounce( leftPaddle.top(), leftPaddle.bottom(), leftPaddle.height )

    #render half-field line
    pygame.draw.line( SURFACE, WHITE, ( WIDTH/2, 0 ), ( WIDTH/2, HEIGHT  ) )

    #render the paddles
    leftPaddle.render(SURFACE)
    rightPaddle.render(SURFACE)

    #render the ball
    ball.update( ball.xspeed, ball.yspeed )
    if scored:
        pygame.time.wait(2000)
        scored = False
    ball.render(SURFACE)

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
