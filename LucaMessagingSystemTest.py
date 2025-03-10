import pygame
import ui_elements as ui
from pygame.locals import *

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

pygame.init()
pygame.display.set_caption("Chat Test")

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)

messages = []

textbox = ui.InputBox(300, 40, BLUE, "Enter text here...", 40, WHITE)

while True:

    textbox.draw(screen, 0, -0.7)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        inp = textbox.get_text(event)


    pygame.display.update()
