# Importing modules
import gui, class_Manager, physics
import time, random, math, json, datetime
import pygame

# Declaring global varibles
wave = 0
score = 0


def main():
    
    main_menu_song = pygame.mixer.Sound('resources/sounds/future-invention-upbeat-high-electronic-technological-music-57037.mp3')
    
    pygame.mixer.Sound.play(main_menu_song)

    # Get the users option from the main menu
    option = ""
    option = gui.main_menu()


    # Change window depending on the button pressed.
    if option == 'play':
        pygame.mixer.Sound.stop(main_menu_song)
        play()
        start_time = datetime.datetime.now()
        
    elif option == 'options':
        pygame.mixer.Sound.stop(main_menu_song)
        show_scores()

    

def play():

    # set global varible
    global wave
    global score
    global start_time

    # Check if it is the first wave
    if wave == 0:
        gui.play(1)
    else:
        gui.play(0)

    
    area = gui.get_area()

    # Declare and intilze varibles
    Background = gui.load_image("resources/images/game.jpg",None)
    Background = gui.scale_image(Background,area[0],area[1])
    game_bg = gui.load_image("resources/images/bg.jpg", None)
    image_player = gui.load_image('resources/images/player.bmp',Background)
    image_rocket = gui.load_image('resources/images/rocket.bmp',Background)
    enemys = []
    bunkers = []
    startx = 50
    starty = 50
    moving = [False,False,False,False]
    turning = [False,False]
    second = True

    image_enemy = gui.scale_image(gui.load_image('resources/images/enemy.png',Background),32,32)
    image_enemy_rocket = gui.scale_image(gui.load_image('resources/images/enemy-rocket.bmp',Background),5,15)

    image_bunker = gui.load_image('resources/images/bunker.png',Background)
    image_bunker = gui.load_image('resources/images/bunker.png', Background)
    image_bunker1 = gui.load_image('resources/images/bunker1.png', Background)
    image_bunker2 = gui.load_image('resources/images/bunker2.png', Background)
    image_bunker3 = gui.load_image('resources/images/bunker3.png', Background)
    
    heart = gui.scale_image(gui.load_image('resources/images/heart.png',Background),28,28)
    
    shoot_sound = pygame.mixer.Sound('resources/sounds/blaster-2-81267.mp3')
    

    enemy_rows,enemy_columns = 4,(10+2*wave)
    player_1_lives = 3
    player_2_lives = 3
    shooting_1 = False
    shooting_2 = False
    rockets_1 = []
    rockets_2 = []
    enemy_rockets = []
    enemy_dead = False

    count, direction, last_hit= 0,0,0
    tick_1, tick_2 = 0,0
    hit_1, hit_2 = False, False
    last_shot_1, last_shot_2 = 0,0 
    startx,starty = 100,50
    enemy_x,enemy_y = 0,0
    bunkers_pos = []
    bunker_x,bunker_y = 0,(area[1]-100)

    # Creates the first player
    player_1 = class_Manager.make_player(image_player, area[0]//2,area[1]-20)
    
    # Creates the second player
    player_2 = class_Manager.make_player(image_player, area[0]//2-20,area[1]-80)
    
    # Set the postions for all the enemys
    for i in range(enemy_rows):
        enemy_y = starty+(50*i)
        for j in range(enemy_columns):
            enemy_x = startx+(j*50) 
            
            enemys.append(class_Manager.make_enemy(image_enemy,enemy_x,enemy_y,2+1*wave))


    gui.clear_screen(game_bg)

    # Game loop
    while True:

        gui.clear_screen(Background)

        # If all enemys are dead
        if (len(enemys) == 0):

            if wave == 5:
                op2 = gui.game_state('YOU WIN!!  score: ' + str(int(score)),0)

                if op2[2]:
                    name = op2[1]
                    save_score(name, score)
            else:
                wave += 1
                play()

        # count is used as a game tick
        # genrate a bunker in one of the 4 postions with a random probabilty
        if count % 100 == 0:

            if (random.randint(0,2) > 1):
                
                bunker_x = (area[0]/6) + (area[0]/6)*random.randint(0,4)
                add_bunker = True

                for i in range(len(bunkers_pos)):
                    
                    if bunkers_pos[i][0] == bunker_x:
                        add_bunker = False
                if add_bunker:
                    bunkers.append(class_Manager.make_bunker(image_bunker,bunker_x,bunker_y))
                    bunkers_pos.append([bunker_x,bunker_y])

            
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

            gui.draw_object(bunkers[i].image, bunkers[i].r)

        # Check if player or enemy rockets hit the bunkers and then have a rondom chance of doing damage
            for j in range(len(rockets_1)):
                if physics.colision(rockets_1[j],bunkers[i],30):
                    del rockets_1[j]
                    bunkers[i].damage()
            for j in range(len(rockets_2)):
                if physics.colision(rockets_2[j],bunkers[i],30):
                    del rockets_2[j]
                    bunkers[i].damage()

            for j in range(len(enemy_rockets)):

                if physics.colision(enemy_rockets[j],bunkers[i],40):
                    del enemy_rockets[j]
                    bunkers[i].damage()
                    break

                if physics.colision(enemy_rockets[j],player_1,20):
                    hit_1 = True
                    break
                if physics.colision(enemy_rockets[j],player_2,20):
                    hit_2 = True
                    break

        # Check the first players number of lives if they are hit
        if hit_1 and (tick_1-last_hit) > 3:
            if player_1_lives == 1 or player_2_lives == 1:
                op1 = gui.game_state("GAME OVER\nSCORE: " + str(score),1)
                name = op1[1]
                save_score(name, score)
                wave = 0 
                if op1[0] == 1:
                    play()
            player_1_lives -= 1            
            hit_1 = False
            last_hit = count//40
        if second:
            # Check the second players number of lives if they are hit
            if  hit_2 and (tick_2 - last_hit) > 3:
                if player_2_lives == 1:
                    op1 = gui.game_state("GAME OVER\nSCORE: " + str(score),1)
                    name = op1[1]
                    save_score(name, score)
                    wave = 0 
                    if op1[0] == 1:
                        play()
                
                player_2_lives -= 1
                hit_2 = False
                last_hit = count//40
            



        # looping through all the enemys to check when to change direction
        for i in range(len(enemys)):
            try:
                if (count % 10) == 0:

                    if(i > (len(enemys)-len(enemys)/4)):
                        if random.randint(0,100) > 99:
                            enemy_rockets.append(class_Manager.make_rocket(image_enemy_rocket, enemys[i].x, enemys[i].y, math.pi))


                    if(direction == 0):

                        if(enemys[i].x >= (area[0]-10)):
                            direction = 1
                        

                            for h in range(enemy_rows*enemy_columns):
                                if enemys[h].speed < 14:
                                    enemys[h].speed += 2
                                enemys[h].y += 25
                                enemys[h].x = area[0]-10 - 50*(h%(enemy_columns-1))

                            

                        enemys[i].move(direction)

                    else:

                        if(enemys[i].x <= 10):
                            direction = 0
                            for h in range(enemy_rows*enemy_columns):
                                if enemys[h].speed < 14:
                                    enemys[h].speed += 2
                                enemys[h].y += 25
                                enemys[h].x = 10 + 50*(h%(enemy_columns-1))


                        enemys[i].move(direction) 

                gui.get_image_rect(enemys[i].image,enemys[i].x,enemys[i].y)

                gui.draw_object(enemys[i].image, enemys[i].r)
                

                if(enemys[i].y >= area[1]):
                    op = gui.game_state('GAME OVER\nSCORE: ' + str(score),1)
                    name = op[1]
                    save_score(name, score)
                    wave = 0
                    if op[0] == 1:
                        play()
            except:
                break


                
            # checks for collision between the first players rocket and an enemy
            for h in range(len(rockets_1)):
                if physics.colision(rockets_1[h], enemys[i],30):
                    del rockets_1[h]
                    del enemys[i]
                    score += 10*(wave+1)
                    break                      
                        
            if second:
                # checks for collision between the second players rocket and an enemy
                for h in range(len(rockets_2)):
                    if physics.colision(rockets_2[h], enemys[i],30):
                        del rockets_2[h]
                        del enemys[i]
                        score += 10*(wave+1)
                        break

    

        # Move the rockets from the first player
        if shooting_1:
            for i in range(len(rockets_1)):
                if(count % 5 == 0):
                    rockets_1[i].move(False) 
                    rockets_1[i].r = gui.get_image_rect(rockets_1[i].image,rockets_1[i].x,rockets_1[i].y)

                gui.draw_object(gui.rotate_image(rockets_1[i].image, rockets_1[i].a), rockets_1[i].r)
        
        
        if second:
            # Move the rockets from the second player
            if shooting_2:
                for j in range(len(rockets_2)):
                    if(count % 5 == 0):
                        rockets_2[j].move(False) 
                        rockets_2[j].r = gui.get_image_rect(rockets_2[j].image,rockets_2[j].x,rockets_2[j].y)

                    gui.draw_object(gui.rotate_image(rockets_2[j].image, rockets_2[j].a), rockets_2[j].r)
                
        


        # Move the enemy rockets
        for i in range(len(enemy_rockets)):
            if(count % 10 == 0):
                enemy_rockets[i].move(True)
                enemy_rockets[i].r = gui.get_image_rect(enemy_rockets[i].image,enemy_rockets[i].x,enemy_rockets[i].y)
            gui.draw_object(enemy_rockets[i].image, enemy_rockets[i].r)


        # draw the first players lives
        for i in range(player_1_lives):
            gui.draw_object(heart, gui.get_image_rect(heart,30+i*20,area[1]-30))
        
        if second:
        # draw the second players lives
            for j in range(player_2_lives):
                gui.draw_object(heart, gui.get_image_rect(heart,30+j*20,area[1]-70))

        # display score
        gui.render_lines("score: " + str(score),area[0]//2,25,30)



        # check user key presses and do actions acroudingly
        keys = gui.get_keys()

        if keys == 'Dx':
            main()

        if keys == 'Dd':
            moving[1] = True

        if keys == 'Da':
            moving[0] = True

        if keys == 'De':
            turning[1] = True

        if keys == 'Dq':
            turning[0] = True

        if keys == 'Dspace':
            if(tick_1 - last_shot_1 > 2):
                
                pygame.mixer.Sound.play(shoot_sound)
                
                rocket_1 = class_Manager.make_rocket(image_rocket, player_1.x, player_1.y, (player_1.a)) 
                rockets_1.append(rocket_1)
                last_shot_1 = count//40

            shooting_1 = True
            
        if keys == 'Ud':
            moving[1] = False

        if keys == 'Ua':
            moving[0] = False

        if keys == 'Ue':
            turning[1] = False

        if keys == 'Uq':
            turning[0] = False


        if(moving[1] == True):
            if(player_1.x < area[0]):
                player_1.move(0)

        if(moving[0] == True):
            if(player_1.x > 0):
                player_1.move(1)

        if(turning[1] == True):
            if player_1.a > -45:
                player_1.a -= 0.5


        if(turning[0] == True):
            if player_1.a < 45:
                player_1.a += 0.5
                
        #checks the keys for the second player movement
        if second:
            if keys == 'Dright':
                moving[3] = True

            if keys == 'Dleft':
                moving[2] = True


            if keys == 'Dup':
                if(tick_2 - last_shot_2 > 2):
                    
                    #pygame.mixer.Sound.play(shoot_sound)
                    
                    rocket_2 = class_Manager.make_rocket(image_rocket, player_2.x, player_2.y, (player_2.a)) 
                    rockets_2.append(rocket_2)
                    last_shot_2 = count//40

                shooting_2 = True
                
            if keys == 'Uright':
                moving[3] = False

            if keys == 'Uleft':
                moving[2] = False
           
            if(moving[3] == True):
                if(player_2.x < area[0]):
                    player_2.move(0)

            if(moving[2] == True):
                if(player_2.x > 0):
                    player_2.move(1)
        
                
                
        
        
        if tick_1 < 10 or tick_2 < 10:
            gui.render_lines("wave " + str(wave + 1),area[0]//2,area[1]//2,40)



        # get count
        if(count%40 == 0):
            tick_1 = count // 40
            if second:
                tick_2 = count // 40
        count += 1

        # draws the player
        gui.draw_object(gui.rotate_image(player_1.image, player_1.a), player_1.r)
        if second:
            gui.draw_object(gui.rotate_image(player_2.image, player_2.a), player_2.r)
        gui.update()
        
        if keys == 'Active':
            second == True
        


# Displays the highscores in the right formate
def show_scores():

    data = get_scores()

    scores = "\n"
    count = 0

    for w in sorted(data, key=data.get, reverse=True):
        if count < 8:
            name = w[0:w.find("~")]
            date = w[w.find("~")+1:w.find(" ")]
            score = data[w]

            scores += date + "  " + name + ": " + str(score) + "\n"
        count += 1

    gui.highscore(scores)

# save a new high score to the json file
def save_score(name, score):


    date = str(datetime.datetime.now())
    name = name + "~" + date

    data = get_scores()
    
    values = []

    


   # data[name] = score

    data.update({name: score})


    with open('data/highscore.json', 'w') as f:
        json.dump(data, f)

# Gets the saved highscores from a json file
def get_scores():

    with open('data/highscore.json') as f:
        data = json.load(f)

    return data


if __name__ == '__main__': main()
