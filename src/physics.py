import math

def colision(a,b):
    x = False
    if(abs(a.x - b.x) < 40 and abs(a.y - b.y) < 40):
        x = True

    return x
