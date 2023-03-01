import pygame
import ctypes
import time
import math

pygame.init()

#giving the width and height of my python window the values of my computer screen dimensions to enable full screen
myCTypesUser = ctypes.windll.user32
Y = myCTypesUser.GetSystemMetrics(1)
X = myCTypesUser.GetSystemMetrics(0)

#defining fonts
fontA = pygame.font.Font('LCDN.TTF', 50)
fontB = pygame.font.Font('HARLOWSI.TTF', 70)

#defining colours
RED = (255, 0, 0)
GREEN = (0, 153, 0)
background_colour = (32, 32, 32)
BLACK = (0, 0, 0)
Missile_Colour = (167, 255, 34)

#creating the python window with the correct dimensions and colour
screen = pygame.display.set_mode((X, Y))
screen.fill(background_colour)

#function to print any text in a certain font on the screen
def TextRenderFunction(WordsWanted, ColourOfText, centeringCoords, font):
    text1 = font.render(WordsWanted, True, ColourOfText)
    textRect = text1.get_rect()
    textRect.center = centeringCoords
    screen.blit(text1, textRect)

TextRenderFunction('Cosmic Battle', (255, 255, 255), (X // 2, Y // 5), fontB)
TextRenderFunction('Instructions:', GREEN, (X//2, Y//3 -10), fontA)
TextRenderFunction('[A] move left, [S] stop move, [D] move right', GREEN, (X//2, Y//3 + 90), fontA)
TextRenderFunction('[Q] rotate left, [W] stop rotate, [E] rotate right', GREEN, (X//2, Y//3 + 150), fontA)
TextRenderFunction('[SPACE] to shoot', GREEN, (X//2, Y//3 + 210), fontA)
TextRenderFunction('[H] for help', GREEN, (X//2, Y//3 + 270), fontA)
TextRenderFunction('[X] to quit', GREEN, (X//2, Y//3 + 330), fontA)
TextRenderFunction('Press [SPACE] to continue', (255, 255, 255), (X//2, Y//3 + 450), fontA)

#applies changes to the display
pygame.display.flip()

titlescreen = True

#while loop, consisting of the main game controls and core access keys
while titlescreen:

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            #key to press to exit the game
            if event.key == pygame.K_x:
                titlescreen = False

            #key to press to play the game from the home screen
            if event.key == pygame.K_SPACE:

                #creating a new screen for the game itself
                game = True
                titlescreen = False

#new screen for game loop
screen.fill(background_colour)

pygame.display.flip()

#circle design
positionX = X//2
positionY = Y - 30
Radians = ((math.pi)/2)
RadiusOfRotation = 15
TurretLineLength = 12.5

#initiating distance variables
positionXTurretLineBottom = positionX + (math.cos(Radians))*(RadiusOfRotation)
positionYTurretLineBottom = positionY - (math.sin(Radians))*(RadiusOfRotation)
positionXTurretLineTop = positionX + (math.cos(Radians))*(RadiusOfRotation + TurretLineLength)
positionYTurretLineTop = positionY - (math.sin(Radians))*(RadiusOfRotation + TurretLineLength)

#drawing the turret on the screen for the first time
pygame.draw.circle(screen, RED, (positionX, positionY), 30)
pygame.draw.line(screen, BLACK, (positionXTurretLineBottom, (positionYTurretLineBottom)), (positionXTurretLineTop, positionYTurretLineTop), width=5)

#updating the display
pygame.display.flip()

#initialising the movement and rotation booleans as false, as to not trigger any movement without KEYDOWN events
MovingLeftBoolean = False
MovingRightBoolean = False
RotateLeftBoolean = False
RotateRightBoolean = False
MissileShoot = False

def MissileShot(positionXMissile, positionYMissile, AngleOfMissileTravel):

        pygame.draw.circle(screen, background_colour, (positionXMissile, positionYMissile), 5)
        positionXMissile = positionXMissile + math.cos(AngleOfMissileTravel)
        positionYMissile = positionYMissile - math.sin(AngleOfMissileTravel)
        pygame.draw.circle(screen, Missile_Colour, (positionXMissile, positionYMissile), 5)

positionForMissileStartX = positionXTurretLineTop - 1 - math.cos(Radians)
positionForMissileStartY = positionYTurretLineTop - 1 - math.sin(Radians)
AngleForMissileStart = Radians

#entering game loop after exiting the title screen loop
while game:

     for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_x:
                game = False

            if  event.key == pygame.K_a:
                MovingLeftBoolean = True
                MovingRightBoolean = False

            if event.key == pygame.K_d:
                MovingRightBoolean = True
                MovingLeftBoolean = False

            if event.key == pygame.K_s:
                MovingRightBoolean = False
                MovingLeftBoolean = False

            if event.key == pygame.K_q:
                RotateLeftBoolean = True
                RotateRightBoolean = False

            if event.key == pygame.K_e:
                RotateLeftBoolean = False
                RotateRightBoolean = True

            if event.key == pygame.K_w:
                RotateLeftBoolean = False
                RotateRightBoolean = False

            #if event.key == pygame.K_SPACE:
                #MissileShoot = True

     #drawing a new turret and replacing the old one when moved
     if MovingLeftBoolean == True and positionX >= 38:
        pygame.draw.circle(screen, background_colour, (positionX, positionY), 30)
        pygame.draw.line(screen, background_colour, (positionXTurretLineBottom, (positionYTurretLineBottom)),(positionXTurretLineTop, positionYTurretLineTop), width=5)

        #position variable calculations
        positionX = positionX - 4
        positionXTurretLineBottom = positionX + (math.cos(Radians)) * (RadiusOfRotation)
        positionYTurretLineBottom = positionY - (math.sin(Radians)) * (RadiusOfRotation)
        positionXTurretLineTop = positionX + (math.cos(Radians)) * (RadiusOfRotation + TurretLineLength)
        positionYTurretLineTop = positionY - (math.sin(Radians)) * (RadiusOfRotation + TurretLineLength)

        pygame.draw.circle(screen, RED, (positionX, positionY), 30)
        pygame.draw.line(screen, BLACK, (positionXTurretLineBottom, (positionYTurretLineBottom)),(positionXTurretLineTop, positionYTurretLineTop), width=5)

     #drawing a new turret and replacing the old one when moved
     if MovingRightBoolean == True and positionX <= 1500:
        pygame.draw.circle(screen, background_colour, (positionX, positionY), 30)
        pygame.draw.line(screen, background_colour, (positionXTurretLineBottom, (positionYTurretLineBottom)),(positionXTurretLineTop, positionYTurretLineTop), width=5)

        #position variable calculations
        positionX = positionX + 4
        positionXTurretLineBottom = positionX + (math.cos(Radians)) * (RadiusOfRotation)
        positionYTurretLineBottom = positionY - (math.sin(Radians)) * (RadiusOfRotation)
        positionXTurretLineTop = positionX + (math.cos(Radians)) * (RadiusOfRotation + TurretLineLength)
        positionYTurretLineTop = positionY - (math.sin(Radians)) * (RadiusOfRotation + TurretLineLength)

        pygame.draw.circle(screen, RED, (positionX, positionY), 30)
        pygame.draw.line(screen, BLACK, (positionXTurretLineBottom, (positionYTurretLineBottom)),(positionXTurretLineTop, positionYTurretLineTop), width=5)

     #drawing a new turret line and replacing the old one when rotated
     if RotateLeftBoolean == True and Radians <= (math.pi):
        pygame.draw.line(screen, RED, (positionXTurretLineBottom, (positionYTurretLineBottom)),(positionXTurretLineTop, positionYTurretLineTop), width=5)
        Radians = Radians + 0.02

        #position variable calculations
        positionXTurretLineBottom = positionX + (math.cos(Radians)) * (RadiusOfRotation)
        positionYTurretLineBottom = positionY - (math.sin(Radians)) * (RadiusOfRotation)
        positionXTurretLineTop = positionX + (math.cos(Radians)) * (RadiusOfRotation + TurretLineLength)
        positionYTurretLineTop = positionY - (math.sin(Radians)) * (RadiusOfRotation + TurretLineLength)

        pygame.draw.line(screen, BLACK, (positionXTurretLineBottom, (positionYTurretLineBottom)),(positionXTurretLineTop, positionYTurretLineTop), width=5)

     #drawing a new turret line and replacing the old one when rotated
     if RotateRightBoolean == True and Radians >= 0:
        pygame.draw.line(screen, RED, (positionXTurretLineBottom, (positionYTurretLineBottom)),(positionXTurretLineTop, positionYTurretLineTop), width=5)
        Radians = Radians - 0.02

        #position variable calculations
        positionXTurretLineBottom = positionX + (math.cos(Radians)) * (RadiusOfRotation)
        positionYTurretLineBottom = positionY - (math.sin(Radians)) * (RadiusOfRotation)
        positionXTurretLineTop = positionX + (math.cos(Radians)) * (RadiusOfRotation + TurretLineLength)
        positionYTurretLineTop = positionY - (math.sin(Radians)) * (RadiusOfRotation + TurretLineLength)

        pygame.draw.line(screen, BLACK, (positionXTurretLineBottom, (positionYTurretLineBottom)),(positionXTurretLineTop, positionYTurretLineTop), width=5)

     if MissileShoot == True:

         MissileShot(positionForMissileStartX, positionForMissileStartY, AngleForMissileStart)

     #only updates the display if changes have been made, to not overload the program and change the running speed
     if MovingRightBoolean or MovingLeftBoolean or RotateRightBoolean or RotateLeftBoolean:
         pygame.display.flip()

     #allows time for the program to run calculations before runnin the loop again
     pygame.time.wait(15)






