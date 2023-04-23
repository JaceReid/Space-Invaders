# Space Invaders

Group number: 10

## Group members:

  1. Rudolf Louw (SU number: 25960091)
  2. Armand Orffer (SU number: 25882473)
  3. James Devine (SU number: 25941232)

## Project ZIP file includes:

  1. main.py
  2. gui.py
  3. button.py
  4. physics.py
  5. objects.py
  6. class_Manager.py
  7. settings.json
  8. resources
     i) fonts
     ii) images
     iii) sounds
  9. data
      i) highscore.json
  10. README.md
  11. Peer review form

## Advanced functionality:
  
  1. Sounds
-	Implemented using the pygame library
-	All mp3 files downloaded for free from the web
-	Sound variables are first declared and initialised using pygame.mixer and then called to play later in the programme
  2. Music
-	Implemented using the pygame library
-	All mp3 files downloaded for free from the web
-	Sound variables are first declared and initialised using pygame.mixer and then called to play later in the programme
-	It is sometimes necessary to call the playing of a song to a stop/pause when calling other functions and changing the user display
  3. High score screen
-	Implemented by giving the user an option on the main menu to view the high scores screen
-	This choice implements a function which opens the json file to which the high scores are saved and populates a "data" array with the information in the file
-	This data array is then sorted from highest to lowest and a loop is used to call the information of the first 8 (if that many) items in the array
-	The called information is used to initialise score variables as strings
-	These strings are then rendered on the high scores screen, with a new background and background music (called as mentioned above in 2)
  4. Saving high score to json file
-	When the gameplay loop is interrupted by a player losing all their lives or gameplay reaching the end of the final wave, this option is given to the user
-	This option is given when the game_state function is called
-	When the user chooses the option to save their score, the get_name function is called which allows user input to type in their name
-	The save_score function is then called from main.py, which opens the jason file for the high scores and updates the information by using json.dump
-	the json file is updated by adding the player name and saved score to the file information
  5. Progressively harder levels
-	The number of columns of enemies increase with each wave and are calculated by using the wave number
  6. Extra lives
-	The player has 3 lives, which are displayed at the bottom left corner of the screen
-	A life gets removed each time a collision occurs between an enemy rocket and the player
-	Once the number of lives of the player reaches 0, gameplay ends and the "Game Over" screen is displayed
  7. Enemies counterattack
-	Every time the game tick (count) modulus 10 is equal to 0, there is a random probability that an enemy rocket is created using the rocket class
-	Once the class is used to create the enemy rocket, it is appended to the array of enemy rockets
-	The array of enemy rockets is looped through to check for collisions between an enemy rocket and the player
-	If a collision occurs, the enemy rocket is deleted and a life is removed from the player
  8. Bunkers
-	every time the game tick (counter) modulus 100 is equal to 0, there is a random probability that a bunker will be generated at one of the possible positions
-	If the probability succeeds, the bunker class is used to create a bunker object, which is appended to the bunker array
-	The array of bunkers is looped through to check for a bunker lready generated at the chosen position
-	If there is a bunker at that position, the bunker will no longer be generated
-	if the position is empty, a bunker is generated at that position
-	The bunker array is constantly looped through to check for collisions with enemy rockets or player rockets
-	If there is a collision in any of these cases, there is a random chance of doing damage to the bunker
-	For each level of damage, a new image is rendered for that specific array, until the bunker reaches full damage (zero health) and is deleted
  9. Improved graphics
-	New backgrounds, for gameplay and menu screens, have been sourced from the web
-	New graphics, for the enemy, player, player missile and player health, were sourced from the web
-	New graphics, for the bunker, different bunker health levels and enemy rocket, were designed in paint.net
  10. Additional player
-	A second player object was created by using the player class used for the first player
-	The second player can be called and initiated by pressing down "2" during gameplay
-	Only if the second player is active, is the second player and its rockets considered in all loops and checks
-	The second player's health is also rendered on the bottom left hand side of the screen
-	New keys, such as arrows for left and right and "Alt" and "Ctrl" for rotation, used for movement for the second player
-	The "Up" arrow is used to command the second player to shoot a player rocket
-	Gameplay ends when the second player has no lives left, even if the first player has lives left
     
## Used code:
The button class is used from this tutorial: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbWpVRkEyQmhaV2hnTlJFcGh1NnU4OUVnMXB2Z3xBQ3Jtc0tsdGtmajQzaTRUM1JwWG1vcG1fRUtPQUNBaHh4YzI1NFhMRUVabkRFMlhYR3hYUzNuYlN2OTFFR0pNZDhsczZyNkRKeHBJakh4ajlhblFhc29DQ1BPMWlHaDR1TGJvajhKdHdJbUg3S3d1anhjTEhoWQ&q=https%3A%2F%2Fgithub.com%2Fbaraltech%2FMenu-System-PyGame&v=GMBqjxcKogA

### Libraries used:
  1. pygame (Used only as a user interface)
  2. Datetime
  3. random
  4. json
  5. math
  6. sys
