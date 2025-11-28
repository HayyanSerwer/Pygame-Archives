import pygame
import pickle
import time
import sys
import random
from os import path
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

tile_size = 50


background = pygame.image.load("background_01.jpg").convert()
play_img = pygame.image.load('play.png')
players_img = pygame.image.load('players.png')
quit_img = pygame.image.load('quit.png')

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
position = (10,10)
text = str('Score: {}'.format(score))

def simon_blinks(key):
    buttons[key] = buttons_on[key]

    # blit
    for i in buttons:
        screen.blit(buttons[i], rects[i])
        screen.blit(font.render(text, True, color), position) 
        pygame.display.update()

    # blink for 250ms
    time.sleep(0.25)

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
players = Button(screen_width // 2 - 60, screen_height // 2 - 150, players_img)
quit_button = Button(screen_width // 2 - 50, screen_height // 2 - 75, quit_img)

menu = True



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    if menu == True:
        if play_button.draw():
            menu = False

        if players.draw():
            print('wasd')
        if quit_button.draw():
            pygame.quit()
            quit()
    else:
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
                text = 'YOU LOSE!'
                position = (192, 64)
                laugh.play()
                screen.fill((30, 30, 30))
                break
            if click == len(sequence):
                sequence.append( random.choice((0, 1, 2, 3)) )
                score += 1
                text = str('Score: {}'.format(score))
                screen.fill((30, 30, 30))
                state = 'OFF'


    pygame.display.update()
    clock.tick(70)
