# Space Invaders

============
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
     - Implemented using the pygame library
     - All mp3 files downloaded for free from the web
     - Sound variables are first declared and initialised using pygame.mixer and then called to play later in the programme
  2. Music
     - Implemented using the pygame library
     - All mp3 files downloaded for free from the web
     - Sound variables are first declared and initialised using pygame.mixer and then called to play later in the programme
     - It is sometimes necessary to call the playing of a song to a stop/pause when calling other functions and changing the user display
  3. High score screen
     - Implemented by giving the user an option on the main menu to view the high scores screen
     - This choice implements a function which opens the json file to which the high scores are saved and populates a "data" array with the information in the file
     - This data array is then sorted from highest to lowest and a loop is used to call the information of the first 8 (if that many) items in the array
     - The called information is used to initialise score variables as strings
     - These strings are then rendered on the high scores screen, with a new background and background music (called as mentioned above in 2)
  4. Saving high score to json file
     - 
  7. Progressively harder levels
  8. Extra lives
  9. Enemies counterattack
  10. Bunkers
  11. Improved graphics

## Used code:
The button class is used from this tutorial: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbWpVRkEyQmhaV2hnTlJFcGh1NnU4OUVnMXB2Z3xBQ3Jtc0tsdGtmajQzaTRUM1JwWG1vcG1fRUtPQUNBaHh4YzI1NFhMRUVabkRFMlhYR3hYUzNuYlN2OTFFR0pNZDhsczZyNkRKeHBJakh4ajlhblFhc29DQ1BPMWlHaDR1TGJvajhKdHdJbUg3S3d1anhjTEhoWQ&q=https%3A%2F%2Fgithub.com%2Fbaraltech%2FMenu-System-PyGame&v=GMBqjxcKogA
### Libraries used:
  1. pygame (Used only as a user interface)
  2. Datetime
  3. random
  4. json
  5. math
  6. sys
