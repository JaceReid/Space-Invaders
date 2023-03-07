import pygame, sys, objects, time, math
from button import Button


pygame.init()

clock = pygame.time.Clock

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

    image_player = pygame.image.load('resources/images/player.bmp').convert()
    player = objects.player(image_player, x//2,y-20, 0, image_player.get_rect(center=(x//2,y-20)))
    screen.blit(player.image, player.r)

    image_rocket = pygame.image.load('resources/images/rocket.bmp').convert()


    enemys = []
    startx = 490
    starty = 50
    image_enemy = pygame.image.load('resources/images/enemy.bmp').convert()
    ex,ey = 0,0


    for i in range(4):
        ey = starty+(50*i)
        for j in range(10):
            ex = startx+(j*40) 
            enemys.append(objects.enemy(image_enemy,(ex),(ey),2,image_enemy.get_rect(center=(ex,ey))))


    shooting = False
    rockets = []
    enemy_dead = False
    count, direction, tick, last_shot= 0,0,0,0
    


    score = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
    while True:
        screen.blit(BG, (0,0))
        if (len(enemys) == 0):
            game_state('YOU WIN!!  score: ' + str(int((time.clock_gettime(time.CLOCK_MONOTONIC_RAW)-score)*100)))


        for i in range(len(enemys)):
            try:
                if (count % 10) == 0:
                    if(enemys[i].x <= (x-5) and direction == 0 or enemys[i].x > x):

                        if(enemys[i].x >= (x-10)):
                            direction = 1
                        

                            for h in range(40): 
                                enemys[h].speed += 2
                                enemys[h].y += 25
                                enemys[h].x = x-10 - 40*(h%9)

                            

                        enemys[i].move(direction)

                    elif(enemys[i].x >= 0 or enemys[i].x <= 0):

                        if(enemys[i].x <= 10):
                            direction = 0
                            for h in range(40): 
                                enemys[h].speed += 2
                                enemys[h].y += 25
                                enemys[h].x = 10 + 40*(h%9)


                        enemys[i].move(direction) 
                screen.blit(enemys[i].image, enemys[i].r)

                if(enemys[i].y >= y):
                    game_over('GAME OVER')
            except:
                break


            for h in range(len(rockets)-1):
                if(abs(rockets[h].x - enemys[i].x) < 20 and abs(rockets[h].y - enemys[i].y) < 20):
                    del rockets[h]
                    del enemys[i]
                    break
                    enemy_dead = True


            if enemy_dead:
                break
        count += 1
    

        if shooting:
            for i in range(len(rockets)):
                if(count % 5 == 0):
                    rockets[i].move() 
                    rockets[i].r = rockets[i].image.get_rect(center=(rockets[i].x,rockets[i].y))
                screen.blit(pygame.transform.rotate(rockets[i].image, rockets[i].a), rockets[i].r)




        pygame.key.set_repeat(1,20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    main_menu()

                if event.key == pygame.K_d:
                    if(player.x < x):
                        player.move(0)

                if event.key == pygame.K_a:
                    if(player.x > 0):
                        player.move(1)

                if event.key == pygame.K_e:
                    if player.a > -45:
                        player.a -= 1.5

                if event.key == pygame.K_q:
                    if player.a < 45:
                        player.a += 1.5

                if event.key == pygame.K_SPACE:
                    if(tick - last_shot > 1):
                        rocket = objects.rocket(image_rocket, player.x, player.y, (player.a), image_rocket.get_rect(center=(player.x,player.y))) 
                        rockets.append(rocket)
                        last_shot = count//40


                    shooting = True
                    


        
        if(count%40 == 0):
            tick = count // 40
        screen.blit(pygame.transform.rotate(player.image, player.a), player.r)
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

        menu_text = get_font(100).render("Space Invaders", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=None, pos=(640, 300), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=None, pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")
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
                    play()
                if OPTIONS_BUTTON.checkForInput(mouse_pos):
                    options()
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def game_state(x):
    while True:

        mouse_pos = pygame.mouse.get_pos()
        render_lines(x,640,200) 

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


main_menu()
