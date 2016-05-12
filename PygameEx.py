""" PygameEx.py
    Ibrahim Sardar

    note:  this is just an example for a quick help reference
"""

#load

import pygame, sys, time
from pygame.locals import *

#res
WINDOWWIDTH   = 720
WINDOWHEIGHT  = 380
WINDOWCENTER  = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)

#init
pygame.init()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Pygame Example")
timer = pygame.time.Clock()

class blockBase(pygame.sprite.Sprite):
    #initializer
    def __init__(self, w, h):
        #attributes
        pygame.sprite.Sprite.__init__(self)
        self.setImage(w, h)
        self.color = BLACK

    # --- update method --- #
    def update(self):
        windowSurface.blit(self.image, (self.rect.x, self.rect.y))
        self.image.fill(self.color)

    # --- get/set methods --- #
    def setCenterPosition(self, xPos, yPos):
        self.rect.centerx = xPos
        self.rect.centery = yPos

    def setImage(self, width, height):
        self.image = pygame.Surface((width, height))
        self.rect  = self.image.get_rect()

    def changeSize(self, size):
        xP = self.rect.centerx
        yP = self.rect.centery
        w  = size
        h  = size
        self.setImage(w, h)
        self.rect.centerx = xP
        self.rect.centery = yP
# ======================= #
# end blockBase           #
# ======================= #

def main():

    #track time
    t    = 0.0
    tOld = 0.0

    #block
    block = blockBase(32, 32)
    block.setCenterPosition(WINDOWWIDTH/2, WINDOWHEIGHT/2)

    #game loop
    while(True):

        #some animation
        t  = pygame.time.get_ticks()/1000.0 #get time in seconds (milliseconds/1000)
        dt = t - tOld
        print(t)
        if dt >= 1 and dt < 2:
            block.changeSize(64)
        elif dt >= 2:
            block.changeSize(128)
            tOld = t

        #NOTE: The OS will assume your program is locked up
        #      if program loops with no events being called.
        #
        #event handling
        for event in pygame.event.get(): 

            #QUIT
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #update
        windowSurface.fill(WHITE)
        block.update()
        pygame.display.update()

        #limit: 60 fps
        timer.tick(60)
# ======================= #
# end main                #
# ======================= #


#if this is the file running, run this main
if __name__ == "__main__":
    main()
