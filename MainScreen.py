import pygame
import ui_elements as ui
import os

pygame.init()
pygame.display.set_caption("Main Menu")

WIDTH = 800
HEIGHT = 600

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

def startchatting():
    print("Chatting start!")
    return True

def settingsmenu():
    print("Time to change settings")
    return True

def settingscolourchange():
    print("Changing colour to red")
    return True

def quitchatting():
    print("Quitting")
    return True

# Main Section
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
footer = ui.Label(WIDTH*3, (HEIGHT//4), BLACK, "", 0, 0)
title = ui.Bubble(WHITE, "AWESOME TEXT MESSAGING", 50, CYAN)
startbutton = ui.Button(400, 60, BLACK, "Start Chatting!", 60, CYAN)
optionsbutton = ui.Button(400, 60, BLACK, "Options", 60, CYAN)
quitbutton = ui.Button(400, 60, BLACK, "Quit", 60, CYAN)

# Settings Section
settingstitle = ui.Bubble(WHITE, "AWESOME SETTINGS MENU", 60, CYAN)
settingscolour = ui.Button(400, 60, BLACK, "Change Colour", 60, CYAN)


settings = False
clock = pygame.time.Clock()
bgcolour = WHITE

while True:

    screen.fill(bgcolour)
    footer.draw(screen, 0, -1)
    
    if not settings:
        title.draw(screen, 0, ui.pin_y(1, -30))
        startbutton.draw(screen, 0, ui.pin_y(0.5, -10))
        optionsbutton.draw(screen, 0, ui.pin_y(0.5, -100))
        quitbutton.draw(screen, 0, ui.pin_y(0.5, -200))
        pygame.display.update()

    if settings:
        settingstitle.draw(screen, 0, ui.pin_y(1, -30))
        settingscolour.draw(screen, 0, ui.pin_y(0.5, -10))
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # if startbutton.is_clicked(event, startchatting):
    #     chatting = True
    #     import chat_screen
    #     startbutton.reset()
    #     pygame.quit()
    
    if optionsbutton.is_clicked(event, settingsmenu):
        settings = True
        optionsbutton.reset()
    
    if quitbutton.is_clicked(event, quitchatting):
        pygame.quit()

    if settingscolour.is_clicked(event, settingscolourchange):
        bgcolour = RED

    pygame.display.update()
    clock.tick(60)