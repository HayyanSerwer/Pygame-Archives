# import modules
import pygame # pygame useful for making games in python, enables a much easier UI for the game
import random # module for generating pseudorandom numbers
from itertools import product # itertools is used for efficient function looping
from pygame.locals import * # subset of pygame, saves typing later on
from pygame.color import Color


pygame.init()

clock = pygame.time.Clock()
white = [0,0,0]
# initialisation
window_width = 800 # size of window's width in pixels
window_height = 700 # size of window's height in pixels
box_size = 50 # size of card boxes
box_gap = 25 # size of gap between cards boxes
board_x = 2 # number of cards across
board_y = 2 # number of cards down
margin_x = (window_width - (board_x * (box_size + box_gap))) // 2
margin_y = (window_height - (board_x * (box_size + box_gap))) // 2
# because the game is in pairs, the board size must be even
assert (board_y * board_x) % 2 == 0 # must be even due to cards being in pairs, otherwise game will be impossible to complete # assert = test if true

# the shapes
shape_one = 'diamond' 
shape_two = 'square'
shape_three = 'triangle'
shape_four = 'circle'

background = Color('Blue') #  background colour
text = "Press P to continue"
text2 = "Press Q to quit"
font = pygame.font.Font("OpenSans-Regular.ttf", 32)
paused = False

def display_text(str, location): #a functin that is used to make displaying texts easier, this function is not really required but it makes displaying text easier
    # Assign text contents and position
    words = font.render(str, True, Color('white')) #renders the words from the font mentioned above
    ss_text = words
    rt_text = words.get_rect()
    rt_text.x = location[0]
    rt_text.y = location[1]
    
    # Draw to screen at specified position
    display.blit(ss_text, rt_text)
    
def pause():
    paused = True

    while paused:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN: #if a key gets pressed down
                if event.key == pygame.K_p: #if p gets pressed down
                    paused = False #pause gets disabled 
                elif event.key == pygame.K_q: #if q gets pressed down
                    pygame.quit() #quits the game
                    quit()
        display_text("Press P to continue",[250,100]) #displays "Press P to continue" when the paused function is called   
        display_text("Press Q to quit",[250,50])#displays "Press Q to quit" when the paused function is called



        pygame.display.update()
        clock.tick(5)#Basically the fps of the game (You can change it to your liking doesn't really matter since the game is paused

# defining the function to draw the entire board
def create_board(board, all_cards_uncovered): #this is just a function that creates one of the boards in the memory game
    for x in range(board_y): #later this has been placed in a loop which creates multiple boards.
        for y in range(board_x):
            create_square(board, all_cards_uncovered, x, y)
 
#  defining the function for resetting the shapes at the end of the game
def game_success(all_cards_uncovered): # = cards revealed
    return all(all(x) for x in all_cards_uncovered) # returns true only if all items are true, in this case if all cards are uncovered, then the shapes are reset

# function for the animation at the start
def shuffle_animation(board): # to cycle showing 5 random shapes at the start
    position = list(product(range(board_y), range(board_x))) # takes the board size values (from itertools), uses cartesian like coordinate system (product)
    random.shuffle(position) # takes the sequence, in this case ~positions list~ and reorganises the order, therefore appearing to shuffle the cards/shapes

    all_cards_uncovered = [[False] * board_x for i in range(board_y)]

    display.fill(background) # fills entire screen with given colour, in this case blue was defined earlier
    create_board(board, all_cards_uncovered) 
    pygame.display.update() # updates only a portion of the screen as once, as opposed to display.flip which would update the entire screen. This means the update is instead generally faster and more efficient.
    pygame.time.wait(500) # pauses the program for a set amount of time. 1 = 1ms, 500 = 500ms = 5 secs

    for e in range(0, board_y * board_x, 5):
        l = position[e: e + 5]
        for x in l:
            all_cards_uncovered[x[0]][x[1]] = True
            create_square(board, all_cards_uncovered, *x)
        pygame.time.wait(500)
        for x in l:
            all_cards_uncovered[x[0]][x[1]] = False
            create_square(board, all_cards_uncovered, *x)

# defining the function for the animation after the game is won successfully
def game_success_animation(board, all_cards_uncovered):
    colour_one = Color('white') # white
    colour_two = background # blue
    for i in range(10): # flashes 10 times total, 5 each colour
        colour_one, colour_two = colour_two, colour_one # alternates the flashes
        display.fill(colour_one) # fill screen in with white at the end
        create_board(board, all_cards_uncovered) # keeps the shapes on screen
        pygame.display.update() # updates the display
        pygame.time.wait(300) # waits before resuming the game to allow for shuffling and animations to complete before the user can continue

# defining the function for setting up the board
def create_new_board(shape, colours): # creates random shapes with random shape colours

    generated = list(product(shape, colours)) # stores the random shape and colours in generated variable, uses random 'cartesian' system for generation.
    num_generated = board_y * board_x // 2 # in this example if height = 4 and width = 8, 4 * 8 = 32 // 2 is 16. // Is a logical operator - floor division - rounds the result down to the nearest whole number
    generated = generated[:num_generated] * 2 # num_generated in the array, makes sure the number of cards generated equals the number of spaces in the grid. Following the example from above, it generates 32 shapes with colours, divides it by 2 (will always be even due to forced even numbers) and duplicates the 16 into 32. This creates pairs.

    random.shuffle(generated) # randomly reorders the cards order
    board = [generated[i:i + board_x]
             for i in range(0, board_y * board_x, board_x)]
    return board
    # spits out the board


def fetch_coordinates(x, y): #this gets co-ordinates for  tje cards
    t = margin_x + y * (box_size + box_gap)
    l = margin_y + x * (box_size + box_gap)
    return t, l


def create_cards(card, x, y):
    xx, yy = fetch_coordinates(x, y)
    if card[0] == shape_one: # if card generated is a diamond
        pygame.draw.polygon(display, card[1], # calculations to make a diamond shape
                            ((xx + box_size // 2, yy + 5), (xx + box_size - 5, yy + box_size // 2),
                             (xx + box_size // 2, yy + box_size - 5), (xx + 5, yy + box_size // 2)))
    elif card[0] == shape_two: # if card generated is a square
        pygame.draw.rect(display, card[1], # calculations to make a square shape
                         (xx + 5, yy + 5, box_size - 10, box_size - 10))
    elif card[0] == shape_three: # if card generated is a triangle
        pygame.draw.polygon(display, card[1], # calculations to make a triangle shape
                            ((xx + box_size // 2, yy + 5), (xx + 5, yy + box_size - 5),
                             (xx + box_size - 5, yy + box_size - 5)))
    elif card[0] == shape_four: # if card generated is a circle
        pygame.draw.circle(display, card[1], # calculations to make a circle shape
                           (xx + box_size // 2, yy + box_size // 2), box_size // 2 - 5)


def get_pos(coord_x, coord_y): # Gets the position(x and y coordinates)
    if coord_x < margin_x or coord_y < margin_y:
        return 0, 0

    x = (coord_y - margin_y) // (box_size + box_gap)
    y = (coord_x - margin_x) // (box_size + box_gap)

    if x >= board_y or y >= board_x or(coord_x - margin_x) % (box_size + box_gap) > box_size or (coord_y - margin_y) % (box_size + box_gap) > box_size:
        return 0, 0
    else:
        return x, y

def create_square(board, all_cards_uncovered, x, y): #a function defined to create a squard onto the board
    cdns = fetch_coordinates(x, y) 
    white_square = (*cdns, box_size, box_size)
    pygame.draw.rect(display, background, white_square) #draws the rect(white square) onto the display
    if all_cards_uncovered[x][y]:
        create_cards(board[x][y], x, y)
    else:
        pygame.draw.rect(display, Color('white'), white_square)
    pygame.display.update(white_square)



# defining the function used to highlight the square when hovered over
def hover_outline(x, y):
    xx, yy = fetch_coordinates(x, y)
    pygame.draw.rect(display, Color('green'), (xx - 5, yy - 5, box_size + 10, box_size + 10), 5)


# the main function
def main():
    global display #globals the local variable display so it can be used whenever you want to

    pygame.init()

    display = pygame.display.set_mode((window_width , window_height))

    shape = (shape_one, shape_two, shape_three, shape_four)
    colours = (Color('orange'), Color('purple'), Color('pink'), Color('red'))

    board = create_new_board(shape, colours)
    all_cards_uncovered = [[False] * board_x for i in range(board_y)]  # keeps track of visibility of square

    x_mouse = None #x-co-ordinates of the mouse
    y_mouse = None#y co-ordinates of the mouse
    pressed_mouse = False
    n = None

    active = True
    shuffle_animation(board) #enables the shuffle animation from the function defined above

    while active:
        display.fill(background) #background gets displayed onto the canvas
        create_board(board, all_cards_uncovered)

        for event in pygame.event.get(): #gets a pygame event
            if event.type == pygame.QUIT:#the event that it got is quit
                active = False#active turns into false which means the game is not active once the game has been quit
            elif event.type == MOUSEMOTION: #detects mouse motion
                x_mouse, y_mouse = pygame.mouse.get_pos() #x and y coordinates  of the mouse
            elif event.type == MOUSEBUTTONDOWN: #if any of the mouse buttons get pressed
                x_mouse, y_mouse = pygame.mouse.get_pos() #get the x and y coordinates of the mouse
                pressed_mouse = True
            if event.type == pygame.KEYDOWN: #if a key is pressed down
                if event.key == pygame.K_p:#if p is pressed down
                    pause() #pause the game (pause function has been defined above)

        x, y = get_pos(x_mouse, y_mouse)

        if x is not None and y is not None:
            if not all_cards_uncovered[x][y]:
                if pressed_mouse:
                    all_cards_uncovered[x][y] = True
                    create_square(board, all_cards_uncovered, x, y)

                    if n is None:
                        n = (x, y)
                    else:
                        pygame.time.wait(1000)
                        if board[x][y] != board[n[0]][n[1]]:
                            all_cards_uncovered[x][y] = False
                            all_cards_uncovered[n[0]][n[1]] = False
                        n = None

                    if game_success(all_cards_uncovered):

                        game_success_animation(board, all_cards_uncovered)

                        board = create_new_board(shape, colours)
                        all_cards_uncovered = [[False] * board_x for i in range(board_y)]
                        game_success(board)

                else:
                    hover_outline(x, y)

        pressed_mouse = False 
        pygame.display.update() # updates the pygame canvas

    else:
       pygame.quit()
       quit()
       

if __name__ == '__main__':
    main()
