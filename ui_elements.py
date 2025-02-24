import pygame

# this is effectively a homemade library where we create classes for ui_elements. this can be imported into the main program to be used.
# the reason we have this in a separate file is to be better organised and promote reusability.
# TLDR we're remaking tkinter from scratch

# label has attributes colour, text and text_colour
class Label():
    def __init__(self, colour, text, text_colour):
        self.colour = colour
        self.text = text
        self.text_colour = text_colour
    
    # method that draws the label to the screen. take parameters: screen to be drawn on, position x, position y
    def draw(self, surface, x, y):
        font = pygame.font.SysFont(None, 40)
        img = font.render(self.text, True, self.text_colour)
        # calculations are made to ensure text is centered and the rectangle fits the text box properly
        pygame.draw.rect(surface, self.colour, (x, y, img.get_width() + 20, img.get_height() + 20))
        surface.blit(img, (x + 10, y + 10))

#Inherited buton from label. Includes a new attribute called function which will run once clicked.
class Button(Label):
    def __init__(self, colour, text, text_colour, function):
        super().__init__(colour, text, text_colour)
        self.function = function
    
    def clicked(self):
        self.function()

# Was about to create a subroutine which would automatically check for click but there is currently no way to access width and height
# feel free to delete or amend if using a different idea
def check_click(x, y, width, height):
    return
    