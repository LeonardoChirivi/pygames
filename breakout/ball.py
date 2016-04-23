import pygame, math, random

class Ball:

    xspeed = random.choice( [7, 0, -7, 5, -5] )
    yspeed = -8
    color = ( 255, 255, 255 )

    def __init__( self, x, y, radius ):
        self.x = x
        self.y = y
        self.radius = radius

    def update( self, xspeed, yspeed ):
        self.x += xspeed
        self.y += yspeed

    def bounce( self, pad ):
        v = 8

        theta = math.atan2( self.x, self.y ) + random.randint( 0, 1 )

        thetaReflection = theta + ( math.pi/5 ) / ( ( self.x - ( pad.right()-pad.left() )/2.0 ) / ( pad.width/2.0 ) )

        if self.xspeed < 0:
            self.xspeed = math.cos( thetaReflection ) * -v
        else:
            self.xspeed = math.cos( thetaReflection ) * v

        self.yspeed = -math.sin( thetaReflection ) * v

    def render( self, screen ):
        pygame.draw.circle( screen, self.color, ( int(self.x), int(self.y) ), self.radius )
