import math
import pygame

class player:
    def __init__(self, image, x, y, a, r):
        self.image = image
        self.x = x
        self.y = y 
        self.a = a
        self.r = r

    def move(self, direction):
        move(self, direction, 3)

    def rotate(self, direction):
        if direction == 0:
            self.a += 1.5
        elif(direction == 1):
            self.a -= 1.5
        else:
            pass

        self.r = self.image.get_rect(center=(self.x,self.y))

class enemy:
    def __init__(self, image, x, y,r):
        self.image = image
        self.x = x
        self.y = y
        self.r = r

    def move(self, direction):
        move(self, direction, 1)


def move(self, direction, amount):
    if direction == 0:
        self.x += amount
            
    elif direction == 1:
        self.x -= amount
    else:
        pass

    self.r = self.image.get_rect(center=(self.x,self.y))
