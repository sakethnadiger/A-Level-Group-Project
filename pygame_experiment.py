import pygame


pygame.init() # creates an object of the pygame class to make our window

pygame.display.set_caption('Quick Start') # sets the caption at the top of the window
window_surface = pygame.display.set_mode((800, 600)) # sets the size of the window. theres some other ways to do fullscreen stc but we wont worry abt that now

background = pygame.Surface((800, 600)) # creating a background object o make a black background
background.fill(pygame.Color('#FF0000'))


BLUE = (0, 255, 255)

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

    window_surface.blit(background, (0, 0))
    pygame.draw.rect(window_surface, BLUE, (10, 10, 50, 50))

    pygame.display.update()