import pygame, sys
import os
import random
from pygame.color import Color
from pygame import mixer
import math

pygame.init()
clock = pygame.time.Clock()
#ball reset command
def circleReset():
    global circle_speedx, circle_speedy
    circle.center = (screen_width/2, screen_height/2)
    circle_speedy *= random.choice((1,-1))
    circle_speedx *= random.choice((1, -1))

#basic variables

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')


circle = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.image.load("sprites/player.png")
player_rect = player.get_rect(center=(screen_width - 20, screen_height/2 - 70))
player2 = pygame.image.load("sprites/player2.png")
player2_rect = player.get_rect(center=(20, screen_height/2 - 70))
button_plus = pygame.Rect(200, 10, 30,30)
button_minus = pygame.Rect(250, 10, 30,30)

menu_button = pygame.Rect(360, 150, 130,50)
menu_button2 = pygame.Rect(360, 230, 130,50)
menu_button3 = pygame.Rect(360, 300, 130,50)

pause_button = pygame.Rect(200, 10, 130,50)
pause_button2 = pygame.Rect(400, 10, 130,50)
pause_button3 = pygame.Rect(600, 10, 170,50)

volume_button = pygame.Rect(370, 255, 30,30)
volume_button2 = pygame.Rect(430, 255, 30,30)
back = pygame.Rect(50, 50, 130,30)

game_over_button = pygame.Rect(200, 10, 130,50)

dark_mode = pygame.Rect(380,550,40,30)
light_mode = pygame.Rect(320,550,40,30)

light_gray = [211,211,211]
grey = [50,50,50]
bg_color = [0,0,0]
white = [255,255,255]
blue = [0,0, 205]
black = [0,0,0]
player1_color = [255,255,255]
player2_color = [255,255,255]
circle_color = [255,255,255]
text_color = [255,255,255]

player_score = 0
player2_score = 0

menu_background = pygame.image.load("sprites/background_04.png")

#Loading the images.
play_img = pygame.image.load('sprites/play.png')
quit_img = pygame.image.load('sprites/quit.png')
level_img = pygame.image.load('sprites/levels.png')
level1_img = pygame.image.load('sprites/level1.png')
level2_img = pygame.image.load('sprites/level2.png')
level3_img = pygame.image.load('sprites/level3.png')
back_img = pygame.image.load('sprites/back.png')



brick = pygame.image.load('sprites/REDBRICKS.png')
brick_rect = brick.get_rect(center=(400, 400))
brick2 = pygame.image.load('sprites/REDBRICKS.png')
brick2_rect = brick.get_rect(center=(500, 400))
brick3 = pygame.image.load('sprites/REDBRICKS.png')
brick3_rect = brick.get_rect(center=(650,400))
brick4 = pygame.image.load('sprites/REDBRICKS.png')
brick4_rect = brick.get_rect(center=(400, 400))
brick5 = pygame.image.load('sprites/REDBRICKS.png')
brick5_rect = brick.get_rect(center=(400, 500))
brick6 = pygame.image.load('sprites/REDBRICKS.png')
brick6_rect = brick.get_rect(center=(400,650))




speed = 5
speed1 = 0
speed2 = 4
circle_speed = 5
circle_speedx = 5
circle_speedy = 5

#A class that is used to create button images that can be clicked to perform tasks using an if statement.
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

#Buttons being made(Not displayed onto the screen with these lines)
play_button = Button(screen_width // 2 - 50, screen_height // 2 - 225, play_img)
level_button = Button(screen_width // 2 - 50, screen_height // 2 - 150, level_img)
quit_button = Button(screen_width // 2 - 50, screen_height // 2 - 75, quit_img)
level1_button = Button(screen_width // 2 - 350, screen_height // 2 - 200, level1_img)
level2_button = Button(screen_width // 2 - 350, screen_height // 2 - 100, level2_img)
level3_button = Button(screen_width // 2 - 350, screen_height // 2, level3_img)
back_button = Button(screen_width - 150, screen_height // 2 - 300, back_img)

#PlayerAI
def player_ai():
    global speed2
    if circle.centerx <= 500:
        if player2_rect.top < circle.y:
            player2_rect.top += speed2
        if player2_rect.top > circle.y:
            player2_rect.top -= speed2

#Font used
font = pygame.font.Font("pixelated.ttf", 32)
options = False



#Creating the levels options.
def options():
    global menu_background, menu, brickx, bricky
    options = True
    while options:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
            screen.blit(menu_background,(0,0))
            if level1_button.draw():
                menu_background = pygame.image.load('sprites/background_021.png')
                menu = False
                options = False
                running = True
                brick_rect.y = 400
                brick_rect.x = 400
                brick2_rect.y = 400
                brick2_rect.x = 500
                brick3_rect.y = 400
                brick3_rect.x = 650
                brick6_rect.x = 400
                brick6_rect.y = 650
            if level2_button.draw():
                menu_background = pygame.image.load('sprites/background_03.jpg')
                menu = False
                options = False
                running = True
                brick_rect.y = 400
                brick_rect.x = 400
                brick2_rect.y = 500
                brick2_rect.x = 400
                brick3_rect.y = 100
                brick3_rect.x = 300
                brick5_rect.x = 1000
                brick5_rect.y = 1000
                brick6_rect.x = 500
                brick6_rect.y = 100
            if level3_button.draw():
                menu_background = pygame.image.load('sprites/background_04.png')
                menu = False
                options = False
                running = True
                brick2_rect.y = 100
                brick2_rect.x = 520
                brick_rect.y = 100
                brick_rect.x = 430
                brick3_rect.y = 100
                brick3_rect.x = 610
                brick5_rect.x = 400
                brick5_rect.x = 650
                brick6_rect.x = 500
                brick6_rect.y = 400
            if back_button.draw():
                options = False
                screen.fill(black)
                menu()

            
        
        pygame.display.update()
        clock.tick(60)

#Creating the menu.
menu = False
def menu():
    global menu_background
    menu = True
    while menu:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()

        screen.blit(menu_background,(0,0))

        if play_button.draw():
            menu = False
            pause = True
            menu_background = pygame.image.load("sprites/background_021.png")

        if quit_button.draw():
            pygame.quit()
            quit()
        if level_button.draw():
            options()
            screen.fill((0,0,0))
            menu = False


        pygame.display.update()
        clock.tick(60)

def pause():
    global paused
    global blue
    global menu_background, player_score, player2_score
    paused = True
    while paused:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
            screen.blit(menu_background,(0,0))
            if level1_button.draw():
                menu_background = pygame.image.load('sprites/background_021.png')
                menu = False
                options = False
                paused = False
                running = True
                player_score = 0
                player2_score = 0
                player_rect.y = screen_height/2
                player2_rect.y = screen_height/2
                brick_rect.y = 400
                brick_rect.x = 400
                brick2_rect.y = 400
                brick2_rect.x = 500
                brick3_rect.y = 400
                brick3_rect.x = 650
                brick6_rect.x = 500
                brick6_rect.y = 400
            if level2_button.draw():
                menu_background = pygame.image.load('sprites/background_03.jpg')
                menu = False
                options = False
                paused = False
                running = True
                player_score = 0
                player2_score = 0
                player_rect.y = screen_height/2
                player2_rect.y = screen_height/2
                brick_rect.y = 400
                brick_rect.x = 400
                brick2_rect.y = 500
                brick2_rect.x = 400
                brick3_rect.y = 100
                brick3_rect.x = 300
                brick5_rect.x = 1000
                brick5_rect.y = 1000
                brick6_rect.x = 500
                brick6_rect.y = 100
            if level3_button.draw():
                menu_background = pygame.image.load('sprites/background_04.png')
                menu = False
                options = False
                paused = False
                player_score = 0
                player2_score = 0
                running = True
                player_rect.y = screen_height/2
                player2_rect.y = screen_height/2
                brick2_rect.y = 100
                brick2_rect.x = 520
                brick_rect.y = 100
                brick_rect.x = 430
                brick3_rect.y = 100
                brick3_rect.x = 610
                brick5_rect.x = 1000
                brick5_rect.y = 1000
                brick6_rect.x = 500
                brick6_rect.y = 400
            if quit_button.draw():
                running = False
            if player_score >= 6:
                display_text("You won!",[screen_width/2,screen_height/2])
            if player2_score >= 6:
                display_text("Opponent won!!",[screen_width/2,screen_height/2])
        pygame.display.update()
        clock.tick(60)

#A command that is used to display text onto the screen, barely used in the code. Was used when the game was in developement stage.        
def display_text(str, location):
    # Assign text contents and position
    words = font.render(str, True, Color('white'))
    ss_text = words
    rt_text = words.get_rect()
    rt_text.x = location[0]
    rt_text.y = location[1]

    # Draw to screen at specified position
    screen.blit(ss_text, rt_text)


#The main game loop.
menu()
running = False
while True:
    running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                speed1 -= speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                speed1 += speed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                speed1 += speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                speed1 -= speed

                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause()

    if player_rect.top <= 0:
        player_rect.top = 0
    if player_rect.bottom >= screen_height:
        player_rect.bottom = screen_height
    if player2_rect.top <= 0:
        player2_rect.top = 0
    if player2_rect.bottom >= screen_height:
        player2_rect.bottom = screen_height
        
    if circle.top <= 0 or circle.bottom >= screen_height:
        circle_speedy *= -1
    if circle.left <= 0:
        circleReset()
        player_score += 1
    if circle.right >= screen_width:
        circleReset()
        player2_score += 1

    if circle.colliderect(player_rect) or circle.colliderect(player2_rect):
        circle_speedx *= -1



        
        

    player_ai()
            
    if brick_rect.colliderect(circle):
        circle_speedx *= -1
    if brick2_rect.colliderect(circle):
        circle_speedx *= -1
    if brick3_rect.colliderect(circle):
        circle_speedx *= -1 
    if brick5_rect.colliderect(circle):
        circle_speedx *= -1
    if brick6_rect.colliderect(circle):
        circle_speedx *= -1

    circle.x -= circle_speedx
    circle.y -= circle_speedy



    player_rect.y += speed1


    screen.blit(menu_background,(0,0))
    screen.blit(player, player_rect)
    screen.blit(player2, player2_rect)
    pygame.draw.ellipse(screen, circle_color, circle)
    screen.blit(brick,brick_rect)
    screen.blit(brick2,brick2_rect)
    screen.blit(brick3,brick3_rect)
    screen.blit(brick5,brick5_rect)
    screen.blit(brick6,brick6_rect)


    if player_score >= 6 or player2_score >= 6:
        pause()
    


    player_text = font.render(f"{player_score}", False, text_color)
    screen.blit(player_text,(405,0))

    player2_text = font.render(f"{player2_score}", False, text_color)
    screen.blit(player2_text,(360,0))

    
    pygame.display.flip()
    clock.tick(60)

            
