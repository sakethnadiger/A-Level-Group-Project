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



def colour_palette():
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

pygame.display.set_caption('a_message') # sets the caption at the top of the window

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT)) # sets the size of the window. theres some other ways to do fullscreen stc but we wont worry abt that now



background = pygame.Surface((WIDTH, HEIGHT)) # creating a background object to make a black background
background.fill(WHITE)



#just testing the button with a dummy variable
def foo():
    print("CLICKED")
test = ui.Button(500, 100, BLACK, "test button", 125, WHITE)
reset_test = ui.Button(200, 40, BLACK, "reset button", 40, WHITE)
logo = ui.Label(100, 60, WHITE, "designed by saketh, harvey, yash and luca.", 25, BLACK)

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
    colour_palette()

    # drawing the label that we defined earlier
    logo.draw(screen, 0.55, -0.95)
    test.draw(screen, 0, 0)
    reset_test.draw(screen, 0, -0.4)
    test.is_clicked(foo)
    reset_test.is_clicked(test.reset)
    reset_test.reset()
    
    
    
    pygame.display.update()
    
