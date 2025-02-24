import pygame


pygame.init() # creates an object of the pygame class to make our window

pygame.display.set_caption('Quick Start') # sets the caption at the top of the window
window_surface = pygame.display.set_mode((800, 600)) # sets the size of the window. theres some other ways to do fullscreen stc but we wont worry abt that now

background = pygame.Surface((800, 600)) # creating a background object o make a black background
background.fill(pygame.Color('#000000'))


# IN PYGAME YOU ALWAYS USE THIS WHILE LOOP STRUCTURE, THIS IS THE CORE SYSTEM OF PYGAME.
# it is what allows us to constantly check for things like clicks and button presses each frame.

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    window_surface.blit(background, (0, 0))

    pygame.display.update()