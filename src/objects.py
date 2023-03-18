import math, pygame, random

class player:
    def __init__(self, image, x, y, a, r):
        self.image = image
        self.x = x
        self.y = y 
        self.a = a
        self.r = r

    def move(self, direction):
        move(self, direction, 1)

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

    def move(self, e):
        if not e:
            a1 = (math.pi/2) - self.a*(math.pi/180) 

            self.x -= 14*math.cos(a1)
            self.y -= 14*math.sin(a1)
        else:
            a1 = (math.pi/2) - self.a*(math.pi/180) 

            self.x -= 14*math.cos(a1)
            self.y += 14*math.sin(a1)
    

class enemy:
    def __init__(self, image, x, y, speed,r):
        self.image = image
        self.x = x
        self.y = y
        self.speed = speed
        self.r = r

    def move(self, direction):
        move(self, direction, self.speed)

    def __str__(self):
        return str(self.x) + " " + str(self.y) + ";  " + str(self.r)

class bunker:
    def __init__(self, image, x,y,r,s):
        self.image = image
        self.x = x
        self.y = y
        self.r = r
        self.s = s

    def damage(self):
        if random.randint(0,3 > 1):
            self.s -= 1

def move(self, direction, amount):
    if direction == 0:
        self.x += amount
            
    elif direction == 1:
        self.x -= amount
    else:
        pass

    self.r = self.image.get_rect(center=(self.x,self.y))
