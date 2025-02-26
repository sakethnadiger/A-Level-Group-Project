import pygame

# this is effectively a homemade library where we create classes for ui_elements. this can be imported into the main program to be used.
# the reason we have this in a separate file is to be better organised and promote reusability.
# TLDR we're remaking tkinter from scratch

# label has attributes colour, text and text_colour



class Label():
    def __init__(self, width, height, colour, text, text_size, text_colour):
        self.width = width
        self.height = height
        self.colour = colour
        self.text = text
        self.text_size = text_size
        self.text_colour = text_colour
        font = pygame.font.SysFont(None, text_size)
        self.img = font.render(self.text, True, self.text_colour)
        # calculations are made to ensure text is centered and the rectangle fits the text box properly
        self.box = pygame.Surface((self.width, self.height))
        self.box.fill(pygame.Color(colour))
    
    # method that draws the label to the screen. take parameters: screen to be drawn on, position x, position y
    #CHANGE - THE CENTRE OF THE ELEMENTS IS NOW WHERE THE THEY WILL BE PLACED, NOT THE TOP LEFT
    def draw(self, surface, x, y):
        surface.blit(self.box, (x - self.width/2, y - self.width/2))
        surface.blit(self.img, (x + (self.width//2) - self.img.get_width()//2, y + (self.height//2) - self.img.get_height()//2))

#Inherited buton from label.
class Button(Label):
    def __init__(self, width, height, colour, text, text_size, text_colour):
        super().__init__(width, height, colour, text, text_size, text_colour)
        self.pressed = False

    # self.hitbox is a rect that contains the clickable area.
    def draw(self, surface, x, y):
        surface.blit(self.box, (x, y))
        surface.blit(self.img, (x + (self.width//2) - self.img.get_width()//2, y + (self.height//2) - self.img.get_height()//2))
        self.hitbox = self.box.get_rect()
        self.hitbox.x, self.hitbox.y = x, y
        

    # checks if the button is clicked. The button can only be clicked once and must be reset with the reset function. the function parameter takes the function that should be ran when clicked/.
    def is_clicked(self, function):
        mousepos = pygame.mouse.get_pos()
        # print(pygame.mouse.get_pos())
        if self.hitbox.collidepoint(mousepos) and pygame.mouse.get_pressed()[0] == 1 and not self.pressed :
            self.pressed = True
            function()
    
    def reset(self):
        self.pressed = False

class TextInput(Label):
    def __init__(self, colour, text_colour, text=""):
        super().__init__(colour, text_colour)
        self.text = text