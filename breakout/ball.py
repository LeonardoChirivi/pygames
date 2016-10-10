import pygame, math, random

class Ball:

    xspeed = random.choice( [1, -1] )
    yspeed = -6
    color = ( 255, 255, 255 )

    def __init__( self, x, y, radius ):
        self.x = x
        self.y = y
        self.radius = radius

    def update( self, xspeed, yspeed ):
        self.x += int(xspeed)
        self.y += int(yspeed)

    def bounce( self, pad ):
        v = 6

        theta = math.atan2( self.x, self.y )
        thetaReflection = theta - math.pi/2 * ( ( self.x - ( pad.right()+pad.left() ) )/2 )

        if self.xspeed < 0:
            self.xspeed = math.cos( thetaReflection ) * -v
        elif self.xspeed > 0:
            self.xspeed = math.cos( thetaReflection ) * v

        self.yspeed = math.sin( thetaReflection ) * v

    def render( self, screen ):
        pygame.draw.circle( screen, self.color, ( int(self.x), int(self.y) ), self.radius )
