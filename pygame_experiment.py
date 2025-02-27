import pygame
import ui_elements as ui
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

clicked = True

def clicked_colour():
    print("there")
    clicked = True
    return True        
def Rainbow_Button():
    pygame.draw.rect(screen, ("#FF0000"), (10, 10, 7, 50))
    pygame.draw.rect(screen, ("#FFA500"), (17, 10, 7, 50))
    pygame.draw.rect(screen, ("#FFFF00"), (24, 10, 7, 50))
    pygame.draw.rect(screen, ("#008000"), (31, 10, 7, 50))
    pygame.draw.rect(screen, ("#0000FF"), (38, 10, 7, 50))
    pygame.draw.rect(screen, ("#4B0082"), (45, 10, 7, 50))
    pygame.draw.rect(screen, ("#EE82EE"), (52, 10, 7, 50))

def Colour_Palette():
    print("boop")
    pygame.draw.rect(screen, RED, (10, 10, 50, 50))
    pygame.draw.rect(screen, ORANGE, (60, 10, 50, 50))
    pygame.draw.rect(screen, LIGHT_ORANGE, (110, 10, 50, 50))
    pygame.draw.rect(screen, PEACH, (160, 10, 50, 50))
    pygame.draw.rect(screen, YELLOW, (210, 10, 50, 50))
    pygame.draw.rect(screen, GREEN, (260, 10, 50, 50))
    pygame.draw.rect(screen, TURQUOISE, (310, 10, 50, 50))
    pygame.draw.rect(screen, CYAN, (360, 10, 50, 50))
    pygame.draw.rect(screen, DARK_GREY, (410, 10, 50, 50))
    pygame.draw.rect(screen, BLUE, (460, 10, 50, 50))
    pygame.draw.rect(screen, BLACK, (510, 10, 50, 50))
    pygame.draw.rect(screen, WHITE, (560, 10, 50, 50))

        

pygame.init() # creates an object of the pygame class to make our window

pygame.display.set_caption('Quick Start') # sets the caption at the top of the window
screen = pygame.display.set_mode((800, 600)) # sets the size of the window. theres some other ways to do fullscreen stc but we wont worry abt that now

background = pygame.Surface((800, 600)) # creating a background object o make a black background
background.fill(WHITE)

# creating an instance of one of the ui elements i have made. a label is a thing that displays text
yashtext = ui.Label(220, 50, BLUE, "yash bash cash", 40, 0)

#just testing the button with a dummy variable
def foo():
    print("CLICKED")
test = ui.Button(400, 100, 0, "test button", 100, (255, 255, 255))
reset_test = ui.Button(300, 50, 0, "reset test button", 50, (255, 255, 255))
colours = ui.Button(49, 50, 0, "text", 10 , (WHITE))

# IN PYGAME YOU ALWAYS USE THIS WHILE LOOP STRUCTURE, THIS IS THE CORE SYSTEM OF PYGAME.
# it is what allows us to constantly check for things like clicks and button presses each frame.

is_running = True

while is_running:
    # this basically handles all the events that happen. key presses, mouse position, everything. the variable event contains all of these events. there are a lot you can have a look at a list online.
    for event in pygame.event.get():
        # event.type helps us identify which event it is specifically to target something like a mouse press.
        if event.type == pygame.QUIT:
            # checking if they press the x button on the window and closing if it happens
            is_running = False

        screen.blit(background, (0, 0))
        colours.draw(screen, 10, 10)
        #clicked = colours.is_clicked(clicked_colour)
        Rainbow_Button()
        if clicked == True:
            print("heloooooo")
            Colour_Palette()

        # drawing the label that we defined earlier
        yashtext.draw(screen, 500, 500)
        test.draw(screen, 300, 200)
        reset_test.draw(screen, 300, 350)
        test.is_clicked(foo)
        reset_test.is_clicked(test.reset)
        reset_test.reset()
    pygame.display.update()
        
