""" main.py
    by Ibrahim Sardar

    NO TESTED YET!
    
"""

#load
import pygame, userInterface, collisionMaster

#init
pygame.init()

#resources

# -window
WINDOWWIDTH   = 720 #depends on xpadding and blockBase width
WINDOWHEIGHT  = 380 #depends on ypadding and blockBase height
WINDOWCENTER  = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("The Snake Game")

""" userInterface AND collisionMaster WILL USE THESE
# -clock
clock = pygame.time.Clock()

# -keys
_quit    = pygame.QUIT
_esc     = pygame.K_ESCAPE
_p       = pygame.K_P
_up      = pygame.K_UP
_down    = pygame.K_DOWN
_right   = pygame.K_RIGHT
_left    = pygame.K_LEFT
_keydown = pygame.KEYDOWN
"""


#main
def main():

    #make a new UI ***not created yet
    ui = userInterface(WINDOWWIDTH, WINDOWHEIGHT)

    #make a new Control Master ***not created yet
    cm = controlMaster(WINDOWWIDTH, WINDOWHEIGHT)

    #game loop
    while(True):

        #user interface
        ui.run()
        """ PSUEDO
        if gameCondition == -1:
            gameScreen()
        elif gameCondition == 0:
            startScreen()
        elif gameCondition == 1:
            pauseScreen()
        elif gameCondition == 2:
            endScreen()
            quitGame()
        #etc...

        """
        
        #event handle
        cm.events()
        """ PSUEDO
        # --assumming custom events have been created-- #
        for event in pygame.event.get():

            if event.type == _quit:
                ui.quit()

            elif event.type == _keydown:

                # check all possibles of event.key
                # these keys have been pressed
                # /!\ also avoid and act on collisions here...

            elif event.type == _keyup:

                # check all possibles of event.key
                # these keys have been released
                # /!\ ...and here
        """

        #collision handle  -possibly don't need this
        cm.collisions()
        """ PSUEDO
        # --remeber most collisions will be in events-- #
        for x in grid:
            for block in grid[x]:
                if block.property is something
                    do this
                elif ...etc.
        """

        #transfer data between handlers
        ui.obtain(cm.getData())
        """ PSUEDO
        #-cm-
        return (condition, otherStuff)
        #-ui-
        gameCondition = condition
        #(use otherStuff...)
        """

        #update
        ui.update()
        """ PSUEDO
        if gameCondition == -1:
            pass #cm got it
        elif gameCondition == 0:
            startScreen()
        elif gameCondition == 1:
            pauseScreen()
        elif gameCondition == 2:
            endScreen()
            quitGame()
        #etc...
        
        """
        cm.update()
        """ PSUEDO
        if gameCondition == -1:
            windowSurface.fill(GAMECOLOR)
            grid.update()
        elif gameCondition == 0:
            pass #ui got it
        elif gameCondition == 1:
            pass #ui got it
        elif gameCondition == 2:
            pass #ui got it
        #etc...
        
        """
        pygame.display.update()


#if this is file running, run this main
if __name__ == "__main__":
    main()
