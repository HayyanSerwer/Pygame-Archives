import pygame
import time
import sys
from pygame import mixer #used to add audio
import random
from pygame.locals import *

pygame.init()
screen_width = 800
screen_height = 600

clock = pygame.time.Clock()
fps = 60

score = 0

font = pygame.font.SysFont("freesansbold.ttf", 32)
winning_font = pygame.font.SysFont("freesansbold.ttf", 100)

grey = [50,50,50]
bg_color = [0,0,0] 
white = [255,255,255]
blue = [0,0, 205]
black = [0,0,0]
player1_color = [255,255,255]
player2_color = [255,255,255]
circle_color = [255,255,255]
text_color = [255,255,255]

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Fiver')



background = pygame.image.load("background_01.jpg").convert()
play_img = pygame.image.load('play.png')
players_img = pygame.image.load('players.png')
quit_img = pygame.image.load('quit.png')
leaderboard_img = pygame.image.load('leaderboard.png')
easy_img = pygame.image.load('text/easy.png')
normal_img = pygame.image.load('text/normal.png')
hard_img = pygame.image.load('text/hard.png')
difficulty_img = pygame.image.load('text/difficulty.png')
           
button_g_off = pygame.image.load('sprites/green_off.png')
button_y_off = pygame.image.load('sprites/yellow_off.png')
button_b_off = pygame.image.load('sprites/blue_off.png')
button_r_off = pygame.image.load('sprites/red_off.png')
buttons_off = {0:button_g_off, 1:button_y_off, 2:button_b_off, 3:button_r_off}

button_g_on = pygame.image.load('sprites/green_on.png')
button_y_on = pygame.image.load('sprites/yellow_on.png')
button_b_on = pygame.image.load('sprites/blue_on.png')
button_r_on = pygame.image.load('sprites/red_on.png')
buttons_on = {0:button_g_on, 1:button_y_on, 2:button_b_on, 3:button_r_on}

rectG = button_g_off.get_rect(center=(352, 192))
rectY = button_y_off.get_rect(center=(352, 320))
rectB = button_b_off.get_rect(center=(480, 320))
rectR = button_r_off.get_rect(center=(480, 192))
rects = {0:rectG, 1:rectY, 2:rectB, 3:rectR}

buttons = {0:button_g_off, 1:button_y_off, 2:button_b_off, 3:button_r_off}

beep = pygame.mixer.Sound('sprites/beep.wav')
laugh = pygame.mixer.Sound('sprites/laugh.wav')
level = 1
max_levels = 4

sequence = []   
click = 0        
wrong = False   
state = 'OFF'

font = pygame.font.SysFont('FiraCode', 32)
score = 0
color = (255, 255, 255)
position = (10, 10)
text = str('Score:'.format(score))

player_score = 0
color = (255, 255, 255)
position2 = (300, 10)
text2 = str('Highscore:'.format(player_score))

score2 = 0
remainder = 0

players = 0

mixer.music.load('sprites/hope.ogg')
mixer.music.play(-1)



def get_high_score():
    with open("high score.txt", "r") as f:
        return f.read()


plus = pygame.Rect(330, 255, 30,30)
minus = pygame.Rect(430, 255, 30,30)

def simon_blinks(key):
    buttons[key] = buttons_on[key]

    # blit
    for i in buttons:
        screen.blit(buttons[i], rects[i])
        screen.blit(font.render(text, True, color), position) 
        pygame.display.update()

    # blink for 250ms
    time.sleep(0.95)

    # turn blinking button off
    screen.fill((30, 30, 30)) 
    buttons[key] = buttons_off[key]

    # blit
    for i in buttons:
        screen.blit(buttons[i], rects[i])
        screen.blit(font.render(text, True, color), position) 
        pygame.display.update()

    # pause between blinks for 750ms
    time.sleep(0.75)

def simon_blinks_normal(key):
    buttons[key] = buttons_on[key]

    # blit
    for i in buttons:
        screen.blit(buttons[i], rects[i])
        screen.blit(font.render(text, True, color), position) 
        pygame.display.update()

    # blink for 250ms
    time.sleep(0.45)

    # turn blinking button off
    screen.fill((30, 30, 30)) 
    buttons[key] = buttons_off[key]

    # blit
    for i in buttons:
        screen.blit(buttons[i], rects[i])
        screen.blit(font.render(text, True, color), position) 
        pygame.display.update()

    # pause between blinks for 750ms
    time.sleep(0.75)

def simon_blinks_hard(key):
    buttons[key] = buttons_on[key]

    # blit
    for i in buttons:
        screen.blit(buttons[i], rects[i])
        screen.blit(font.render(text, True, color), position) 
        pygame.display.update()

    # blink for 250ms
    time.sleep(0.15)

    # turn blinking button off
    screen.fill((30, 30, 30)) 
    buttons[key] = buttons_off[key]

    # blit
    for i in buttons:
        screen.blit(buttons[i], rects[i])
        screen.blit(font.render(text, True, color), position) 
        pygame.display.update()

    # pause between blinks for 750ms
    time.sleep(0.75)
#A command that is used to display text onto the screen      
def display_text(str, location):
    # Assign text contents and position
    words = font.render(str, True, Color('white'))
    ss_text = words
    rt_text = words.get_rect()
    rt_text.x = location[0]
    rt_text.y = location[1]

    # Draw to screen at specified position
    screen.blit(ss_text, rt_text)

def get_click(click_pos):

    global click
    global wrong
    
    for i in rects:
        if rects[i].collidepoint(click_pos):

            """ turn on clicked button """
            buttons[i] = buttons_on[i]
            # blit
            for j in buttons:
                screen.blit(buttons[j], rects[j])
                screen.blit(font.render(text, True, color), position) 
                pygame.display.update()

            # blink for 250ms
            time.sleep(0.25)

            # turn blinking button off
            screen.fill((30, 30, 30)) 
            buttons[i] = buttons_off[i]

            # blit
            for j in buttons:
                screen.blit(buttons[j], rects[j])
                screen.blit(font.render(text, True, color), position) 
                pygame.display.update()

            # pause between blinks for 750ms
            time.sleep(0.75)
            
            """ check whether the right button in the sequence was pressed """
            if i == sequence[click]:
                click += 1
            else:
                wrong = True

player_2 = False
def player_2():
    global background, menu, state, score, click, score2, remainder
    player_2 = True
    while menu:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
            if state == 'OFF':
                for number in sequence:
                    pygame.event.pump()
                    beep.play()
                    simon_blinks(number)
                state = 'ON'
                click = 0
            # Click buttons
            if state == 'ON':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    beep.play()
                    get_click(pygame.mouse.get_pos())

                if click == len(sequence):
                    sequence.append(random.choice((0, 1, 2, 3)) )
                    score += 1
                    score2 += 1
                    remainder = score2 % 2
                    print(remainder)
                    text = str('Score: {}'.format(score2))
                    state = 'OFF'
                if wrong and remainder == 1:
                    display_text("PLAYER2 LOST!!",[350,100])
                    if quit_button.draw():
                        pygame.quit()
                        quit()
                        break

                if wrong and remainder == 0:
                    display_text("PLAYER1 LOST!!",[350,100])
                    if quit_button.draw():
                        pygame.quit()
                        quit()
                        break

        if remainder == 0:
            display_text("Player 1",[350,20])
        else:
            display_text("Player 2's turn",[350,20])
        display_text("Highscore:",[580,10])
        highscore_text = font.render(f"{highscore}", False, text_color)
        screen.blit(highscore_text,(700,10))
        player_text = font.render(f"{score}", False, text_color)
        width = 50
        file = open("score.txt", "a")
        file.write(str(score2)+","+user_text+"\n")
        file.close()
        file = open("score.txt", "r")
        readthefile = file.readlines()
        sortedData = sorted(readthefile,reverse = True)
        screen.blit(player_text,(80,10))
        pygame.display.update()
        clock.tick(60)

def player_2_normal():
    global background, menu, state, score, click, score2, remainder
    player_2 = True
    while menu:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
            if state == 'OFF':
                for number in sequence:
                    pygame.event.pump()
                    beep.play()
                    simon_blinks_normal(number)
                state = 'ON'
                click = 0
            # Click buttons
            if state == 'ON':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    beep.play()
                    get_click(pygame.mouse.get_pos())

                if click == len(sequence):
                    sequence.append(random.choice((0, 1, 2, 3)) )
                    score += 1
                    score2 += 1
                    remainder = score2 % 2
                    print(remainder)
                    text = str('Score: {}'.format(score2))
                    state = 'OFF'
                if wrong and remainder == 1:
                    display_text("PLAYER2 LOST!!",[350,100])
                    if quit_button.draw():
                        pygame.quit()
                        quit()
                        break

                if wrong and remainder == 0:
                    display_text("PLAYER1 LOST!!",[350,100])
                    if quit_button.draw():
                        pygame.quit()
                        quit()
                        break

        if remainder == 0:
            display_text("Player 1",[350,20])
        else:
            display_text("Player 2's turn",[350,20])
        display_text("Highscore:",[580,10])
        highscore_text = font.render(f"{highscore}", False, text_color)
        screen.blit(highscore_text,(700,10))
        player_text = font.render(f"{score}", False, text_color)
        width = 50
        file = open("score.txt", "a")
        file.write(str(score2)+","+user_text+"\n")
        file.close()
        file = open("score.txt", "r")
        readthefile = file.readlines()
        sortedData = sorted(readthefile,reverse = True)
        screen.blit(player_text,(80,10))
        pygame.display.update()
        clock.tick(60)
        
def player_2_hard():
    global background, menu, state, score, click, score2, remainder
    player_2 = True
    while menu:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
            if state == 'OFF':
                for number in sequence:
                    pygame.event.pump()
                    beep.play()
                    simon_blinks_hard(number)
                state = 'ON'
                click = 0
            # Click buttons
            if state == 'ON':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    beep.play()
                    get_click(pygame.mouse.get_pos())

                if click == len(sequence):
                    sequence.append(random.choice((0, 1, 2, 3)) )
                    score += 1
                    score2 += 1
                    remainder = score2 % 2
                    print(remainder)
                    text = str('Score: {}'.format(score2))
                    state = 'OFF'
                if wrong and remainder == 1:
                    display_text("PLAYER2 LOST!!",[350,100])
                    if quit_button.draw():
                        pygame.quit()
                        quit()
                        break

                if wrong and remainder == 0:
                    display_text("PLAYER1 LOST!!",[350,100])
                    if quit_button.draw():
                        pygame.quit()
                        quit()
                        break

        if remainder == 0:
            display_text("Player 1",[350,20])
        else:
            display_text("Player 2's turn",[350,20])
        display_text("Highscore:",[580,10])
        highscore_text = font.render(f"{highscore}", False, text_color)
        screen.blit(highscore_text,(700,10))
        player_text = font.render(f"{score}", False, text_color)
        width = 50

        file = open("score.txt", "a")
        file.write(str(score2)+","+user_text+"\n")
        file.close()
        file = open("score.txt", "r")
        readthefile = file.readlines()
        sortedData = sorted(readthefile,reverse = True)

        screen.blit(player_text,(80,10))
        pygame.display.update()
        clock.tick(60)
class Button():
    def __init__(self, x ,y ,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.press = False
    def draw(self):
        movement = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.press == False:
                movement = True
                self.press = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.press = False
            
                
        
        screen.blit(self.image, self.rect)
        return movement
    
play_button = Button(screen_width // 2 - 50, screen_height // 2 - 225, play_img)
play2_button = Button(screen_width // 2, screen_height // 2 + 150, play_img)
players = Button(screen_width // 2 - 60, screen_height // 2 - 150, players_img)
quit_button = Button(screen_width // 2 - 50, screen_height // 2 -75, quit_img)
leaderboard_button = Button(screen_width // 2 - 50, screen_height // 2 + 30, leaderboard_img)
difficulty_button = Button(screen_width // 2, screen_height // 2 , difficulty_img)
easy_button = Button(screen_width // 2 - 10, screen_height // 2 - 150, easy_img)
normal_button = Button(screen_width // 2 - 50, screen_height // 2 - 75 , normal_img)
hard_button = Button(screen_width // 2 - 50, screen_height // 2  , hard_img)
easy2_button = Button(screen_width // 2 - 110, screen_height // 2 - 150, easy_img)
normal2_button = Button(screen_width // 2 - 100, screen_height // 2 - 75 , normal_img)
hard2_button = Button(screen_width // 2 - 100, screen_height // 2  , hard_img)
leaderboard_button2 = Button(screen_width // 2 - 50, screen_height // 2  - 300, leaderboard_img)

try:
    highscore = int(get_high_score())
except:
    highscore = 0

user_text = ' '


width = 205


menu = False
def menu():
    global background, remainder, user_text, text_surface, surface, sortedData, width, state,background, menu, state, score, click, score2, remainder, highscore
    menu = True

    while menu:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[0: -1]
                else:
                    user_text += event.unicode

        
        text_surface = font.render(user_text, True, (255,255,255))
        screen.blit(background,(0,0))
        display_text("Enter your name:",[20,10])
        screen.blit(text_surface,(205,10))
        if play_button.draw():
            difficulty()
        if players.draw():
            difficulty_player2()
        if quit_button.draw():
            pygame.quit()
            quit()
        if leaderboard_button.draw():
            menu = False

        
        pygame.display.update()
        clock.tick(60)
        
difficulty = False

def difficulty_player2():
    difficulty = True
    while difficulty:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
        screen.fill((30,30,30))
        
        if easy2_button.draw():
            player_2()
        if normal2_button.draw():
            player_2_normal()
        if hard2_button.draw():
            print('hard')
            player_2_hard()

        pygame.display.update()
        clock.tick(60)
def difficulty():
    difficulty = True
    while difficulty:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
        screen.fill((30,30,30))
        
        if easy_button.draw():
            easy()
        if normal_button.draw():
            print('normal')
            normal()
        if hard_button.draw():
            print('hard')
            hard()

        pygame.display.update()
        clock.tick(60)
easy = False
def easy():
    global state,background, menu, state, score, click, score2, remainder, highscore
    while easy:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
            if state == 'OFF':
                for number in sequence:
                    pygame.event.pump()
                    beep.play()
                    simon_blinks(number)
                state = 'ON'
                click = 0
            # Click buttons
            if state == 'ON':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    beep.play()
                    get_click(pygame.mouse.get_pos())
                if wrong:
                    display_text("YOU LOST!!",[350,100])
                    if quit_button.draw():
                        menu()
                        score = 0
                        score2 = 0
                        state = "ON"
                        not wrong
                if click == len(sequence):
                    sequence.append( random.choice((0, 1, 2, 3)) )
                    score += 1
                    text = str('Score: {}'.format(score))
                    screen.fill((30, 30, 30))
                    state = 'OFF'
                if highscore < score:
                    highscore = score
                with open("high score.txt", "w") as f:
                    f.write(str(highscore))
                display_text("Highscore:",[580,10])
                highscore_text = font.render(f"{highscore}", False, text_color)
                screen.blit(highscore_text,(700,10))
            width = 100
            file = open("score.txt", "a")
            file.write(str(score)+","+user_text+"\n")
            file.close()
            file = open("score.txt", "r")
            readthefile = file.readlines()
            sortedData = sorted(readthefile,reverse = True)
        player_text = font.render(f"{score}", False, text_color)
        screen.blit(player_text,(80,10))
        pygame.display.update()
        clock.tick(70)
normal = False
def normal():
    global state,background, menu, state, score, click, score2, remainder, highscore
    while normal:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
            if state == 'OFF':
                for number in sequence:
                    pygame.event.pump()
                    beep.play()
                    simon_blinks_normal(number)
                state = 'ON'
                click = 0
            # Click buttons
            if state == 'ON':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    beep.play()
                    get_click(pygame.mouse.get_pos())
                if wrong:
                    display_text("YOU LOST!!",[350,100])
                    if quit_button.draw():
                        menu()
                        score = 0
                        score2 = 0
                        state = "ON"
                        not wrong
                    break
                if click == len(sequence):
                    sequence.append( random.choice((0, 1, 2, 3)) )
                    score += 1
                    text = str('Score: {}'.format(score))
                    screen.fill((30, 30, 30))
                    state = 'OFF'
                if highscore < score:
                    highscore = score
                with open("high score.txt", "w") as f:
                    f.write(str(highscore))
                display_text("Highscore:",[580,10])
                highscore_text = font.render(f"{highscore}", False, text_color)
                screen.blit(highscore_text,(700,10))
            width = 100
            file = open("score.txt", "a")
            file.write(str(score)+","+user_text+"\n")
            file.close()
            file = open("score.txt", "r")
            readthefile = file.readlines()
            sortedData = sorted(readthefile,reverse = True)
        player_text = font.render(f"{score}", False, text_color)
        screen.blit(player_text,(80,10))
        pygame.display.update()
        clock.tick(70)
hard = False
def hard():
    global state,background, menu, state, score, click, score2, remainder, highscore
    while hard:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
            if state == 'OFF':
                for number in sequence:
                    pygame.event.pump()
                    beep.play()
                    simon_blinks_hard(number)
                state = 'ON'
                click = 0
            # Click buttons
            if state == 'ON':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    beep.play()
                    get_click(pygame.mouse.get_pos())
                if wrong:
                    display_text("YOU LOST!!",[350,100])
                    if quit_button.draw():
                        menu()
                        score = 0
                        score2 = 0
                        state = "ON"
                        not wrong
                if click == len(sequence):
                    sequence.append( random.choice((0, 1, 2, 3)) )
                    score += 1
                    text = str('Score: {}'.format(score))
                    screen.fill((30,30,30))
                    state = 'OFF'
                if highscore < score:
                    highscore = score
                with open("high score.txt", "w") as f:
                    f.write(str(highscore))
                display_text("Highscore:",[580,10])
                highscore_text = font.render(f"{highscore}", False, text_color)
                screen.blit(highscore_text,(700,10))
            width = 100
            file = open("score.txt", "a")
            file.write(str(score)+","+user_text+"\n")
            file.close()
            file = open("score.txt", "r")
            readthefile = file.readlines()
            sortedData = sorted(readthefile,reverse = True)
        player_text = font.render(f"{score}", False, text_color)
        screen.blit(player_text,(80,10))
        pygame.display.update()
        clock.tick(70)
menu()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((30,30,30))
    width = 100
    file = open("score.txt", "a")
    file.write(str(score)+","+user_text+"\n")
    file.close()
    file = open("score.txt", "r")
    readthefile = file.readlines()
    sortedData = sorted(readthefile,reverse = True)
    for line in range(10):
        surface = font.render(str(line+1)+": "+str(sortedData[line]), 2,(255,255,255))
        width += 50
        screen.blit(surface,(100,width))
    pygame.display.update()
    clock.tick(70)
