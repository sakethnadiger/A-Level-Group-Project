import pygame
import os
import ui_elements as ui
from Network import Network
network = Network()

os.environ['SDL_VIDEO_WINDOW_POS'] = f"{100}, {100}"

def connecting():
    print("connected")
    return True

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

footer = ui.Label(WIDTH*3, (HEIGHT//4),  BLACK, "", 0, 0)
message_input = ui.InputBox(WIDTH*0.75, 0.5*(HEIGHT//8), WHITE, "", 40, BLUE)
connect_button = ui.Button(400, 60, BLACK, "Connect to server", 60, WHITE)

is_running = True
fullscreen = False
connected = False

clock = pygame.time.Clock()


chat_history = []


while is_running:
    
    #DRAW OBJECTS HERE
    screen.fill(WHITE)
    footer.draw(screen, 0, -1)
    message_input.width = screen.get_width()*0.5
    message_input.draw(screen, 0, ui.pin_y(-1, (HEIGHT//16)))
    connect_button.draw(screen, ui.pin_x(-1, (connect_button.width//2 + 10)), ui.pin_y(1, -(connect_button.height//2 + 10)))
    
    if connected:
        # the way the server system is set up is that we have to send something every frame. we just send a full stop as a "null" message in order to
        # say that nothing is being sent on this frame.
        if msg_to_send != ".":
            print("sending", msg_to_send)
            # "chat history" is a list stored on the clients device that contains the chat history so we can draw it each frame.
            chat_history.append(msg_to_send + "¬0") # attatching a userID to each message so we know which ones were sent by who. I used an arbitrary character "¬" bc no ones gonna type that
        # THIS IS THE LINE. this is how you send something on a network. every time you send a message the reply is returned, so you have to put "reply ="
        reply = network.send(msg_to_send) # to repeat the way the system works is you send the message and that will always return the reply, so you must store it in a variable.
        if reply == None:
            print("Not able to connect. Please check that the server is running, or ask yash for help. ")
            connected = False
        # again checking that the reply is not null and that its an actual message we want to add to the history
        elif reply != ".":
            print("recieved", reply)
            chat_history.append(reply + "¬1")
            
    msg_y = 100
    for msg in chat_history:
        msg, id = msg.split("¬")
        if id == "0":
            replyBubble = ui.Bubble(TURQUOISE, msg, 40, WHITE)
            replyBubble.draw(screen, ui.pin_x(1, -(replyBubble.width//2 + 100)), ui.pin_y(0, msg_y))
        else:
            replyBubble = ui.Bubble(GREEN, msg, 40, WHITE)
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
