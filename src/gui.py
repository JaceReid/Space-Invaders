import pygame, sys
from button import Button

pygame.init()

screen = pygame.display.set_mode()
area = screen.get_rect()
a,b,x,y = area

pygame.display.set_caption("Menu")

BG = pygame.image.load("resources/images/game.png")

def get_font(size): #sets the font
    return pygame.font.Font("resources/fonts/LCDN.TTF", size)


def render_lines(text,x,y):

    text = text.splitlines()
    for i, l in enumerate(text):
        controls_text = get_font(45).render(l, True, "White")
        controls_rect = controls_text.get_rect(center=(x,(y+60*i)))
        screen.blit(controls_text, controls_rect)

def play():

    screen.blit(BG, (0,0))
    show = True

    while show:
        render_lines("Controls: \nD - move right \nA - move left \nE - rotate clockwise\n Q - rotate counter-clockwise\nX - quit \nPRESS ENTER TO START",640,200)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    show = False

        pygame.display.update()



    while True:
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(BG, (0,0))

        #draw objects
        pygame.draw.circle(screen, "Red", (x//2,y-20), 30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(BG, (0,0))
        render_lines("Options:",640,200) 

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(mouse_pos)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(mouse_pos):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        screen.blit(BG, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Space Invaders", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=None, pos=(640, 300), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=None, pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")
        QUIT_BUTTON = Button(image=None, pos=(640, 500), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse_pos):
                    play()
                if OPTIONS_BUTTON.checkForInput(mouse_pos):
                    options()
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
