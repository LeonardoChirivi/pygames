# -*- coding: utf-8 -*-
# pong.py
# A simple 1972 PONG rip off in python
#
# Class representing the ball object
#
# author: Leonardo Chirivì
# (c) 2016

import pygame, math

class Ball:

    color = (255, 255, 255)
    xspeed = 10
    yspeed = 10

    def __init__( self, x, y, radius ):
        self.x = x
        self.y = y
        self.radius = radius

    def set_xspeed( self, speed ):
        self.xspeed = speed

    def set_yspeed( self, speed ):
        self.yspeed = speed

    def update( self, xspeed, yspeed ):
        self.x += xspeed
        self.y += yspeed

    def bounce( self, pad_top, pad_bottom, pad_height ):
        v = 10
        # theta is the angle the ball hits the paddle
        theta = math.atan2( self.x, self.y )

        #thetaReflection is the angle the ball will bounce off the paddle
        thetaReflection = theta + ( math.pi/4 ) * (  ( self.y - ( pad_bottom + pad_top )/2.0 )   / ( pad_height / 2.0 ) )

        # simple trig calcoulates the bouncing trajectory
        if self.yspeed < 0:
            self.set_yspeed( math.sin( thetaReflection )  * -v )
        else:
            self.set_yspeed( math.sin( thetaReflection )  * v )
        self.set_xspeed( -self.xspeed )

    def render( self, screen ):
        pygame.draw.circle( screen, self.color, ( int(self.x), int(self.y) ), self.radius )
