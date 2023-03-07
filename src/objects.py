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

class rocket:
    def __init__(self, image, x, y, a, r):
        self.image = image
        self.x = x
        self.y = y 
        self.a = a
        self.r = r

    def move(self):
        a1 = (math.pi/2) - self.a*(math.pi/180) 

        self.x -= 8*math.cos(a1)
        self.y -= abs(8*math.sin(a1))

class enemy:
    def __init__(self, image, x, y, speed,r):
        self.image = image
        self.x = x
        self.y = y
        self.speed = speed
        self.r = r

    def move(self, direction):
        move(self, direction, self.speed)



def move(self, direction, amount):
    if direction == 0:
        self.x += amount
            
    elif direction == 1:
        self.x -= amount
    else:
        pass

    self.r = self.image.get_rect(center=(self.x,self.y))
