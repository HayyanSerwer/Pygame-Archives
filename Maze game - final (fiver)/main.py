import pygame
import constants
import pickle
import os
from os import path
from pygame.locals import *

pygame.init()
screen_width = 500
screen_height = 500

clock = pygame.time.Clock()
fps = 60

score = 0

font = pygame.font.SysFont("freesansbold.ttf", 24)
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

background = pygame.image.load("background_01.jpg")
tile_size = 16

loading_background = pygame.image.load(os.path.join("loading_screen.png"))
end_screen = pygame.image.load(os.path.join("end_screen.png"))
play_img = pygame.image.load('play.png')
quit_img = pygame.image.load('quit.png')

level = 1
max_levels = 3
restart_image = pygame.image.load('restart2.png')

game_over = 0


def display_text(text, font, text_col, x, y):
    img =  font.render(text, True, text_col)
    screen.blit(img, (x,y))


def reset_level(level):
    global map_data
    player.reset(50, 30)
    gate_group.empty()
    coin_group.empty()
    if path.exists(f'levels{level}_data'):
        pickle_in = open(f'levels{level}_data', 'rb')
        map_data = pickle.load(pickle_in)
    world = World(map_data)
    return world

class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        image.set_colorkey(constants.BLACK)

        # Return the image
        return image

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

ORANGE_METAL            = (576, 720, 70, 70)
GREY_METAL           = (279, 0, 70, 70)
PURPLE          = (497, 1, 70, 70)
BLUE1   = (593, 81, 70, 40)
BLUE2 = (584, 120, 70, 40)

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

class Player():
    def __init__(self,x,y):
        self.reset(x,y)

    def update(self, game_over):
        dx = 0
        dy = 0
        walk_cooldown = 5
        overlap = 20
        if game_over == 0:
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                self.vel_y = -2
                dy += self.vel_y

            if key[pygame.K_s]:
                self.vel_y = +2
                dy += self.vel_y
                

                
            if key[pygame.K_a] or key[pygame.K_a]:
                dx -= 2
                self.direction = -1
            if key[pygame.K_d] or key[pygame.K_d]:
                self.direction = 1
                dx += 2




            
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_walk):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_walk[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]
                


            
            self.mid_air = True
            for tile in world.tile_list:
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.mid_air = False

            if pygame.sprite.spritecollide(self,gate_group, False):
                game_over = 1


            self.rect.x += dx
            self.rect.y += dy

        screen.blit(self.image, self.rect)
        return game_over

    def reset(self,x,y):
        self.images_walk = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1,5):
            img_walk = pygame.image.load('sprite1.png')
            img_walk = pygame.transform.scale(img_walk,(12,15))
            img_left = pygame.transform.flip(img_walk, True, False)
            self.images_walk.append(img_walk)
            self.images_left.append(img_left)
        self.image = self.images_walk[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 50
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jump = False
        self.direction = 0
        self.mid_air = True
        
class World():
    def __init__(self, data):
        self.tile_list = []
        #load images
        dirt = pygame.image.load('tile2.png')
        block = pygame.image.load('tile.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(block, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    ghost = Enemy(col_count * tile_size, row_count * tile_size)
                    ghost_group.add(ghost)
                if tile == 4:
                    gate = Gate(col_count * tile_size, row_count * tile_size)
                    gate_group.add(gate)
                if tile == 5:
                    ghost2 = Enemy2(col_count * tile_size, row_count * tile_size)
                    ghost2_group.add(ghost2)
                if tile == 6:
                    coin = Coin(col_count * tile_size, row_count * tile_size)
                    coin_group.add(coin)
                col_count +=1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])





class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('treasure.png')
        self.image = pygame.transform.scale(img,(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Gate(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('gate2.png')
        self.image = pygame.transform.scale(img, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

menu = False
def menu():
    global loading_background
    menu = True
    while menu:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
            screen.fill((0,0,0))

        if play_button.draw():
            menu = False
            pause = True

        if quit_button.draw():
            pygame.quit()
            quit()

        pygame.display.update()
        clock.tick(60)

end_game = False
def end_game():
    global menu_background, game_over, level
    end_game = True
    while end_game:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()

        screen.blit(end_screen,(0,0))
        if restart_button.draw():
            level = 1
            game_over = 0
            score =0
            map_data = [ ]
            world = reset_level(level)
            end_game = False
            menu()




        pygame.display.update()
        clock.tick(60)



player = Player(30, 50)
coin_group = pygame.sprite.Group()

gate_group = pygame.sprite.Group()

if path.exists(f'levels{level}_data'):
    pickle_in = open(f'levels{level}_data', 'rb')
    map_data = pickle.load(pickle_in)
world = World(map_data)

play_button = Button(screen_width // 2 - 50, screen_height // 2 - 225, play_img)
quit_button = Button(screen_width // 2 - 50, screen_height // 2 - 75, quit_img)
restart_button = Button(screen_width //  2 - 50, screen_height // 2 + 100, restart_image)

menu()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(background,(0,0))
    world.draw()
    if game_over == 0:
        if pygame.sprite.spritecollide(player, coin_group, True):
            score += 1
        display_text('Score:' + str(score), font, white, tile_size - 10, 5)
        
    game_over = player.update(game_over)
    gate_group.draw(screen)

    coin_group.draw(screen)
    if game_over == -1:
        if restart_button.draw():
            player.reset(100, screen_height - 130)
            game_over = 0
            score = 0
    if game_over == 1:
        level += 1
        if level <= max_levels:
            world_data = []
            world = reset_level(level)
            game_over = 0
        else:
            level = 1
            map_data = []
            world = reset_level(level)
            game_over = 0
            score = 0
            end_game()





    pygame.display.update()
    clock.tick(60)


pygame.quit()
