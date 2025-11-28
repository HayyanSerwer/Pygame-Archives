import pygame
import constants
import pickle
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

#defining variables
grey = [50,50,50]
bg_color = [0,0,0]
white = [255,255,255]
blue = [0,0, 205]
black = [0,0,0]
player1_color = [255,255,255]
player2_color = [255,255,255]
circle_color = [255,255,255]
text_color = [255,255,255]

menu_title_img = pygame.image.load('menu_title.png')
play_img = pygame.image.load('play.png')
quit_img = pygame.image.load('quit.png')

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Fiver')

background = pygame.image.load("background_01.jpg")#change this if you want to change the GAME background TO something else
tile_size = 40

menu_background = pygame.image.load("background2.jpg")#change this if you want to change the MENU background to something else

level = 1
max_levels = 4
restart_image = pygame.image.load('restart2.png')

game_over = 0

#used to create a button(play, quit etc)
class Button():
    def __init__(self, x ,y ,image):
        self.image = image #Gets the image
        self.rect = self.image.get_rect()#Creates a rect for the image so a user can interact with it
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

#Importing the buttons using the buttons function (pictures have already been imported)
menu_title_button = Button(screen_width // 2 - 350, screen_height // 2 - 300, menu_title_img)
play_button = Button(screen_width // 2 - 250, screen_height // 2 - 150, play_img)
quit_button = Button(screen_width // 2 - 250, screen_height // 2 , quit_img)



def display_text(text, font, text_col, x, y):
    img =  font.render(text, True, text_col)
    screen.blit(img, (x,y))

#Main game loop(Try not to change anything)
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

        if menu_title_button.draw():
            print('Bajan Bus stop')
        if play_button.draw():
            menu = False
            pause = True
        if quit_button.draw():
            pygame.quit()
            quit()

        pygame.display.update()
        clock.tick(60)

end_game = False
def end_game():#End game screen
    global menu_background
    end_game = True
    while end_game:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()

        screen.blit(menu_background,(0,0))

        if play_button.draw():
            menu = False
            pause = True
            menu_background = pygame.image.load("loading_screen.png")
            board()



        pygame.display.update()
        clock.tick(60)


def reset_level(level):
    player.reset(100, screen_height - 130)
    ghost_group.empty()
    ghost2_group.empty()
    gate_group.empty()
    coin_group.empty()
    coin3_group.empty()
    coin4_group.empty()
    coin5_group.empty()
    if path.exists(f'level{level}_data'):
        pickle_in = open(f'level{level}_data', 'rb')
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



class Player():
    def __init__(self,x,y):
        self.reset(x,y)

    def update(self, game_over):
        dx = 0
        dy = 0
        walk_cooldown = 5
        if game_over == 0:
            key = pygame.key.get_pressed()
            if key[pygame.K_UP] and self.jump == False and self.mid_air == False:
                self.vel_y = -15
                self.jump = True
            if key[pygame.K_UP] == False:
                self.jump = False
                
                
            if key[pygame.K_LEFT] or key[pygame.K_a]:
                self.counter += 1
                dx -= 5
                self.direction = -1
            if key[pygame.K_RIGHT] or key[pygame.K_d]:
                self.counter += 1
                self.direction = 1
                dx += 5

            if key[pygame.K_LEFT] == False  and key[pygame.K_RIGHT] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_walk[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]


            
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_walk):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_walk[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]
                

            self.vel_y += 1
            if self.vel_y > 15:
                self.vel_y = 15
            dy += self.vel_y
            
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

            if pygame.sprite.spritecollide(self, ghost_group, False):
                game_over = -1
                print(game_over)
            if pygame.sprite.spritecollide(self, ghost2_group, False):
                game_over = -1
                print(game_over)
            if pygame.sprite.spritecollide(self,gate_group, False):
                game_over = 1


                    
            self.rect.x += dx
            self.rect.y += dy

        screen.blit(self.image, self.rect)
        return game_over

    def reset(self,x,y):
        global coin_group, img_walk
        self.images_walk = []
        self.images_left = []
        self.index = 0
        self.counter = 0

        for num in range(50,60):
            img_walk = pygame.image.load(f'colors/player{num}.png')
            img_walk = pygame.transform.scale(img_walk,(40,80))
            img_left = pygame.transform.flip(img_walk, True, False)
            self.images_walk.append(img_walk)
            self.images_left.append(img_left)   
     
        self.image = self.images_walk[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jump = False
        self.direction = 0
        self.mid_air = True
    def reset1(self,x,y):
        global coin_group, img_walk
        self.images_walk = []
        self.images_left = []
        self.index = 0
        self.counter = 0

        for num in range(11,19):
            img_walk = pygame.image.load(f'colors/player{num}.png')
            img_walk = pygame.transform.scale(img_walk,(40,80))
            img_left = pygame.transform.flip(img_walk, True, False)
            self.images_walk.append(img_walk)
            self.images_left.append(img_left)   
     
        self.image = self.images_walk[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jump = False
        self.direction = 0
        self.mid_air = True
    def reset2(self,x,y):
        global coin_group, img_walk
        self.images_walk = []
        self.images_left = []
        self.index = 0
        self.counter = 0

        for num in range(23,30):
            img_walk = pygame.image.load(f'colors/player{num}.png')
            img_walk = pygame.transform.scale(img_walk,(40,80))
            img_left = pygame.transform.flip(img_walk, True, False)
            self.images_walk.append(img_walk)
            self.images_left.append(img_left)   

        self.image = self.images_walk[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jump = False
        self.direction = 0
        self.mid_air = True
    def reset3(self,x,y):
        global coin_group, img_walk
        self.images_walk = []
        self.images_left = []
        self.index = 0
        self.counter = 0

        for num in range(41,49):
            img_walk = pygame.image.load(f'colors/player{num}.png')
            img_walk = pygame.transform.scale(img_walk,(40,80))
            img_left = pygame.transform.flip(img_walk, True, False)
            self.images_walk.append(img_walk)
            self.images_left.append(img_left)   

        self.image = self.images_walk[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jump = False
        self.direction = 0
        self.mid_air = True
    def reset4(self,x,y):
        global coin_group, img_walk
        self.images_walk = []
        self.images_left = []
        self.index = 0
        self.counter = 0

        for num in range(1,11):
            img_walk = pygame.image.load(f'colors/player{num}.png')
            img_walk = pygame.transform.scale(img_walk,(40,80))
            img_left = pygame.transform.flip(img_walk, True, False)
            self.images_walk.append(img_walk)
            self.images_left.append(img_left)   

        self.image = self.images_walk[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
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
                    coin5 = Coin5(col_count * tile_size, row_count * tile_size)
                    coin5_group.add(coin5)
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
                if tile == 7:
                    coin3 = Coin3(col_count * tile_size, row_count * tile_size)
                    coin3_group.add(coin3)
                if tile == 8:
                    coin4 = Coin4(col_count * tile_size, row_count * tile_size)
                    coin4_group.add(coin4)


                col_count +=1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])



class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bus.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y + 5
        self.move_direction = 2
        self.move_counter = 0
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if self.move_counter > 130:
            self.move_direction *= -1
            self.move_counter *= 0

class Enemy2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bus.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y + 5
        self.move_direction = 2
        self.move_counter = 0
    def update(self):
        self.rect.x -= self.move_direction
        self.move_counter += 1
        if self.move_counter > 100:
            self.move_direction *= -1
            self.move_counter *= 0

class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('coin2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin3(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('coin3.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin4(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('coin4.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin5(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('coin5.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Gate(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('gate2.png')
        self.image = pygame.transform.scale(img, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 10


ghost_group = pygame.sprite.Group()
ghost2_group = pygame.sprite.Group()

player = Player(100, screen_height - 130)
coin_group = pygame.sprite.Group()
coin3_group = pygame.sprite.Group()
coin4_group = pygame.sprite.Group()
coin5_group = pygame.sprite.Group()

gate_group = pygame.sprite.Group()

if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')
    map_data = pickle.load(pickle_in)
world = World(map_data)


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
        ghost_group.update()
        ghost2_group.update()

    if pygame.sprite.spritecollide(player, coin_group, True):
        Player.reset3(player, player.rect.x, player.rect.y)
    if pygame.sprite.spritecollide(player, coin3_group, True):
        Player.reset1(player, player.rect.x, player.rect.y)
    if pygame.sprite.spritecollide(player, coin4_group, True):
        Player.reset2(player, player.rect.x, player.rect.y)
    if pygame.sprite.spritecollide(player, coin5_group, True):
        Player.reset4(player, player.rect.x, player.rect.y)
        
    ghost_group.draw(screen)
    game_over = player.update(game_over)
    gate_group.draw(screen)
    ghost2_group.draw(screen)
    coin_group.draw(screen)
    coin3_group.draw(screen)
    coin4_group.draw(screen)
    coin5_group.draw(screen)
    if game_over == -1:
        if restart_button.draw():
            map_data = []
            world = reset_level(level)
            game_over = 0
            
    if game_over == 1:
        level += 1
        if level <= max_levels:
            map_data = []
            world = reset_level(level)
            game_over = 0

        else:
            if restart_button.draw():
                level = 1
                map_data = []
                world = reset_level(level)
                game_over = 0
                score = 0

    if level == 5:
        display_text('YOU WON', winning_font, white, 300,250)

    gate_group.draw(screen)
    pygame.display.update()
    clock.tick(60)


pygame.quit()
