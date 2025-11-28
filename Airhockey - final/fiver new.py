import pygame, sys
import random
from os import path
import os


def gethighscore():
    with open("highscore.txt", "r") as f:
        return f.read()

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    if ball_rect.top <=0 or ball_rect.bottom >= screen_height:
        ball_speed_y *= -1
    if ball_rect.colliderect(goal):
        player_score += 1
        ball_restart()
    if ball_rect.colliderect(goal2):
        ball_restart()
        opponent_score += 1
    if ball_rect.colliderect(Player1_rect) or ball_rect.colliderect(Player2_rect):
        ball_speed_x *= -1
        

def ball_restart():
    global ball_speed_y, ball_speed_x
    ball_rect.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1, -1))


def ScreenText(text, color, x,y, size, style, bold=False, itallic = False):
    font = pygame.font.SysFont(style,size, bold=bold, italic=itallic)
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x,y))

pygame.init()
clock = pygame.time.Clock()

gravity = 1

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('AirHockey')

light_grey = [200,200,200]
line = pygame.Rect(screen_width/2 - 15, screen_height/2, 255,255)
boundary = pygame.Rect(screen_width - 10, screen_height - 270, 10, 340)
boundary2 = pygame.Rect(screen_width - 10, screen_height/2 -300, 10, 270)
boundary3 = pygame.Rect(0, screen_height - 270, 10, 340)
boundary4 = pygame.Rect(0, screen_height/2 -300, 10, 270)
goal = pygame.Rect(screen_width - 10, screen_height/2 - 120, 10, 150)
goal2 = pygame.Rect(screen_width/2 - 400, screen_height/2 - 120, 10, 150)
BLACK = [0,0,0]
white = [255,255,255]
red = [255, 0, 0]

ball = pygame.image.load("sprites/puck1.png").convert()
ball_rect = ball.get_rect(center = (400, 256))
ball_speed_x = 4
ball_speed_y = 4

Player1 = pygame.image.load("sprites/red_paddle1.png").convert()
Player1_rect = Player1.get_rect(center = (150, 256))



Player2 = pygame.image.load("sprites/blue_paddle1.png").convert()
Player2_rect = Player2.get_rect(center = (650, 256))

Player1_speed = 0
Player1_speedx = 0
Player1_speedy = 0
Player2_speed = 0
Player2_speedx = 0
Player2_speedy = 0

player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

try:
    highscore = int(gethighscore())
except:
    highscore = 0
while True:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Player1_speedx += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                Player1_speedx -= 7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                Player1_speedx -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                Player1_speedx += 7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Player1_speedy -=5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                Player1_speedy +=5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                Player1_speedy += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                Player1_speedy -= 5


        #PLAYER 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                Player2_speedx += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                Player2_speedx -= 7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Player2_speedx -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                Player2_speedx += 7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player2_speedy -=5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                Player2_speedy +=5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Player2_speedy += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                Player2_speedy -= 5

        #PLAYER COLLISIONS
        if Player1_rect.top <= 0:
            Player1_rect.top = 0
        if Player1_rect.bottom >= screen_height:
            Player1_rect.bottom = screen_height
        if Player2_rect.top <= 0:
            Player2_rect.top = 0
        if Player2_rect.bottom >= screen_height:
            Player2_rect.bottom = screen_height
        if Player2_rect.right >= screen_width:
            Player2_rect.right = screen_width
        if Player1_rect.left <= 0:
            Player1_rect.left = 0
        if Player1_rect.right >= screen_width/2:
            Player1_rect.right = screen_width/2
        if Player2_rect.left <= screen_width/2:
            Player2_rect.left = screen_width/2

        #boundary collision
    if ball_rect.colliderect(boundary) or ball_rect.colliderect(boundary2) or ball_rect.colliderect(boundary3) or ball_rect.colliderect(boundary4):
        ball_speed_x *= -1

        if player_score == 5 or opponent_score == 5:
            pygame.quit()
            sys.exit()
            

    Player1_rect.x += Player1_speedx
    Player1_rect.y += Player1_speedy
    Player2_rect.x += Player2_speedx
    Player2_rect.y += Player2_speedy

    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y
    screen.fill(BLACK)
    screen.blit(Player1, Player1_rect)
    screen.blit(Player2, Player2_rect)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))
    screen.blit(ball, ball_rect)
    ball_animation()

    


    pygame.draw.rect(screen, white, goal)
    pygame.draw.rect(screen, white, goal2)
    pygame.draw.rect(screen, BLACK, boundary)
    pygame.draw.rect(screen, BLACK, boundary2)
    pygame.draw.rect(screen, BLACK, boundary3)
    pygame.draw.rect(screen, BLACK, boundary4)

    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text,(405,0))

    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text,(380,0))



    pygame.display.flip()
    clock.tick(60)

