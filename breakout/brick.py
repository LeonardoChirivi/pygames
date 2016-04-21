import pygame

class Brick:

    color = ( 0, 255, 255 )

    def __init__( self, width, heght ):
        self.width = width
        self.height = height

    def render( self, screen ):
        pygame.draw.rect( screen, self.COLOR, (self.xpos, self.ypos, self.width, self.height) )
