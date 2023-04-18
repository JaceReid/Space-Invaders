# Importing modules
import gui, class_Manager, physics
import time, random, math, json, datetime

# Declaring global varibles
wave = 0
score = 0


def main():

    # Get the users option from the main menu
    option = ""
    option = gui.main_menu()


    # Change window depending on the button pressed.
    if option == 'play':
        play()
        start_time = datetime.datetime.now()
    elif option == 'options':
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
    BG = gui.load_image("resources/images/game.jpg",None)
    BG = gui.scale_image(BG,area[0],area[1])
    game_bg = gui.load_image("resources/images/bg.jpg", None)
    image_player = gui.load_image('resources/images/player.bmp',BG)
    image_rocket = gui.load_image('resources/images/rocket.bmp',BG)
    enemys = []
    bunkers = []
    startx = 50
    starty = 50
    moving = [False,False]
    turning = [False,False]

    image_enemy = gui.scale_image(gui.load_image('resources/images/enemy.png',BG),32,32)
    image_enemy_rocket = gui.scale_image(gui.load_image('resources/images/enemy-rocket.bmp',BG),5,15)

    image_bunker = gui.load_image('resources/images/bunker.png',BG)
    image_bunker = gui.load_image('resources/images/bunker.png', BG)
    image_bunker1 = gui.load_image('resources/images/bunker1.png', BG)
    image_bunker2 = gui.load_image('resources/images/bunker2.png', BG)
    image_bunker3 = gui.load_image('resources/images/bunker3.png', BG)
    
    heart = gui.scale_image(gui.load_image('resources/images/heart.png',BG),28,28)
    

    r,c = 4,(10+2*wave)
    player_lives = 3
    shooting = False
    rockets = []
    enemy_rockets = []
    enemy_dead = False

    count, direction, tick, last_shot= 0,0,0,0
    hit = False
    last_hit = 0
    startx,starty = 100,50
    ex,ey = 0,0
    bunkers_pos = []
    bx,by = 0,(area[1]-100)


    player = class_Manager.make_player(image_player, area[0]//2,area[1]-20)

    # Set the postions for all the enemys
    for i in range(r):
        ey = starty+(50*i)
        for j in range(c):
            ex = startx+(j*50) 
            
            enemys.append(class_Manager.make_enemy(image_enemy,ex,ey,2+1*wave))


    gui.clear_screen(game_bg)

    # Game loop
    while True:

        gui.clear_screen(BG)

        # If all enemys are dead
        if (len(enemys) == 0):

            if wave == 5:
                gui.game_state('YOU WIN!!  score: ' + str(int(score)),0)
                name = gui.get_name()
                save_score(name, score)
            else:
                wave += 1
                play()

        # count is used as a game tick
        # genrate a bunker in one of the 4 postions with a random probabilty
        if count % 100 == 0:

            if (random.randint(0,2) > 1):
                
                bx = 50 +400*random.randint(0,5)
                add_bunker = True

                for i in range(len(bunkers_pos)):
                    
                    if bunkers_pos[i][0] == bx:
                        add_bunker = False
                if add_bunker:
                    bunkers.append(class_Manager.make_bunker(image_bunker,bx,by))
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

            gui.draw_object(bunkers[i].image, bunkers[i].r)

        # Check if player or enemy rockets hit the bunkers and then have a rondom chance of doing damage
            for j in range(len(rockets)):
                if physics.colision(rockets[j],bunkers[i],30):
                    del rockets[j]
                    bunkers[i].damage()

            for j in range(len(enemy_rockets)):

                if physics.colision(enemy_rockets[j],bunkers[i],40):
                    del enemy_rockets[j]
                    bunkers[i].damage()
                    break

                if physics.colision(enemy_rockets[j],player,20):
                    hit = True
                    break

        # Check the players number of lives if they are hit
        if hit and (tick-last_hit) > 3:
            if player_lives == 1:
                op = gui.game_state("GAME OVER\nSCORE: " + str(score*(wave+1)),1)
                name = op[1]
                save_score(name, score)
                wave = 0 
                if op[0] == 1:
                    play()
            player_lives -= 1
            hit = False
            last_hit = count//40



        # looping through all the enemys to check when to change direction
        for i in range(len(enemys)):
            try:
                if (count % 10) == 0:

                    if(i > (len(enemys)-len(enemys)/4)):
                        if random.randint(0,100) > 99:
                            enemy_rockets.append(class_Manager.make_rocket(image_enemy_rocket, enemys[i].x, enemys[i].y, math.pi))


                    if(enemys[i].x <= (area[0]-5) and direction == 0 or enemys[i].x > area[0]):

                        if(enemys[i].x >= (area[0]-10)):
                            direction = 1
                        

                            for h in range(r*c): 
                                if enemys[h].speed < 14:
                                    enemys[h].speed += 2
                                enemys[h].y += 25
                                enemys[h].x = area[0]-10 - 50*(h%(c-1))

                            

                        enemys[i].move(direction)

                    elif(enemys[i].x >= 0 or enemys[i].x <= 0):

                        if(enemys[i].x <= 10):
                            direction = 0
                            for h in range(r*c): 
                                if enemys[h].speed < 14:
                                    enemys[h].speed += 2
                                enemys[h].y += 25
                                enemys[h].x = 10 + 50*(h%(c-1))


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


                

            for h in range(len(rockets)):
                if physics.colision(rockets[h], enemys[i],30):
                    del rockets[h]
                    del enemys[i]
                    score += 10*(wave+1)
                    break


    

        # Move the rockets from the player
        if shooting:
            for i in range(len(rockets)):
                if(count % 5 == 0):
                    rockets[i].move(False) 
                    rockets[i].r = gui.get_image_rect(rockets[i].image,rockets[i].x,rockets[i].y)

                gui.draw_object(gui.rotate_image(rockets[i].image, rockets[i].a), rockets[i].r)


        # Move the enemy rockets
        for i in range(len(enemy_rockets)):
            if(count % 10 == 0):
                enemy_rockets[i].move(True)
                enemy_rockets[i].r = gui.get_image_rect(enemy_rockets[i].image,enemy_rockets[i].x,enemy_rockets[i].y)
            gui.draw_object(enemy_rockets[i].image, enemy_rockets[i].r)


        # draw the player lives
        for i in range(player_lives):
            gui.draw_object(heart, gui.get_image_rect(heart,30+i*20,area[1]-30))

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
            if(tick - last_shot > 2):
                rocket = class_Manager.make_rocket(image_rocket, player.x, player.y, (player.a)) 
                rockets.append(rocket)
                last_shot = count//40

            shooting = True
            
        if keys == 'Ud':
            moving[1] = False

        if keys == 'Ua':
            moving[0] = False

        if keys == 'Ue':
            turning[1] = False

        if keys == 'Uq':
            turning[0] = False


        if(moving[1] == True):
            if(player.x < area[0]):
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

        
        if tick < 10:
            gui.render_lines("wave " + str(wave + 1),area[0]//2,area[1]//2,40)



        # get count
        if(count%40 == 0):
            tick = count // 40
        count += 1

        gui.draw_object(gui.rotate_image(player.image, player.a), player.r)
        gui.update()

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
