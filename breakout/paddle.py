import pygame

class Paddle:

    speed = 7
    COLOR = (255, 255, 255)

    def __init__(self, width, height, xpos, ypos ):
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos

    def move_left(self):
        self.xpos -= self.speed

    def move_right(self):
        self.xpos += self.speed

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
