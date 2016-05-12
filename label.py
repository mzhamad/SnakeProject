""" label.py
    by Ibrahim Sardar
    
"""

class label(pygame.sprite.Sprite):
    #initialize
    def __init__(self, txt, color, pos, font, centered):
        #attributes
        pygame.sprite.Sprite.__init__(self)
        self.txt   = txt
        self.color = color
        self.pos   = pos
        self.font  = font

        self.image = self.font.render(self.txt, True, self.color)
        self.rect  = self.image.get_rect()
        
        #centered text
        if centered == True:
            self.rect.center = self.pos

        #left - aligned text
        if centered == False:
            self.rect.topleft = self.pos

    def update(self):    
        windowSurface.blit(self.image, self.rect)


#if this is file running, run this main
if __name__ == "__main__":
    main()
