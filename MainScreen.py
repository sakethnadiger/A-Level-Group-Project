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

# def settingsmenu():
    # print("Time to change settings")
    # return True

# def settingscolourchange():
    # print("Changing colour to red")
    # return True

def quitchatting():
    print("Quitting")
    return True

# Main Section
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
footer = ui.Label(WIDTH*3, (HEIGHT//4), ui.BLACK, "", 0, 0)
title = ui.Bubble(ui.WHITE, "AWESOME TEXT MESSAGING", 50, ui.CYAN)
startbutton = ui.Button(400, 60, ui.BLACK, "Start Chatting!", 60, ui.CYAN)
optionsbutton = ui.Button(400, 60, ui.BLACK, "Options", 60, ui.CYAN)
quitbutton = ui.Button(400, 60, ui.BLACK, "Quit", 60, ui.CYAN)

# Settings Section
settingstitle = ui.Bubble(ui.WHITE, "AWESOME SETTINGS MENU", 60, ui.CYAN)
settingscolour = ui.Button(400, 60, ui.BLACK, "Change Colour", 60, ui.CYAN)


settings = False
clock = pygame.time.Clock()

while True:

    screen.fill(ui.WHITE)
    footer.draw(screen, 0, -1)
    

    title.draw(screen, 0, ui.pin_y(1, -30))
    startbutton.draw(screen, 0, ui.pin_y(0.5, -10))
    optionsbutton.draw(screen, 0, ui.pin_y(0.5, -100))
    quitbutton.draw(screen, 0, ui.pin_y(0.5, -200))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if startbutton.is_clicked(event, startchatting):
        chatting = True
        import chat_screen
        startbutton.reset()
        pygame.quit()
    
    # if optionsbutton.is_clicked(event, settingsmenu):
        # settings = True
        # optionsbutton.reset()
    
    if quitbutton.is_clicked(event, quitchatting):
        pygame.quit()

    # if settingscolour.is_clicked(event, settingscolourchange):
        # bgcolour = RED

    pygame.display.update()
    clock.tick(60)