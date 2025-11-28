import pygame, sys
import os
import random
import math
from pygame.color import Color

pygame.init()
clock = pygame.time.Clock()

gravity = 1

screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Movement')

background = pygame.image.load('Assets/background1.png')
tower = pygame.image.load('Assets/Tower1.png')
tower_rect = tower.get_rect()
font = pygame.font.Font("freesansbold.ttf", 24)

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

Player1 = pygame.image.load(os.path.join("assets", "Player.png"))
Player1_rect = Player1.get_rect(center=(400,440))
left_enemy = [pygame.image.load(os.path.join("Assets/Enemy", "L1E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L2E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L3E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L4E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L5E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L6E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L7E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L8E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L9P.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L10P.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L11P.png"))
        ]


bullet_x = 500
bullet_y = 0
bullet = pygame.image.load("assets/bullet.png")
bullet_rect = bullet.get_rect(center=(bullet_x, bullet_y))
bullet_speedx = 5
bullet_speedy = 0
bullet_state = "ready"
Player1_speed = 0
Player1_speedx = 0
Player1_speedy = 0

enemy_startx = 0
enemy_starty = 0

Tower_health = 100
Player_health = 100
score = 0

jump = False
jumpcount = 5

black = [0,0,0]
white = [255,255,255]

def bullet_fire(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet,(x+10,y+30))

def display_text(str, location):
    # Assign text contents and position
    words = font.render(str, True, Color('white'))
    ss_text = words
    rt_text = words.get_rect()
    rt_text.x = location[0]
    rt_text.y = location[1]

    # Draw to screen at specified position
    screen.blit(ss_text, rt_text)
    
def Collide(enemy_startx, enemy_starty, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_startx-bullet_x,2) + math.pow(enemy_starty - bullet_y,2))
    if distance < 50:
        return True
    else:
        return False 

game_over = False
def game_over():
    game_over = True
    while game_over:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
            screen.blit(background,(0,0))
            display_text("GAME OVER:",[400,250])
        pygame.display.update()
        clock.tick(60)
class Enemy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.stepIndex = 0
        # Health
        self.hitbox = (self.x, self.y, 64, 64)
        self.health = 30

    def step(self):
        if self.stepIndex >= 33:
            self.stepIndex = 0

    def draw(self, win):
        self.hitbox = (self.x + 20, self.y + 10, 30, 45)
        pygame.draw.rect(win, (255, 0, 0), (self.x + 0, self.y - 100, 0, 0))
        if self.health >= 0:
            pygame.draw.rect(win, (0, 255, 0), (self.x + 15, self.y, self.health, 10))
        self.step()
        win.blit(left_enemy[self.stepIndex // 3], (self.x, self.y))
        self.stepIndex += 1

    def move(self):
        global bullet_x
        global Tower_health, score
        self.x -= speed
        collision = Collide(self.x, self.y, bullet_x, bullet_y)
        collision2 = Collide(self.x, self.y, Player1_rect.x, Player1_rect.y)
        if collision:
            score += 1
            enemies.remove(enemy)
            bullet_x = 1000
        if collision2:
            print('hit')
            Player1_rect.x = 100
        if self.x <= 200:
            Tower_health -= 15
            enemies.remove(enemy)
        if Tower_health <= 0:
            game_over()
                
            
    def off_screen(self):
        return not (self.x >= -50 and self.x <= screen_width + 50)


enemies = []
speed = 3
kills = 0
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if bullet_state == "ready":
                    bullet_x = Player1_rect.x
                    bullet_y = Player1_rect.y
                    bullet_fire(Player1_rect.x, bullet_y)
            
    if not(jump):
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount <=  0:
                neg = -1
            Player1_rect.y -= (jumpcount ** 2) * 0.5 * neg
            jumpcount -= 1
            Player1_rect.y += 1
        else:
            jump = False
            jumpcount = 10

            
        #BOUNDARY COLLISIONS
        if Player1_rect.right >= screen_width:
            Player1_rect.right = screen_width
        if Player1_rect.top <= 0:
            Player1_rect.top = 0
        if Player1_rect.bottom >= screen_height:
            Player1_rect.bottom = screen_height
        if Player1_rect.left <= 0:
            Player1_rect.left = 0

    Player1_rect.x += Player1_speedx
    Player1_rect.y += Player1_speedy

    screen.blit(background,(0,0))
    screen.blit(Player1,Player1_rect)
    screen.blit(tower,(0,190))
    if bullet_state == "fire":
        bullet_fire(bullet_x, bullet_y)
        bullet_x += bullet_speedx
    if len(enemies) == 0:
        enemy = Enemy(1000, 400, speed)
        enemies.append(enemy)
        if speed <= 10:
            speed += 1
    if bullet_x >= 1000:
        bullet_x = Player1_rect.x
        bullet_y = 500
        bullet_state = "ready"
    
    for enemy in enemies:
        enemy.draw(screen)
    for enemy in enemies:
        enemy.move()
        if enemy.off_screen() or enemy.health == 0:
            enemies.remove(enemy)
    Tower_health_text = font.render(f"{Tower_health}", False, text_color)
    screen.blit(Tower_health_text,(160,0))
    Score_text = font.render(f"{score}", False, text_color)
    screen.blit(Score_text,(880,0))
    display_text("Tower health:",[0,0])
    display_text("Score:",[800,0])
    pygame.display.flip()
    clock.tick(60)
