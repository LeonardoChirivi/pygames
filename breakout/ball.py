import pygame

class Ball:

    xspeed = 10
    yspeed = 10
    color = ( 255, 255, 255 )

    def __init__( x, y, radius ):
        self.x = x
        self.y = y
        self.radius = radius

    def update( self, xspeed, yspeed ):
        self.x += xspeed
        self.y += yspeed

    def render( self, screen ):
        pygame.draw.cirlce( screen, self.color, ( int(self.x), int(self.y) ), self.radius )
