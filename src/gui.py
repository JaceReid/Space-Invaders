import pygame, sys, objects, time, math, random
from button import Button
import physics


pygame.init() 


screen = pygame.display.set_mode()
area = screen.get_rect()
a,b,x,y = area

pygame.display.set_caption("Menu")

BG = pygame.image.load("resources/images/game.png")
game_bg = pygame.image.load("resources/images/bg.png")


def get_font(size): #sets the font
    return pygame.font.Font("resources/fonts/LCDN.TTF", size)


def render_lines(text,x,y):

    text = text.splitlines()
    for i, l in enumerate(text):
        controls_text = get_font(45).render(l, True, "White")
        controls_rect = controls_text.get_rect(center=(x,(y+60*i)))
        screen.blit(controls_text, controls_rect)

def colision(a,b):
    x = False
    if(abs(a.x - b.x) < 40 and abs(a.y - b.y) < 40):
        x = True

    return x

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

    image_player = pygame.image.load('resources/images/player.bmp').convert_alpha(BG)
    player = objects.player(image_player, x//2,y-20, 0, image_player.get_rect(center=(x//2,y-20)))
    screen.blit(player.image, player.r)

    image_rocket = pygame.image.load('resources/images/rocket.bmp').convert_alpha(BG)



    enemys = []
    bunkers = []
    startx = 50
    starty = 50
    moving = [False,False]
    turning = [False,False]
    image_enemy = pygame.transform.scale(pygame.image.load('resources/images/enemy.png').convert_alpha(BG),(32,32))
    image_enemy_rocket = pygame.transform.scale(pygame.image.load('resources/images/enemy-rocket.bmp').convert_alpha(BG),(5,15))
    image_bunker = pygame.image.load('resources/images/bunker.bmp').convert_alpha(BG)
    image_bunker1 = pygame.image.load('resources/images/bunker1.bmp').convert_alpha(BG)
    image_bunker2 = pygame.image.load('resources/images/bunker2.bmp').convert_alpha(BG)
    image_bunker3 = pygame.image.load('resources/images/bunker3.bmp').convert_alpha(BG)
    heart = pygame.transform.scale(pygame.image.load('resources/images/heart.png').convert_alpha(BG),(28,28))
    r,c = 4,10
    player_lives = 3
    shooting = False
    rockets = []
    enemy_rockets = []
    enemy_dead = False
    count, direction, tick, last_shot= 0,0,0,0
    hit = False
    last_hit = 0

    ex,ey = 0,0
    bunkers_pos = []

    bx,by = 0,(y-100)


    for i in range(r):
        ey = starty+(50*i)
        for j in range(c):
            ex = startx+(j*50) 
            enemys.append(objects.enemy(image_enemy,(ex),(ey),2,image_enemy.get_rect(center=(ex,ey))))



    score = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)

    screen.blit(game_bg, (0,0))
    while True:
        screen.blit(BG, (0,0))
        if (len(enemys) == 0):
            score = int((time.clock_gettime(time.CLOCK_MONOTONIC_RAW)-score)*100)
            game_state('YOU WIN!!  score: ' + str(score))

        if count % 100 == 0:
            if (random.randint(0,2) > 1):
                
                bx = 50 +400*random.randint(0,5)
                add = True

                for i in range(len(bunkers_pos)):
                    
                    if bunkers_pos[i][0] == bx:
                        add = False
                if add:
                    bunkers.append(objects.bunker(image_bunker,bx,by,image_bunker.get_rect(center=(bx,by)),4))
                    bunkers_pos.append([bx,by])

            
        for i in range(len(bunkers)):

            if(bunkers[i].s == 3):
                bunkers[i].image = image_bunker1
            elif(bunkers[i].s == 2):
                bunkers[i].image = image_bunker2
            elif(bunkers[i].s == 1):
                bunkers[i].image = image_bunker3
            elif(bunkers[i].s == 0):
                del bunkers[i]
                break

            screen.blit(bunkers[i].image, bunkers[i].r)

            for j in range(len(rockets)):
                if colision(rockets[j],bunkers[i]):
                    del rockets[j]
                    bunkers[i].damage()

            for j in range(len(enemy_rockets)):

                if colision(enemy_rockets[j],bunkers[i]):
                    del enemy_rockets[j]
                    bunkers[i].damage()
                    break

                if colision(enemy_rockets[j],player):
                    hit = True
                    break

        if hit and tick-last_hit > 3:
            if player_lives == 1:
                game_state("GAME OVER")
            player_lives -= 1
            hit = False
            last_hit = count//40



        for i in range(len(enemys)):
            try:
                if (count % 10) == 0:

                    if(i > (len(enemys)-len(enemys)/4)):
                        if random.randint(0,100) > 99:
                            enemy_rockets.append(objects.rocket(image_enemy_rocket, enemys[i].x, enemys[i].y, math.pi, image_enemy_rocket.get_rect(center=(enemys[i].x,enemys[i].y))))


                    if(enemys[i].x <= (x-5) and direction == 0 or enemys[i].x > x):

                        if(enemys[i].x >= (x-10)):
                            direction = 1
                        

                            for h in range(40): 
                                enemys[h].speed += 2
                                enemys[h].y += 25
                                enemys[h].x = x-10 - 50*(h%9)

                            

                        enemys[i].move(direction)

                    elif(enemys[i].x >= 0 or enemys[i].x <= 0):

                        if(enemys[i].x <= 10):
                            direction = 0
                            for h in range(40): 
                                enemys[h].speed += 2
                                enemys[h].y += 25
                                enemys[h].x = 10 + 50*(h%9)


                        enemys[i].move(direction) 
                screen.blit(enemys[i].image, enemys[i].r)

                if(enemys[i].y >= y):
                    game_state('GAME OVER')
            except:
                break


                

            for h in range(len(rockets)-1):
                if(abs(rockets[h].x - enemys[i].x) < 20 and abs(rockets[h].y - enemys[i].y) < 20):
                    del rockets[h]
                    del enemys[i]
                    break


    

        if shooting:
            for i in range(len(rockets)):
                if(count % 5 == 0):
                    rockets[i].move(False) 
                    rockets[i].r = rockets[i].image.get_rect(center=(rockets[i].x,rockets[i].y))
                screen.blit(pygame.transform.rotate(rockets[i].image, rockets[i].a), rockets[i].r)


        for i in range(len(enemy_rockets)):
            if(count % 10 == 0):
                enemy_rockets[i].move(True)
                enemy_rockets[i].r = enemy_rockets[i].image.get_rect(center=(enemy_rockets[i].x,enemy_rockets[i].y))
            screen.blit(enemy_rockets[i].image, enemy_rockets[i].r)


        for i in range(player_lives):
            screen.blit(heart, heart.get_rect(center=(30+i*20,y-30)))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    main_menu()

                if event.key == pygame.K_d:
                    moving[1] = True


                if event.key == pygame.K_a:
                    moving[0] = True

                if event.key == pygame.K_e:
                    turning[1] = True

                if event.key == pygame.K_q:
                    turning[0] = True

                if event.key == pygame.K_SPACE:
                    if(tick - last_shot > 2):
                        rocket = objects.rocket(image_rocket, player.x, player.y, (player.a), image_rocket.get_rect(center=(player.x,player.y))) 
                        rockets.append(rocket)
                        last_shot = count//40

                    shooting = True
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    moving[1] = False
                if event.key == pygame.K_a:
                    moving[0] = False

                if event.key == pygame.K_e:
                    turning[1] = False
                if event.key == pygame.K_q:
                    turning[0] = False


        if(moving[1] == True):
            if(player.x < x):
                player.move(0)

        if(moving[0] == True):
            if(player.x > 0):
                player.move(1)

        if(turning[1] == True):
            if player.a > -45:
                player.a -= 0.5


        if(turning[0] == True):
            if player.a < 45:
                player.a += 0.5



        if(count%40 == 0):
            tick = count // 40
        count += 1

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

    timer = time.clock_gettime(time.CLOCK_MONOTONIC_RAW) 

    while True:
        screen.blit(BG, (0,0))
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

        if(x == "GAME OVER"):
            count = 5 - abs(int((timer - time.clock_gettime(time.CLOCK_MONOTONIC_RAW))))

            render_lines(str(count),640,300)

            if(count == 0):
                play()

        pygame.display.update()


main_menu()
