import pygame, sys
import os
import random


pygame.init()
clock = pygame.time.Clock()

gravity = 1

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Movement')


#background2_rect = background2.get_rect()
background = pygame.image.load(os.path.join("sprites", "background.png"))


font = pygame.font.Font('freesansbold.ttf', 30)  
text = "Game Over"

Player1 = pygame.image.load(os.path.join("sprites", "car4.png")).convert_alpha()
Player1_rect = Player1.get_rect(center=(400,520))

paused = False

def create_background():
    screen.blit(background,(0,background_starty))
    screen.blit(background,(0,background_starty - 650))
    

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

def cars(carsx, carsy):
    global car, car_rect
    car = pygame.image.load(os.path.join("sprites", "car5.png"))
    car_rect = car.get_rect(center=(car_startx,car_starty))
    screen.blit(car, car_rect)
    if Player1_rect.colliderect(car_rect):
        ScreenText(text, white, 50,50, size = 50, style ="freesansbold.ttf")
        pause()
        paused = True

        




Player1_speed = 0
Player1_speedx = 0
Player1_speedy = 0

jump = False
jumpcount = 5

black = [0,0,0]
white = [255,255,255]

background_speed = 3
background2_speed = 3

car_startx = random.randrange(0, screen_width)
car_starty = -500
car_speed = 7
car_width = 50
car_height = 50

background_starty = 0
background2_starty = 0

background_startx = 0
background2_startx = 0


userInput = pygame.key.get_pressed()
while True:

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()                                          
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                Player1_speedx += 7
            if event.key == pygame.K_a:
                Player1_speedx -= 7
                        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                Player1_speedx -= 7
            if event.key == pygame.K_a:
                Player1_speedx += 7
                


                

#First remember that if jumpCount >= 10 then neg (which is like gravity) is equal to 1. This means that your character will go up as jumpCount squared * 0.5 is going to be * by 1. But if jumpCount is < 0 (or if jumpCount is a negative number) then neg is equal to 1,
                #so jumpCount squared * 0.5 will be * by negative 1, so y will be minused by a negative number, so y will add it because a positive minus a negative number (p - -d) be the same as adding the number (p - -d is the same as     p + d). Therefore, your y value will go down, because the lower on the window you go, the higher your 'y' value will be. Then, jumpCount is being minused by 1 everytime the loop will loop around, so your character goes up but at a decreasing rate.
#Then, when jumpCount reaches 0, like the peak of a graph, neg becomes -1 and you start going down. Then, when jumpCount becomes -11, it is  < 10, so the else statement plays, isjump is false, and the jumping stops.



        #BOUNDARY COLLISIONS
        if Player1_rect.right >= screen_width:
            Player1_rect.right = screen_width
        if Player1_rect.top <= 0:
            Player1_rect.top = 0
        if Player1_rect.bottom >= screen_height:
            Player1_rect.bottom = screen_height
        if Player1_rect.left <= 0:
            Player1_rect.left = 0


    screen.fill(white)
    Player1_rect.x += Player1_speedx
    Player1_rect.y += Player1_speedy





    car_starty += car_speed
    background_starty += background_speed
    background2_starty += background2_speed

    if car_starty > screen_height:
        car_starty = 0 - car_rect.y
        car_startx = random.randrange(0, screen_width)
        
    create_background()
    screen.blit(Player1,Player1_rect)
    cars(car_startx, car_starty)
    
    if background_starty >= 650:
        background_starty = 0

        


    
    pygame.display.flip()
    clock.tick(60)
