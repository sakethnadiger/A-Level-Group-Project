import pygame
import os
import ui_elements as ui

os.environ['SDL_VIDEO_WINDOW_POS'] = f"{100}, {100}"


RED = pygame.Color("#F94144")
ORANGE = pygame.Color("#F3722C")
LIGHT_ORANGE = pygame.Color("#F8961E")
PEACH = pygame.Color("#F9844A")
YELLOW = pygame.Color("#F9C74F")
GREEN = pygame.Color("#90BE6D")
TURQUOISE = pygame.Color("#43AA8B")
CYAN = pygame.Color("#4D908E")
DARK_GREY = pygame.Color("#5A5A5A")
BLUE = pygame.Color("#277DA1")
BLACK = pygame.Color("#032834")
WHITE = pygame.Color("#FFFFEF")


pygame.init()

pygame.display.set_caption('Chatroom')

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

footer = ui.Label(WIDTH, (HEIGHT//4), DARK_GREY, "", 0, 0)
message_input = ui.InputBox(WIDTH*0.75, 0.5*(HEIGHT//8), BLACK, "", 40, PEACH)

is_running = True
fullscreen = False


messages = []

while is_running:
    
    
    #DRAW OBJECTS HERE
    screen.fill(BLACK)
    footer.draw(screen, 0, -1)
    message_input.draw(screen, 0, ui.pin_y(-1, (HEIGHT//16)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    WIDTH = pygame.display.get_window_size()[0]
                    HEIGHT = pygame.display.get_window_size()[1]
                    
                else:
                    pygame.display.quit()
                    pygame.display.init()
                    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
                    WIDTH = 800
                    HEIGHT = 600
    
        message_input.update(event)
    
    pygame.display.update()

