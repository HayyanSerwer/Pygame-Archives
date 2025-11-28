import pygame # pygame useful for making games in python, enables a much easier UI for the game
import os # needed for python file launching
import sys # used for quitting
from pygame.color import Color # colour module, makes defining colours quicker

pygame.font.init() # initialising
font = pygame.font.Font('OpenSans-Regular.ttf', 30) # importing the font file       
blue   = (Color('blue')) # Using the pygame.color module - 
gray = (Color('gray')) # This means I do not have to use hex or RGB codes

window_width = 800
window_height = 950
display = pygame.display.set_mode((window_width , window_height))
background = Color('Blue')
rules_text1 = ("test test test")

def draw_button(text_bar, box, base_colour, hover_colour, user):

    font = pygame.font.Font(None, 40)

    button_box = pygame.Rect(box)

    text_bar = font.render(text_bar, True, Color('White'))
    text_box = text_bar.get_rect(center=button_box.center)

    return [text_bar, text_box, button_box, base_colour, hover_colour, user, False]


def check(data, event):

    text_bar, text_box, box, base_colour, hover_colour, user, hover = data

    if event.type == pygame.MOUSEMOTION:
        # hover = True/False   
        data[-1] = box.collidepoint(event.pos)

    elif event.type == pygame.MOUSEBUTTONDOWN:
        if hover and user:      
            user()


def button_draw(display, data):

    text_bar, text_box, box, base_colour, hover_colour, user, hover = data

    if hover:
        color = hover_colour
    else:
        color = base_colour

    pygame.draw.rect(display, color, box)
    display.blit(text_bar, text_box)

def b1_clicked():
  global level
  level = 'exit'

def b2_clicked():
  global level
  level = 'rules'

def b3_clicked():
  global level
  global running
  level = 'game'

def b4_clicked():
  global level
  level = 'mg' #mg = memory game

def return_button():
    global level
    level = 'menu'

level = 'menu'

b1 = draw_button("Exit", (300, 475, 200, 75), blue, gray, b1_clicked)
b2 = draw_button("Rules", (300, 75, 200, 75),  blue, gray, b2_clicked)
b3 = draw_button("Launch Response Time Test Game", (160, 175, 500, 120), blue, gray, b3_clicked)
b4 = draw_button("Launch Memory Game", (160, 325, 500, 120), blue, gray, b4_clicked)

return_button = draw_button("Return to menu", (269, 400, 250, 100), blue, gray, return_button)

running = True
textsurface = font.render(rules_text1, False, Color('White'))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if level == 'menu':
            check(b1, event)
            check(b2, event)
            check(b3, event)
            check(b4, event)
        elif level == 'exit':
            check(return_button, event)
        elif level == 'rules':
            check(return_button, event)

    display.fill(Color('Black'))

    if level == 'menu':
        button_draw(display, b1)
        button_draw(display, b2)
        button_draw(display, b3)
        button_draw(display, b4)
    elif level == 'exit':
        sys.exit("User chose quit")
    elif level == 'rules':
        button_draw(display, return_button)
        display.blit(textsurface,(300,300))
    elif level == 'game':
        os.system('python rtt.py')
    elif level == 'mg':
        os.system('python memory.py')

    pygame.display.update()