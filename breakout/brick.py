import pygame

class Brick:

    color = ( 0, 255, 255 )
    hit = False

    def __init__( self, width, height, xpos, ypos ):
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos

    def left(self):
        return self.xpos

    def right(self):
        return self.xpos + self.width

    def top(self):
        return self.ypos

    def bottom(self):
        return self.ypos + self.height

    def render( self, screen ):
        pygame.draw.rect( screen, self.color, (self.xpos, self.ypos, self.width, self.height) )
