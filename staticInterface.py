""" staticInterface.py
    by Ibrahim Sardar

    NOT TESTED YET!
    
"""

#handles static graphics (NOT any dynamic graphics)
class staticInterface(object):
    #initializer
    def __init__(self, wwidth, wheight):
        #attributes
        self.wwidth  = wwidth
        self.wheight = wheight
        
        self.gameCondition = -1
        self.labelGroup = pygame.sprite.Group()
        self.screenFill = BLACK
        self.noFill = False

    # --- update method --- #
    def update(self):
        labelGroup.empty()
        
        if gameCondition == 0:
            startScreen()
        elif gameCondition == 1:
            gameScreen()
        elif gameCondition == 2:
            pauseScreen()
        elif gameCondition == 3:
            endScreen()
        
        if noFill == False:
            windowSurface.fill(screenFill)
        labelGroup.update()

    # --- other methods --- #
    def setCondition(self, cond):
        gameCondition = cond

    # --- screens --- #
    def gameScreen(self):
        title = label("SNAKE GAME",
                      GREEN,
                      (6, 6),
                      font1,
                      False)
        score = label("Score:",
                      BLACK,
                      (title.rect.right+12, title.rect.bottom-12),
                      font2,
                      False)
        length = label("Length:",
                       BLACK,
                       (title.rect.right+12, title.rect.bottom),
                       font2,
                       False)
        
        screenFill = WHITE
        noFill = False
        labelGroup.add(title, score, length)

        textBottomLeft = (length.rect.right, title.rect.bottom)
        return textBottomLeft
    
    def startScreen(self):
        title = label("THE SNAKE GAME",
                      WHITE,
                      (wwidth/2, wheight*3/4 ),
                      font1,
                      True)
        info  = label("esc to quit, enter to begin",
                      BLACK,
                      (wwidth/2, wheight*3/4 +50),
                      font2,
                      True)
        info2 = label("p to pause, arrow-keys to move snake",
                      BLACK,
                      (wwidth/2, wheight*3/4 +80),
                      font2,
                      True)
        
        screenFill = GREEEN
        noFill = False
        labelGroup.add(title, info, info2)

    def pauseScreen(self):
        title = label("PAUSED",
                      BLACK,
                      (wwidth/2, wheight*3/4 ),
                      font1,
                      True)
        info  = label("esc to quit, p to resume",
                      BLACK,
                      (wwidth/2, wheight*3/4 +50),
                      font2,
                      True)
        info2 = label("arrow-keys to move snake",
                      BLACK,
                      (wwidth/2, wheight*3/4 +80),
                      font2,
                      True)
        
        noFill = True
        labelGroup.add(title, info, info2)

    def endScreen(self):
        title = label("YOU DIED",
                      RED,
                      (wwidth/2, wheight*3/4 ),
                      font1,
                      True)
        
        noFill = True
        labelGroup.add(title)

    
