import pygame

class Brick:

    color = ( 0, 255, 255 )
    xpos = 0
    ypos = 0
    hit = False

    def __init__( self, width, height ):
        self.width = width
        self.height = height

    def render( self, screen ):
        pygame.draw.rect( screen, self.color, (self.xpos, self.ypos, self.width, self.height) )
