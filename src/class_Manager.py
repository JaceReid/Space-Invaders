import pygame, objects

# Methods to create objects that require pygame methods.

def make_enemy(image,x,y,s):
    return objects.enemy(image,x,y,s,image.get_rect(center=(x,y)))

def make_player(image,x,y):
    return objects.player(image, x//2,y-20, 0, image.get_rect(center=(x//2,y-20)))

def make_rocket(image,x,y,a):
    return objects.rocket(image, x, y, a, image.get_rect(center=(x,y))) 


def make_bunker(image,x,y):
    return objects.bunker(image,x,y,image.get_rect(center=(x,y)),4)
    

