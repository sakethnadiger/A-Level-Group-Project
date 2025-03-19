import pygame
import ui_elements as ui
import os

pygame.init()
pygame.display.set_caption("Main Menu")

WIDTH = 800
HEIGHT = 600

def startchatting():
    print("Chatting start!")
    return True

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
footer = ui.Label(WIDTH*3, (HEIGHT//4), ui.BLACK, "", 0, 0)
title = ui.Bubble(ui.WHITE, "AWESOME TEXT MESSAGING", 50, ui.CYAN)
startbutton = ui.Button(400, 60, ui.BLACK, "Start Chatting!", 60, ui.CYAN)


clock = pygame.time.Clock()

while True:

    screen.fill(ui.WHITE)
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