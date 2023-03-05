import math

class player:

    def move(obj,dirc):
        if(dirc == 0):
            obj.posx += .1
        elif(dirc == 1):
            obj.posy -= .1
        elif(dirc == 2):
            obj.posx -= .1
        elif(dirc == 3):
            obj.posy += .1
