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

menu = False
def menu():
    global background
    menu = True
    while menu:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()

        screen.blit(background,(0,0))

        if play_button.draw():
            menu = False
        if players.draw():
            print('wasd')
        if quit_button.draw():
            pygame.quit()
            quit()


        pygame.display.update()
        clock.tick(60)

menu()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(background,(0,0))



    pygame.display.update()
    clock.tick(70)
