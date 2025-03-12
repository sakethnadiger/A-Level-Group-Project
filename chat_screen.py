import pygame
import os
import ui_elements as ui
from Network import Network
network = Network()

os.environ['SDL_VIDEO_WINDOW_POS'] = f"{100}, {100}"

def connecting():
    print("connected")
    return True

pygame.init()

pygame.display.set_caption('Chatroom')

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

footer = ui.Label(WIDTH*3, (HEIGHT//4),  ui.BLACK, "", 0, 0)
message_input = ui.InputBox(WIDTH*0.75, 0.5*(HEIGHT//8), ui.WHITE, "", 40, ui.BLUE)
connect_button = ui.Button(400, 60, ui.BLACK, "Connect to server", 60, ui.WHITE)

is_running = True
fullscreen = False
connected = False

clock = pygame.time.Clock()


chat_history = []


while is_running:
    
    #DRAW OBJECTS HERE
    screen.fill(ui.WHITE)
    footer.draw(screen, 0, -1)
    message_input.width = screen.get_width()*0.5
    message_input.draw(screen, 0, ui.pin_y(-1, (HEIGHT//16)))
    connect_button.draw(screen, ui.pin_x(-1, (connect_button.width//2 + 10)), ui.pin_y(1, -(connect_button.height//2 + 10)))
    
    # read pygame_experiment.py for an explanation
    if connected:
        if msg_to_send != ".":
            print("sending", msg_to_send)
            chat_history.append(msg_to_send + "¬0")
        reply = network.send(msg_to_send)
        if reply == None:
            print("Not able to connect. Please check that the server is running, or ask yash for help. ")
            connected = False
        elif reply != ".":
            print("recieved", reply)
            chat_history.append(reply + "¬1")
            
    msg_y = 100
    for msg in chat_history:
        msg, id = msg.split("¬")
        if id == "0":
            replyBubble = ui.Bubble(ui.TURQUOISE, msg, 40, ui.WHITE)
            # Why does this work when the padding  ------------------------v is 100 and replyBubble.width, even though they are identical??
            replyBubble.draw(screen, ui.pin_x(1, 0), ui.pin_y(0, msg_y))
            print(replyBubble.width)
        else:
            replyBubble = ui.Bubble(ui.GREEN, msg, 40, ui.WHITE)
            replyBubble.draw(screen, ui.pin_x(0, -50), ui.pin_y(0, msg_y))
        msg_y -= 45

    msg_to_send = "."
    
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
        message = message_input.get_text(event)
        if connect_button.is_clicked(event, connecting):
            connected = True
            connect_button.reset()
        if message is not None:
            msg_to_send = message
        message_input.update(event)
    
    pygame.display.update()
    clock.tick(60)
