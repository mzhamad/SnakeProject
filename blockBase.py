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

//end blockBase class