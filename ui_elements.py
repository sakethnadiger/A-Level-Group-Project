import pygame

# this is effectively a homemade library where we create classes for ui_elements. this can be imported into the main program to be used.
# the reason we have this in a separate file is to be better organised and promote reusability.
# TLDR we're remaking tkinter from scratch

# label has attributes colour, text and text_colour



#NOW USING A COORDINATE SYSTEM WITH 0,0 AT THE CENTRE OF SCREEN AND INPUT COORDINATES RELATIVE TO CENTRE. E.G. 0.5 IS HALFWAY UP TO THE TOP
#INPUT WILL BE A NUMBER x OR y, WITH |x| < 1 AND |y| < 1
def convert_coords(input_x, input_y):
    width, height = pygame.display.get_window_size()
    screen_centre_x = width // 2
    screen_centre_y = height // 2
    true_x = int(screen_centre_x * (1 + input_x))
    true_y = int(screen_centre_y * (1 - input_y))
    return true_x, true_y

def convert_coords_back(true_x, true_y):
    width, height = pygame.display.get_window_size()
    screen_centre_x = width // 2
    screen_centre_y = height // 2
    input_x = (true_x / int(screen_centre_x)) -1
    input_y = (true_y / int(screen_centre_y) -1)*(-1)
    return input_x, input_y


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
        new_x = convert_coords(x, y)[0]
        new_y = convert_coords(x, y)[1]
        centred_x = new_x - self.width//2
        centred_y = new_y - self.height//2
        surface.blit(self.box, (centred_x, centred_y))
        surface.blit(self.img, (centred_x + (self.width//2) - self.img.get_width()//2, centred_y + (self.height//2) - self.img.get_height()//2))

#Inherited buton from label.
class Button(Label):
    def __init__(self, width, height, colour, text, text_size, text_colour):
        super().__init__(width, height, colour, text, text_size, text_colour)
        self.pressed = False

    # self.hitbox is a rect that contains the clickable area.
    def draw(self, surface, x, y):
        new_x, new_y = convert_coords(x, y)
        centred_x = new_x - self.width//2
        centred_y = new_y - self.height//2
        surface.blit(self.box, (centred_x, centred_y))
        surface.blit(self.img, (centred_x + (self.width//2) - self.img.get_width()//2, centred_y + (self.height//2) - self.img.get_height()//2))
        self.hitbox = self.box.get_rect()
        self.hitbox.x, self.hitbox.y = centred_x, centred_y
        

    # checks if the button is clicked. The button can only be clicked once and must be reset with the reset function. the function parameter takes the function that should be ran when clicked/.
    def is_clicked(self, event, function):
        mousepos = pygame.mouse.get_pos()
        if self.hitbox.collidepoint(mousepos) and not self.pressed:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.pressed = True
                function()
    
    def reset(self):
        self.pressed = False

class InputBox(Label):
    def __init__(self, width, height, colour, default_text, text_size, text_colour):
        super().__init__(width, height, colour, default_text, text_size, text_colour)
        self.pressed = False
        self.default = True
        # saving the default text
        self.default_text = self.text

    def draw(self, surface, x, y):
        new_x, new_y = convert_coords(x, y)
        centred_x = new_x - self.width//2
        centred_y = new_y - self.height//2
        surface.blit(self.box, (centred_x, centred_y))
        font = pygame.font.SysFont(None, self.text_size)
        self.img = font.render(self.text, True, self.text_colour)
        surface.blit(self.img, (centred_x + (self.width//2) - self.img.get_width()//2, centred_y + (self.height//2) - self.img.get_height()//2))
        self.hitbox = self.box.get_rect()
        self.hitbox.x, self.hitbox.y = centred_x, centred_y
    
    def update(self, event):
        mousepos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.default:
                self.text = ""
                self.default = False
            if self.hitbox.collidepoint(mousepos) and not self.pressed:
                self.pressed = True
            else:
                if not self.default and self.text == "":
                    self.default = True
                    self.text = self.default_text
                self.pressed = False
        if event.type == pygame.KEYDOWN and self.pressed:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1] 
            else: 
                self.text += event.unicode
        