import pygame # needed for game
import random # needed for random numbers
import time # needed for the timing function of the game
import os # needed for switching files
from pygame.color import Color # same function as memory game
from os import path

global score
def gethighscore():
    with open("highscore.txt", "r") as f:
        return f.read()
pygame.init()
clock = pygame.time.Clock()

def ScreenText(text, color, x,y, size, style, bold=False, itallic = False):
    font = pygame.font.SysFont(style,size, bold=bold, italic=itallic)
    window_text = font.render(text, True, color)
    window.blit(window_text, (x,y))



    
# Application setup and game information
pygame.init()
window_width = 800
window_height = 700
window = pygame.display.set_mode((window_width, window_height))
font = pygame.font.Font('OpenSans-Regular.ttf', 30)  
quit_text = "Quitting"


try:
    highscore = int(gethighscore())
except:
    highscore = 0


background = Color('Blue')

kick_time = time.time()
sixty_sec = 60 # 60 secs

# Store game data
begin_time = time.time()
running = True
terminated = True
points = 0
score = 0
time_paused = 0
response_time_initial = 0
response_time = 0

# creates the initial target
colour = Color('white') # colour of square
square_x = 95
square_y = 95
r_x = (window_width // 2) - square_x // 2        
r_y = (window_height // 2) - square_y // 2


white = [255,255,255]

paused = False
def pause():
    paused = True

    while paused:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN: #if a key gets pressed down
                if event.key == pygame.K_p: #if p gets pressed down
                    paused = False #pause gets disabled 
                elif event.key == pygame.K_q: #if q gets pressed down
                    pygame.quit() #quits the game
                    quit()
        display_text("Press P to continue",[250,100]) #displays "Press P to continue" when the paused function is called   
        display_text("Press Q to quit",[250,50])#displays "Press Q to quit" when the paused function is called



        pygame.display.update()
        clock.tick(60)#Basically the fps of the game (You can change it to your liking doesn't really matter since the game is paused 

def display_text(str, location):
    # Assign text contents and position
    words = font.render(str, True, Color('white'))
    ss_text = words
    rt_text = words.get_rect()
    rt_text.x = location[0]
    rt_text.y = location[1]

    # Draw to screen at specified position
    window.blit(ss_text, rt_text)
    
# Defining the function that shows all the counting elements
def display_screen():
    global response_time_initial, terminated, total_time, highscore
    
    # Create a blank canvas every frame. 
    window.fill(background)
    
    total_time = round((active_time - begin_time) - time_paused, 2)
    total_time = '{0:.2f}'.format(total_time) # 2 decimal places
    
    # Shows all three counters at the top of the screen
    display_text("Points: " +str(points), [250, 0])
    display_text("Time: " +str(total_time), [30, 0])
    display_text("Reaction Time: " +str(response_time) +" ms", [470, 0])
    ScreenText(f"highscore  {highscore}", white,50,50, size=20, style = "OpenSans-Regular.ttf") #DISPLAYS the current highscore FROM the text file

    pygame.draw.rect(window, colour, (r_x, r_y, square_x, square_y))
    
    # tracks the amount of time the target has been on screen before the user clicked it
    if terminated == True: # If target has been terminated...
        response_time_initial = time.time()  # ...restart the timer
        terminated = False # reset and loops back                    

when_missed = ("You Missed!")
textsurface = font.render(when_missed, False, Color('black'))


while running:

    if time.time() > kick_time + sixty_sec: # [c2 - https://raspberrypi.stackexchange.com/questions/15613/stop-program-after-a-period-of-time]
      print("Your time is up! Exiting to menu")
      print("Your score was" ,points)
      time.sleep(3)
      os.system('python menu.py') # stops the game after a pre determined amount of time, this is so the game does not continue on forever
    pygame.time.delay(5)
    active_time = time.time()       
    for event in pygame.event.get():  
        # if the key 'q' is pressed then the program quits
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            print("You have quit the program. Returning to menu...")
            time.sleep(2)
            os.system('python menu.py')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause()
   

        # Tracks the users cursor position and if they have clicked
        # c3 https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection
        cursor_position = pygame.mouse.get_pos()      # returns x and y positions  
        if pygame.mouse.get_pressed() == (1,0,0):
            if event.type == pygame.MOUSEBUTTONDOWN:
            
                # Check if the mouse cursor is hovering over the target
                # https://stackoverflow.com/questions/11846032/detect-mouseover-an-image-in-pygame
                if cursor_position[0] >= r_x - square_x//10 and cursor_position[0] <= r_x + square_x and cursor_position[1] >= r_y - square_y//10 and cursor_position[1] <= r_y + square_y:   
                
                    # If so, increment points and update reaction time
                    points += 1
                    score += 1
                    terminated = True
                    response_time = str(round((time.time() - response_time_initial)))
                    
                    # caps reaction time at 999 due to formatting issues that would otherwise be present
                    if float(response_time) <= 0.999:
                        response_time = response_time[2 : len(response_time) : 1]    # remove decimals from reaction time
                    else:
                        response_time = 999
                    
                    # Prints a reaction time generic speed in the command line


                    # Randomly assigns a new position for the square after it has been terminated
                    r_x = random.randrange(0, 600, 50)
                    r_y = random.randrange(50, 500, 50)

                # what happens when the player does not click on the square 
                else:
                    terminated = True
                    total_time = 0
                    points = 0
                    start_time = time.time()
                    response_time = 0
                    r_x = (window_width // 2) - square_x // 2       
                    r_y = (window_height // 2) - square_y // 2     # resets position of square
                    missed = True
                    while missed:
                      display_text("You Missed! You Lose Two Seconds!", [170, 75])
                      pygame.display.update()
                      time.sleep(2)
                      break

    if highscore <= points: #this if statements sees if the highscore has gone past the prev highscore
        highscore = points#and when the highscore passes the prev highscore it changes itself to the current highscore
    with open("highscore.txt", "w") as f: #this writes the current highscore onto the text file
        f.write(str(highscore))

    # refreshes the game screen
    display_screen()
    pygame.display.update()

pygame.quit()
