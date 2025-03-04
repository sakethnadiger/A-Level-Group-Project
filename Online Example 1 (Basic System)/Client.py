# in a server-client network, the client is the thing that processes and sends requests to other clients. This is basically like a "user" or "person"
# on the network.

# this includes the basic code that is the game.

# in this example, we don't actually do anything with this code, this is just an example of how the main game code would look like.

import pygame
from Network import Network # we import from the python file we made called network.py, like how we import from ui_elements. This has a class we can use to send messages to and from the server.

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(win,player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network() # creates an instantiation of the network class created in network.py to be able to send/recieve messages to and from the server.
    startPos = read_pos(n.getPos())
    p = Player(startPos[0],startPos[1],100,100,(0,255,0))
    p2 = Player(0,0,100,100,(255,0,0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))  # in this example we have set the server up so that it recieves the player 1 position and returns the player 2 positon and vice versa
        # this example constantly sends the position info of the players even if they dont update because its better to constantly check for a game.
        # we probably wont do this exact thing in our chatroom because its inefficient and makes it more difficult to know if a message coming in is a new message.
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p, p2)

main()