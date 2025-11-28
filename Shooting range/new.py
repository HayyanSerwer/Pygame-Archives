import pygame, sys
import random

pygame.init()
clock = pygame.time.Clock()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Shooting range')
crosshair = pygame.image.load('crosshair1.png').convert()


target_position_x = random.randrange(50, 700)
target_position_y = random.randrange(80, 500)
target = pygame.Rect(target_position_x, target_position_y, 50, 50)


target2 = pygame.Rect(target_position_x, target_position_y, 50, 50)


target3 = pygame.Rect(target_position_x, target_position_y, 50, 50)

BLACK = [0,0,0]
red =  [255, 0, 0]
white = [255, 255,255]

player_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)
while True:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center = event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
                if crosshair_rect.colliderect(target):
                    target.y = random.randrange(80, 500)
                    target.x =  random.randrange(50, 700)
                    player_score += 1
                if crosshair_rect.colliderect(target2):
                    target2.y = random.randrange(80, 500)
                    target2.x = random.randrange(50, 700)
                if crosshair_rect.colliderect(target3):
                    target3.y = random.randrange(80, 500)
                    target3.x = random.randrange(50, 700)
     





    screen.fill(BLACK)
    pygame.draw.rect(screen, red, target)
    pygame.draw.rect(screen, red, target2)
    pygame.draw.rect(screen, red, target3)
    player_text = game_font.render(f"{player_score}", False, white)
    screen.blit(player_text,(405,0))

    pygame.display.flip()
    clock.tick(60)
