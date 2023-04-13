import math

def colision(a,b,d):
    x = False
    if(abs(a.x - b.x) < d and abs(a.y - b.y) < d ):
        x = True

    return x
