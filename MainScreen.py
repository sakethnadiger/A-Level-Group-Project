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

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
footer = ui.Label(WIDTH*3, (HEIGHT//4), BLACK, "", 0, 0)
title = ui.Bubble(WHITE, "AWESOME TEXT MESSAGING", 50, CYAN)
startbutton = ui.Button(400, 60, BLACK, "Start Chatting!", 60, CYAN)


clock = pygame.time.Clock()

while True:

    screen.fill(WHITE)
    footer.draw(screen, 0, -1)
    title.draw(screen, 0, 0.90)
    startbutton.draw(screen, 0, 0.5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if startbutton.is_clicked(event, startchatting):
        chatting = True
        import chat_screen
        pygame.quit()
        break    

    pygame.display.update()
    clock.tick(60)