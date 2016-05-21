""" blockBase.py
"""

#load
import pygame

#init
pygame.init()

#window
WINDOWWIDTH   = 720
WINDOWHEIGHT  = 380
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

#blockBase
class blockBase(pygame.sprite.Sprite):
    #initializer
    def __init__(self, color, w, h):
        #attributes
        pygame.sprite.Sprite.__init__(self)
        self.setImage(w, h)
        self.color = color

    # --- update method --- #
    def update(self):
        windowSurface.blit(self.image, (self.rect.x, self.rect.y))
        self.image.fill(self.color)

    # --- get/set methods --- #
    def setCenterPos(self, xPos, yPos):
        self.rect.centerx = xPos
        self.rect.centery = yPos

    def setImage(self, width, height):
        self.image = pygame.Surface((width, height))
        self.rect  = self.image.get_rect()

#end blockBase class
