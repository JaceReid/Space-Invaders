import math

#collisions function that detects when the x and y values of two objects are within a certain range of each other and returning the boolean x (True when within range)
def colision(a,b,d):
    x = False
    if(abs(a.x - b.x) < d and abs(a.y - b.y) < d ):
        x = True

    return x
