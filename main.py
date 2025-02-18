print("This code is from a branch")
import pygame
from pygame.locals import *

pygame.init()

print("Hello World")

HEIGHT = 400
WIDTH = 400

window = pygame.display.set_mode((HEIGHT, WIDTH))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
    pygame.display.update()
