import pygame
import os
import ui_elements as ui

#Helps reset window settings to previous state
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{100}, {100}"

# ui_elements refers to the python file in the same folder. this is basically our own homemade library of classes of ui elements that we have made. see that file for more info.
#BTW I HAVE SHORTENED THE UI LIBRARY NAME TO JUST "UI" - WILL SPEED UP DEVELOPMENT
RED = pygame.Color("#F94144")
ORANGE = pygame.Color("#F3722C")
LIGHT_ORANGE = pygame.Color("#F8961E")
PEACH = pygame.Color("#F9844A")
YELLOW = pygame.Color("#F9C74F")
GREEN = pygame.Color("#90BE6D")
TURQUOISE = pygame.Color("#43AA8B")
CYAN = pygame.Color("#4D908E")
DARK_GREY = pygame.Color("#577590")
BLUE = pygame.Color("#277DA1")
BLACK = pygame.Color("#032834")
WHITE = pygame.Color("#FFFFEF")

global clicked
clicked = False

def clicked_colour():
    global clicked
    if clicked == False:
        clicked = True
    else:
        clicked = False
    colours.reset()
def Rainbow_Button():
    red.draw(screen, ui.convert_coords_back((ui.convert_coords(-0.9,3)[0])-21,3)[0], 0.9)
    orange.draw(screen, ui.convert_coords_back((ui.convert_coords(-0.9,3)[0])-14,3)[0], 0.9)
    yellow.draw(screen, ui.convert_coords_back((ui.convert_coords(-0.9,3)[0])-7,3)[0], 0.9)
    green.draw(screen, ui.convert_coords_back((ui.convert_coords(-0.9,3)[0]),3)[0], 0.9)
    blue.draw(screen, ui.convert_coords_back((ui.convert_coords(-0.9,3)[0])+7,3)[0], 0.9)
    indigo.draw(screen, ui.convert_coords_back((ui.convert_coords(-0.9,3)[0])+14,3)[0], 0.9)
    violet.draw(screen, ui.convert_coords_back((ui.convert_coords(-0.9,3)[0])+21,3)[0], 0.9)  
    rainbow_text.draw(screen, ui.convert_coords_back((ui.convert_coords(-0.9,3)[0]) +22,3)[0], ui.convert_coords_back(3,((ui.convert_coords(3,0.9)[1])+30))[1])

def Colour_Palette():
    pygame.draw.rect(screen, RED, (130, 10, 50, 50))
    pygame.draw.rect(screen, ORANGE, (180, 10, 50, 50))
    pygame.draw.rect(screen, LIGHT_ORANGE, (230, 10, 50, 50))
    pygame.draw.rect(screen, PEACH, (280, 10, 50, 50))
    pygame.draw.rect(screen, YELLOW, (330, 10, 50, 50))
    pygame.draw.rect(screen, GREEN, (380, 10, 50, 50))
    pygame.draw.rect(screen, TURQUOISE, (430, 10, 50, 50))
    pygame.draw.rect(screen, CYAN, (480, 10, 50, 50))
    pygame.draw.rect(screen, DARK_GREY, (530, 10, 50, 50))
    pygame.draw.rect(screen, BLUE, (580, 10, 50, 50))
    pygame.draw.rect(screen, BLACK, (630, 10, 50, 50))
    pygame.draw.rect(screen, WHITE, (680, 10, 50, 50))
    COLOUR_text.draw(screen, 0,0.7)

pygame.init() # creates an object of the pygame class to make our window

pygame.display.set_caption('Chatroom') # sets the caption at the top of the window

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)# --> fullscreen has now been implemented



#just testing the button with a dummy variable
def foo():
    print("CLICKED")
test = ui.Button(500, 100, BLACK, "test button", 125, WHITE)
reset_test = ui.Button(200, 40, BLACK, "reset button", 40, WHITE)
logo = ui.Label(100, 60, WHITE, "designed by saketh, harvey, yash and luca.", 25, BLACK)
textbox = ui.InputBox(300, 40, LIGHT_ORANGE, "Enter text here...", 40, WHITE)

colours = ui.Button(48, 50, 0, "", 10 , (WHITE))
rainbow_text = ui.Label(0, 0, YELLOW, "Show colour palette", 14, 0)
COLOUR_text = ui.Label(0, 0, YELLOW, "Red              Orange     Light Orange       Peach             Yellow             Green          Turquoise           Cyan           Dark Grey           Blue                Black             White", 13, 0)
red = ui.Label(8, 50, "#E81416", "", 14, 0)
orange = ui.Label(8, 50, "#FFA500", "", 14, 0)
yellow = ui.Label(8, 50, "#FAEB36", "", 14, 0)
green = ui.Label(8, 50, "#79C314", "", 14, 0)
blue = ui.Label(8, 50, "#487DE7", "", 14, 0)
indigo = ui.Label(8, 50, "#4B369D", "", 14, 0)
violet = ui.Label(8, 50, "#70369d", "", 14, 0)
# IN PYGAME YOU ALWAYS USE THIS WHILE LOOP STRUCTURE, THIS IS THE CORE SYSTEM OF PYGAME.
# it is what allows us to constantly check for things like clicks and button presses each frame.

is_running = True
fullscreen = False

while is_running:
  
    # DRAW OBJECTS FIRST
    screen.fill(WHITE)
    test.draw(screen, 0, 0)
    reset_test.draw(screen, 0, -0.4)
    textbox.draw(screen, 0, -0.7)
    logo.draw(screen, 0.55, -0.95)
    reset_test.reset()
    
    colours.draw(screen, -0.9, 0.9)
    Rainbow_Button()
    if clicked == True:
        Colour_Palette()
        
    # EVENT CHECK AFTER DRAWING ALL OBJECTS

    # this basically handles all the events that happen. key presses, mouse position, everything. the variable event contains all of these events. there are a lot you can have a look at a list online.
    for event in pygame.event.get():
        # event.type helps us identify which event it is specifically to target something like a mouse press.
        if event.type == pygame.QUIT:
            # checking if they press the x button on the window and closing if it happens
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    WIDTH = pygame.display.get_window_size()[0]
                    HEIGHT = pygame.display.get_window_size()[1]
                    
                else:
                    #Following two lines help reset window size to previous state also
                    pygame.display.quit()
                    pygame.display.init()
                    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
                    WIDTH = 800
                    HEIGHT = 600
        colours.is_clicked(event, clicked_colour)
        test.is_clicked(event, foo)
        reset_test.is_clicked(event, test.reset)
        textbox.update(event)
    
    
    # DON'T DRAW ANYTHING HERE IM LOOKING AT YOU HARVEY
    
    
    pygame.display.update()

