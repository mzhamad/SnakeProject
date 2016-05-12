""" main.py
    by Ibrahim Sardar

    NOT TESTED YET!
    
"""

#load
import pygame, staticInterface, dynamicInterface

#init
pygame.init()

#resources
# -colors
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
GREY   = (192, 192, 192)
GREEN  = (  0, 255,   0)
PINK   = (255, 183, 234)
RED    = (255,   0,   0)
ORANGE = (255, 128,   0)
BLUE   = (  0,   0, 255)
BROWN  = (102,  51,   0)
PURPLE = (102,   0, 102)
YELLOW = (255, 255,   0)

# -fonts
font1 = pygame.font.SysFont("aharoni", 72)
font2 = pygame.font.SysFont("comicsansms", 28)
font3 = pygame.font.SysFont("miriamfixed", 12)

# -keys
_quit    = pygame.QUIT
_esc     = pygame.K_ESCAPE
_p       = pygame.K_P
_up      = pygame.K_UP
_down    = pygame.K_DOWN
_right   = pygame.K_RIGHT
_left    = pygame.K_LEFT
_keydown = pygame.KEYDOWN

# -window
WINDOWWIDTH   = 720 #depends on xpadding and blockBase width
WINDOWHEIGHT  = 380 #depends on ypadding and blockBase height
WINDOWCENTER  = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("The Snake Game")

# -clock
clock = pygame.time.Clock()


#main
def main():

    #make a new Static Interface
    si = userInterface(WINDOWWIDTH, WINDOWHEIGHT)

    #make a new Dynamic Interface ***not created yet
    di = dynamicInterface(WINDOWWIDTH, WINDOWHEIGHT)

    #set si to startscreen
    si.setCondition(0)

    #game loop
    while(True):
        
        #event handle
        # basically, readys the variables for an
        # update later depending on user inputs
        di.events()
        """ PSUEDO
        # --assumming custom events have been created-- #
        for event in pygame.event.get():

            if event.type == _quit:
                quit()

            elif event.type == _keydown:

                # check all possibles of event.key
                # these keys have been pressed
                # /!\ also avoid and act on collisions here...

            elif event.type == _keyup:

                # check all possibles of event.key
                # these keys have been released
                # /!\ ...and here
        """

        #transfer data between handlers
        si.setCondition(di.getCondition())

        #update
        si.update() # -blit static graphics first
        di.update() # -then blit dynamic graphics if
                    #  current condition includes them
        pygame.display.update()


#if this is file running, run this main
if __name__ == "__main__":
    main()
