import pygame
import os
import ui_elements as ui # imoprting classes from ui_elements.py
from Network import Network # importing a class from network.py
network = Network() # creates an instantiation of the network class in network.py in order to send messages to the server
#Helps reset window settings to previous state
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{100}, {100}"

# ui_elements refers to the python file in the same folder. this is basically our own homemade library of classes of ui elements that we have made. see that file for more info.
#BTW I HAVE SHORTENED THE UI LIBRARY NAME TO JUST "UI" - WILL SPEED UP DEVELOPMENT

def Rainbow_Button():
    red.draw(screen, ui.pin_x(-0.9, -21), 0.9)
    orange.draw(screen, ui.pin_x(-0.9, -14), 0.9)
    yellow.draw(screen, ui.pin_x(-0.9, -7), 0.9)
    green.draw(screen, ui.pin_x(-0.9, 0), 0.9)
    blue.draw(screen, ui.pin_x(-0.9, 7), 0.9)
    indigo.draw(screen, ui.pin_x(-0.9, 14), 0.9)
    violet.draw(screen, ui.pin_x(-0.9, 21), 0.9)  
    rainbow_text.draw(screen, ui.pin_x(-0.9,22),ui.pin_y(0.9,-32))



def Colour_Palette(start, pos, speed):
    Red.draw(screen, ui.pin_x(-0.9,120),0.9)
    Orange.draw(screen, ui.pin_x(-0.9,170),0.9)
    Light_Orange.draw(screen, ui.pin_x(-0.9,220),0.9)
    Peach.draw(screen, ui.pin_x(-0.9,270),0.9)
    Yellow.draw(screen, ui.pin_x(-0.9,320),0.9)
    Green.draw(screen, ui.pin_x(-0.9,370),0.9)
    Turquoise.draw(screen, ui.pin_x(-0.9,420),0.9)
    Cyan.draw(screen, ui.pin_x(-0.9,470),0.9)
    Blue.draw(screen, ui.pin_x(-0.9,520),0.9)
    Dark_Grey.draw(screen, ui.pin_x(-0.9,570),0.9)
    Black.draw(screen, ui.pin_x(-0.9,620),0.9)
    White.draw(screen, ui.pin_x(-0.9,670),0.9)
    COLOUR_text.draw(screen, ui.pin_x(-0.9,396), ui.pin_y(0.9,-32))
    pos, speed = ui.animate_x(ui.pin_x(-0.9, start),ui.pin_x(-0.9, 960), pos, speed)
    rect.draw(screen, ui.pin_x(-0.9, pos), 0.9)   
    return start, pos, speed
pygame.init() # creates an object of the pygame class to make our window

pygame.display.set_caption('Chatroom') # sets the caption at the top of the window

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)# --> fullscreen has now been implemented

def clicked_colour():
    return True

def foo():
    print("CLICKED")

def connecting():
    print("connected")
    return True
logo = ui.Label(350, 25, ui.WHITE, "designed by saketh, harvey, yash and luca.", 25, ui.BLACK)
textbox = ui.InputBox(300, 40, ui.LIGHT_ORANGE, "Enter text here...", 40, ui.WHITE)
connect_button = ui.Button(400, 60, ui.BLACK, "Connect to server", 60, ui.WHITE)

colours = ui.Button(48, 50, 0, "", 10 , (ui.WHITE))
rainbow_text = ui.Label(0, 0, ui.YELLOW, "Show colour palette", 14, 0)
COLOUR_text = ui.Label(0, 0, ui.YELLOW, "Red              Orange      Light Orange       Peach             Yellow             Green          Turquoise           Cyan                Blue           Dark Grey           Black             White", 13, 0)
red = ui.Label(8, 50, ui.RED, "", 14, 0)
orange = ui.Label(8, 50, ui.ORANGE, "", 14, 0)
yellow = ui.Label(8, 50, ui.YELLOW, "", 14, 0)
green = ui.Label(8, 50, ui.GREEN, "", 14, 0)
blue = ui.Label(8, 50, ui.BLUE, "", 14, 0)
indigo = ui.Label(8, 50, "#4B369D", "", 14, 0)
violet = ui.Label(7, 50, "#70369d", "", 14, 0)

Red = ui.Label(51, 50, ui.RED, "", 0, 0)
Orange = ui.Label(51, 50, ui.ORANGE, "", 0, 0)
Light_Orange = ui.Label(51, 50, ui.LIGHT_ORANGE, "", 0, 0)
Peach = ui.Label(51, 50, ui.PEACH, "", 0, 0)
Yellow = ui.Label(51, 50, ui.YELLOW, "", 0, 0)
Green = ui.Label(51, 50, ui.GREEN, "", 0, 0)
Turquoise = ui.Label(51, 50, ui.TURQUOISE, "", 0, 0)
Cyan = ui.Label(51, 50, ui.CYAN, "", 0, 0)
Dark_Grey = ui.Label(51, 50, ui.DARK_GREY, "", 0, 0)
Blue = ui.Label(51, 50, ui.BLUE, "", 0, 0)
Black = ui.Label(51, 50, ui.BLACK, "", 0, 0)
White = ui.Label(50, 50, ui.WHITE, "", 0, 0)
rect = ui.Label(590, 80, ui.WHITE, "", 0, 0)

#test bubbles
t = "This is a test sentence which is testing the bubble functionality. This sentence should be split across several lines."
testBubble = ui.Bubble(ui.GREEN, "saketh", 50, ui.WHITE)
multiLineTestBubble = ui.Bubble(ui.GREEN, t, 20, ui.WHITE)

# IN PYGAME YOU ALWAYS USE THIS WHILE LOOP STRUCTURE, THIS IS THE CORE SYSTEM OF PYGAME.
# it is what allows us to constantly check for things like clicks and button presses each frame.

show_palette = False

is_running = True
fullscreen = False
messageReal = False #Testing variable to allow for messages to appear
connected = False

clock = pygame.time.Clock()

messages = []
chat_history = []
while is_running:
  
    # DRAW OBJECTS FIRST
    screen.fill(ui.WHITE)
    textbox.draw(screen, 0, -0.7)
    logo.draw(screen, ui.pin_x(1, -(logo.width//2 + 10)), ui.pin_y(-1, (logo.height//2 + 5)))
    connect_button.draw(screen, 0,0.5)
    # testBubble.draw(screen, 0, 0.5)
    # multiLineTestBubble.draw(screen, 0.5, 0.5)

    colours.draw(screen, -0.9, 0.9)
    Rainbow_Button()
    if show_palette == True:
        start_point, palette_pos, palette_speed = Colour_Palette(start_point, palette_pos, palette_speed)

    # SENDING DATA

    # currently the system works where data is sent in the form of a string. we have to send data every frame, so each frame where there are no new
    # messages, we just send a blank "." . In future, we can make it so that we send objects instead of strings (this will allow us to add names 
    # corresponding to each message), however i just wanted to implement the basic system first.

    # when you send data, the reply is returned back on the same line so you must write "reply = network.send(message)".

    # currently we have it set up so that the current user is ID 0 and every single other user is ID 1. This means that at the moment we can't implement
    # things like names and unique colours for groups of more than 2 people. However, again, im gonna change that in the future when i implement
    # sending objects instead of strings.

    # having this under a boolean if statement ensures we dont send stuff every frame when were not connected and producing a million errors.
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

    # printing the chat history, so that each persons message is on the opposite side and the next message is lower each time
    msg_y = 100
    for msg in chat_history:
        msg, id = msg.split("¬")
        if id == "0":
            replyBubble = ui.Bubble(ui.TURQUOISE, msg, 40, ui.WHITE)
            replyBubble.draw(screen, ui.pin_x(0, 50), ui.pin_y(0, msg_y))
        else:
            replyBubble = ui.Bubble(ui.GREEN, msg, 40, ui.WHITE)
            replyBubble.draw(screen, ui.pin_x(0, -50), ui.pin_y(0, msg_y))
        msg_y -= 45

    msg_to_send = "." # setting the message as blank as default for when there are no new messages each frame.
        
    # EVENT CHECK AFTER DRAWING ALL OBJECTS

    # this basically handles all the events that happen. key presses, mouse position, everything. the variable event contains all of these events. there are a lot you can have a look at a list online.
    for event in pygame.event.get():
        # event.type helps us identify which event it is specifically to target something like a mouse press.
        if event.type == pygame.QUIT:
            # checking if they press the x button on the window and closing if it happens
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    WIDTH = pygame.display.get_window_size()[0]
                    HEIGHT = pygame.display.get_window_size()[1]
                    
                else:
                    #Following two lines help reset window size to previous state also
                    pygame.display.quit()
                    pygame.display.init()
                    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
                    WIDTH = 800
                    HEIGHT = 600
        if colours.is_clicked(event, clicked_colour):
            show_palette = not show_palette
            palette_pos = 390
            palette_speed = 0.1
            start_point = palette_pos
            colours.reset()
        if connect_button.is_clicked(event, connecting):
            connected = True
            connect_button.reset()
        #Check if the enter/return key is pressed. If it is the current value in the textbox is returned and set as a variable
        inp = textbox.get_text(event)
        #Currently the messages which are actually valid are being appended to a 'messages' list which is defined outside the while loop
        #If we are using this system could put the if statement below into the class but if not then do not
        #Also changed the updating of the text box so it does not display unicode of the return key
        if inp is not None:
            messages.append(inp)
            msg_to_send = inp
        textbox.update(event)

    # if len(messages) > 0:
    #     messageBubble = ui.Bubble(ui.BLUE, messages[0], 40, ui.WHITE)
    #     messageReal = True
    #     messages.pop(0)
        
    # if messageReal == True:
    #     messageBubble.draw(screen, ui.pin_x(-1, messageBubble.width // 2 + 20), ui.pin_y(-1, messageBubble.height // 2 + 20))

    # DON'T DRAW ANYTHING HERE IM LOOKING AT YOU HARVEY
    
    
    pygame.display.update()

