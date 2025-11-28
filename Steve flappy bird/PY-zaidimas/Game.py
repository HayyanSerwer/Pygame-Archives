import pygame, sys
import os
import random


pygame.init()
clock = pygame.time.Clock()

gravity = 1

text = "Game Over"

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Movement')
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
light_grey = (255,255,255)

def create_obsticle():
        random_obsticle_pos = random.choice(obsticle_height)
        bottom_obsticle = obsticle_surface.get_rect(midtop = (900, random_obsticle_pos))
        top_obsticle = obsticle_surface.get_rect(midbottom = (900,random_obsticle_pos - 125))
        return bottom_obsticle, top_obsticle

def move_obsticles(obsticles):
        for obsticle in obsticles:
                obsticle.centerx -= 5
        return obsticles

def draw_obsticles(obsticles):
        for obsticles in obsticles:
                screen.blit(obsticle_surface, obsticles)
def check_collision(obsticles):
        global score
        for obsticle in obsticles:
                if Player1_rect.colliderect(obsticle):
                        ScreenText(text, white, 50,50, size = 50, style ="freesansbold.ttf")
                        pause()
                        paused = True  
        if Player1_rect.top <= -50 or Player1_rect.bottom >= 450:
                score += 1

def obsticle_score_check():
    global score, score_input
    if obsticle_list:
        for obsticle in obsticle_list:
            if 95 < obsticle.centerx < 105 and score_input:
                score += 1
                score_input = False
            if obsticle.centerx < 0:
                score_input = True
def pause():
    paused = True

    while paused:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()

            

        pygame.display.update()
        clock.tick(60)

def ScreenText(text, color, x,y, size, style, bold=False, itallic = False):
    font = pygame.font.SysFont(style,size, bold=bold, italic=itallic)
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x,y))


  
score_input = True
obsticle_surface = pygame.image.load("obsticle.png")
background = pygame.image.load('background1.png')
obsticle_list = []
SPAWNOBSTICLE = pygame.USEREVENT
pygame.time.set_timer(SPAWNOBSTICLE, 1200)
obsticle_height = [200,300,400]
Player1 = pygame.image.load( "steve1.png")
Player1_rect = Player1.get_rect(center=(150,256))

Player1_speed = 0
Player1_speedx = 0
Player1_speedy = 0

black = [0,0,0]
white = [255,255,255]
while True:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                Player1_speedx += 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                Player1_speedx -= 3
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Player1_speedx -= 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                Player1_speedx += 3
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Player1_speedy -=5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                Player1_speedy +=5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                Player1_speedy += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                Player1_speedy -= 5
        if event.type == SPAWNOBSTICLE:
                obsticle_list.extend(create_obsticle())

    Player1_rect.x += Player1_speedx
    Player1_rect.y += Player1_speedy

    screen.fill(white)
    screen.blit(background,(0,0))

    screen.blit(Player1,Player1_rect)

    obsticle_list = move_obsticles(obsticle_list)
    draw_obsticles(obsticle_list)
    check_collision(obsticle_list)
    obsticle_score_check()
    score_text = font.render(f"{score}", False, light_grey)
    screen.blit(score_text,(405,0))
    pygame.display.flip()
    clock.tick(60)
