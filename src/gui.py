# Import need modules
import pygame, sys, objects, time, math, random
from button import Button
import physics, main


# Intialize pygame and get screen size
pygame.init() 
screen = pygame.display.set_mode()
area = screen.get_rect()
a,b,x,y = area

pygame.display.set_caption("Menu")

BG = pygame.image.load("resources/images/game.png")
game_bg = pygame.image.load("resources/images/bg.png")

def update(): #Update the display
    pygame.display.update()

def get_font(size): #sets the font
    return pygame.font.Font("resources/fonts/LCDN.TTF", size)

def get_area(): # get display area

    xy = [x,y]

    return xy

def draw_object(a,r): # Draw an object with pygame
    screen.blit(a, r)

def rotate_image(i,a): # Rotate an image with pygame
    return pygame.transform.rotate(i, a)

def get_image_rect(i,x,y): # Get the pygame image rect
    return i.get_rect(center=(x,y))

def load_image(i,b): # Load an image with pygame
    if b == None:
        i = pygame.image.load(i)
    else:
        i = pygame.image.load(i).convert_alpha(b)

    return i

def scale_image(i,x,y): # Scale an image with pygame
    return pygame.transform.scale(i ,(x,y))

def clear_screen(i): # clear the screen 
    screen.blit(i, (0,0))

def render_lines(text,x,y,font_size): # Render multiple lines split with a \n

    text = text.splitlines()
    for i, l in enumerate(text):
        controls_text = get_font(font_size).render(l, True, "White")
        controls_rect = controls_text.get_rect(center=(x,(y+60*i)))
        screen.blit(controls_text, controls_rect)

def get_keys(): # get the keys pressed by the user with pygame
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                return 'Dx'

            if event.key == pygame.K_d:
                return 'Dd'


            if event.key == pygame.K_a:
                return 'Da'

            if event.key == pygame.K_e:
                return 'De'

            if event.key == pygame.K_q:
                return 'Dq'

            if event.key == pygame.K_SPACE:
                return 'Dspace' 

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                return 'Ud'
            if event.key == pygame.K_a:
                return 'Ua'

            if event.key == pygame.K_e:
                return 'Ue'

            if event.key == pygame.K_q:
                return 'Uq'

def play(a): # show the play screen

    screen.blit(BG, (0,0))
    show = False

    if a:
        show = True

    while show:
        render_lines("Controls: \nD - move right \nA - move left \nE - rotate clockwise\n Q - rotate counter-clockwise\nX - quit \nPRESS ENTER TO START",640,200,45)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    show = False

        pygame.display.update()
    
def highscore(scores): # Show the highscore screen
    while True:
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(BG, (0,0))
        render_lines("Highscore:" ,640,100,45) 
        render_lines(scores, 640, 120,30)

        OPTIONS_BACK = Button(image=None, pos=(640, 700), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(mouse_pos)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(mouse_pos):
                    main.main()

        pygame.display.update()

def main_menu(): # show the main menu screen
    while True:
        screen.blit(BG, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("Space Invaders", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=None, pos=(640, 300), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=None, pos=(640, 400), 
                            text_input="HIGHSCORES", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")
        QUIT_BUTTON = Button(image=None, pos=(640, 500), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")

        screen.blit(menu_text, menu_rect)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse_pos):
                    return 'play'
                if OPTIONS_BUTTON.checkForInput(mouse_pos):
                    return 'options'
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def game_state(x,r): # display either a win or game over screen

    timer = time.clock_gettime(time.CLOCK_MONOTONIC_RAW) 

    while True:
        screen.blit(BG, (0,0))
        mouse_pos = pygame.mouse.get_pos()
        render_lines(x,640,200,40) 
        render_lines("Press S to save score!",640,300,35)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(mouse_pos)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                   get_name() 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(mouse_pos):
                    main.main()

        if r:
            count = 5 - abs(int((timer - time.clock_gettime(time.CLOCK_MONOTONIC_RAW))))
            
            render_lines(str(count),640,300,30)

            if(count == 0):
                return 1
        pygame.display.update()

def get_name(): # Get the users name to save with the highscore

    name = ""
    checking = True

    while checking:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    name += "q"
                if event.key == pygame.K_w:
                    name += "w"
                if event.key == pygame.K_e:
                    name += "e"
                if event.key == pygame.K_r:
                    name += "r"
                if event.key == pygame.K_t:
                    name += "t"
                if event.key == pygame.K_y:
                    name += "y"
                if event.key == pygame.K_u:
                    name += "u"
                if event.key == pygame.K_i:
                    name += "i"
                if event.key == pygame.K_o:
                    name += "o"
                if event.key == pygame.K_p:
                    name += "p"
                if event.key == pygame.K_a:
                    name += "a"
                if event.key == pygame.K_s:
                    name += "s"
                if event.key == pygame.K_d:
                    name += "d"
                if event.key == pygame.K_f:
                    name += "f"
                if event.key == pygame.K_g:
                    name += "g"
                if event.key == pygame.K_h:
                    name += "h"
                if event.key == pygame.K_j:
                    name += "j"
                if event.key == pygame.K_k:
                    name += "k"
                if event.key == pygame.K_l:
                    name += "l"
                if event.key == pygame.K_z:
                    name += "z"
                if event.key == pygame.K_x:
                    name += "x"
                if event.key == pygame.K_c:
                    name += "c"
                if event.key == pygame.K_v:
                    name += "v"
                if event.key == pygame.K_b:
                    name += "b"
                if event.key == pygame.K_n:
                    name += "n"
                if event.key == pygame.K_m:
                    name += "m"
                if event.key == pygame.K_RETURN:
                    checking = False
    return name
