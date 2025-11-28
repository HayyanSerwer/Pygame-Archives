import pygame, sys
import random

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Space invader')




def main():
    global main_font, level, lives, health
    run = True
    FPS = 60
    lives = 1
    health = 100
    main_font = pygame.font.SysFont("comicsans", 30)
    clock = pygame.time.Clock()

BLACK = [0,0,0]

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (Player1_rect.x + 16,Player1_rect.y + 10))


Player1 = pygame.image.load("sprites/tree2.png").convert()
Player1_rect = Player1.get_rect(center = (150, 256))

Player1_startx = 150
Player1_starty = 256
Player1_speed = 0
Player1_speedx = 0
Player1_speedy = 0

enemy_startx = random.randint(500, screen_width - 50)
enemy_starty = random.randrange(50, screen_height)
enemy_speed = 7
enemy_width = 50
enemy_height = 50

bullet = pygame.image.load("sprites/banana.png").convert()
bullet_rect = bullet.get_rect()
bullet_startx = Player1_startx
bullet_starty = Player1_starty
bullet_speed = 7
bullet_state = "ready"


enemy = pygame.image.load("sprites/mike.png").convert()
enemy_rect = enemy.get_rect(center = (enemy_startx, enemy_starty))

BLACK = [0,0,0]
while True:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                Player1_speedx += 7
            if event.key == pygame.K_a:
                Player1_speedx -= 7
            if event.key == pygame.K_w:
                Player1_speedy -=5
            if event.key == pygame.K_s:
                Player1_speedy += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                Player1_speedx -= 7
            if event.key == pygame.K_a:
                Player1_speedx += 7
            if event.key == pygame.K_w:
                Player1_speedy +=5
            if event.key == pygame.K_s:
                Player1_speedy -= 5

        #BOUNDARY COLLISIONS
        if Player1_rect.right >= screen_width:
            Player1_rect.right = screen_width
        if Player1_rect.top <= 0:
            Player1_rect.top = 0
        if Player1_rect.bottom >= screen_height:
            Player1_rect.bottom = screen_height
        if Player1_rect.left <= 0:
            Player1_rect.left = 0

        #bullet


        if Player1_rect.colliderect(enemy_rect):
            enemy_startx = random.randint(500, screen_width - 50)
                        
    screen.fill(BLACK)
    main()
    lives_label = main_font.render(f"Lives:{lives}", 1, (255, 255, 255))
    Health_label = main_font.render(f"Health:{health}", 1, (255, 255, 255))
    screen.blit(enemy, enemy_rect)
    screen.blit(lives_label, (10,10))
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
                fire_bullet(Player1_rect.x, bullet_starty)

    if bullet_state is "fire":
        fire_bullet(Player1_rect.x, bullet_starty)
        bullet_rect.x -= bullet_speed
    bullet_rect.x -= bullet_speed
    Player1_rect.x += Player1_speedx
    Player1_rect.y += Player1_speedy
    screen.blit(Player1, Player1_rect)
    screen.blit(Health_label, (110, 10))

    pygame.display.flip()
    clock.tick(60)
