# -*- coding: utf-8 -*-
# pong.py
# A simple 1972 PONG rip off in python
#
# Class representing the paddle object
#
# author: Leonardo Chirivì
# (c) 2016

import pygame

class Paddle:

    speed = 7
    COLOR = (255, 255, 255)

    def __init__(self, width, height, xpos, ypos ):
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos

    def move_up(self):
        self.ypos -= self.speed

    def move_down(self):
        self.ypos += self.speed

    def left(self):
        return self.xpos

    def right(self):
        return self.xpos + self.width

    def top(self):
        return self.ypos

    def bottom(self):
        return self.ypos + self.height

    def render(self, screen):
        pygame.draw.rect( screen, self.COLOR, (self.xpos, self.ypos, self.width, self.height) )
