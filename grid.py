""" grid.py
    by Ibrahim Sardar

    NO TESTED YET!
    
"""

#load
import blockBase
#from pygame.locals import *

#resources
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)

#grid class
class grid(object):
    #initializer
    def __init__(self, w, h, wblock, hblock, color):
        #attributes
        pygame.sprite.Sprite.__init__(self)
        self.matrix = []
        self.fillGrid(w, h, wblock, hblock, color)

    # --- update method --- #
    def update(self):
        for i in matrix:
            for j in matrix[i]:
                matrix[i][j].update()

    # --- fills matrix --- #
    def fillGrid(self, w, h, wblock, hblock, color):
        for i in range(w):
            tmp = []
            for j in range(h):
                tmp.append( blockBase(wblock, hblock, color) )
                
                xpadding = (i+1)*2
                ypadding = (j+1)*2
                
                xoffset = xpadding + (i*wblock)
                yoffset = ypadding + (j*yblock)
                
                tmp[j].x = xoffset
                tmp[j].y = yoffset
                
            matrix.append(tmp)

    # --- print grid (for testing) --- #
    def printGrid(self):
        for i in matrix:
            print('\n')
            for j in matrix[i]:
                print( matrix[i][j].x  +  ","  +  matrix[i][j].y  +  " " )
    
# ======================= #
# end grid                #
# ======================= #


if __name__ == "__main__":
    main()
