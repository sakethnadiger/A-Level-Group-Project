import pygame
from textwrap import wrap

# this is effectively a homemade library where we create classes for ui_elements. this can be imported into the main program to be used.
# the reason we have this in a separate file is to be better organised and promote reusability.
# TLDR we're remaking tkinter from scratch

# label has attributes colour, text and text_colour

#added all the colours into here to use for the main files
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
#NOW USING A COORDINATE SYSTEM WITH 0,0 AT THE CENTRE OF SCREEN AND INPUT COORDINATES RELATIVE TO CENTRE. E.G. 0.5 IS HALFWAY UP TO THE TOP
#INPUT WILL BE A NUMBER x OR y, WITH |x| < 1 AND |y| < 1
def convert_coords(input_x, input_y):
    width, height = pygame.display.get_window_size()
    screen_centre_x = width / 2
    screen_centre_y = height / 2
    true_x = int(screen_centre_x * (1 + input_x))
    true_y = int(screen_centre_y * (1 - input_y))
    return true_x, true_y

def convert_coords_back(true_x, true_y):
    width, height = pygame.display.get_window_size()
    screen_centre_x = width / 2
    screen_centre_y = height / 2
    input_x = (true_x / int(screen_centre_x)) -1
    input_y = (true_y / int(screen_centre_y) -1)*(-1)
    return input_x, input_y

def pin_x(x_Saketh_coord, x_pixel_offset):
    width = pygame.display.get_window_size()[0]
    screen_centre_x = width // 2
    x_coord = int(screen_centre_x * (1 + x_Saketh_coord))
    new_x_coord = x_coord + x_pixel_offset
    new_x_Saketh_coord = (new_x_coord / int(screen_centre_x)) -1
    return new_x_Saketh_coord

def pin_y(y_Saketh_coord, y_pixel_offset):
    height = pygame.display.get_window_size()[1]
    screen_centre_y = height // 2
    y_coord = int(screen_centre_y * (1 - y_Saketh_coord))
    new_y_coord = y_coord - y_pixel_offset
    new_y_Saketh_coord = (new_y_coord / int(screen_centre_y) -1)*(-1)
    return new_y_Saketh_coord

def animate_x(start, end, pos, speed,):
    #turns the given coordinate into its true coordinate value
    start = int(pygame.display.get_window_size()[0] //2 * (1 + start))
    end = int(pygame.display.get_window_size()[0] //2 * (1 + end))
    #gets the true value of pos when it is pinned to -0.9
    pinned_pos = int(pygame.display.get_window_size()[0] //2 * (1 + pin_x(-0.9, pos)))
    #makes the rectangle speed up until half way and then slowes it down until back to speed = 0.1
    if pinned_pos <= (start + (end - start)/2):
        pos += speed
        speed += 0.2
    elif speed > 0.2:
        pos += speed
        speed -= 0.2
    return pos, speed

def animate_y(start, end, pos, speed,):
    #turns the given coordinate into its true coordinate value
    start = int(pygame.display.get_window_size()[1] //2 * (1 + start))
    end = int(pygame.display.get_wndow_size()[1] //2 * (1 + end))
    #gets the true value of pos when it is pinned to -0.9
    pinned_pos = int(pygame.display.get_window_size()[1] //2 * (1 + pin_y(0.6, pos)))#change 0.6 to the coord you want to pin too.
    #makes the rectangle speed up until half way and then slowes it down until back to speed = 0.1
    if pinned_pos <= (start + (end - start)/2):
        pos += speed
        speed += 0.2
    elif speed > 0.2:
        pos += speed
        speed -= 0.2
    return pos, speed
#Separates a line of text into multiple lines with a set character limit which has not been fixed yet
def multi_line_separator(text, char_limit):
    if len(text) <= char_limit:
        return [text]
    words = text.split()
    lines = []
    result = ""

    for iter, i in enumerate(words):
        if len(result + " " + i) <= char_limit:
            if iter == 0:
                result += i
            else:
                result += " " + i
        else:
            remainder = char_limit - len(result)
            result += remainder * " "
            lines.append(result)
            result = i
            
    remainder = char_limit - len(result)
    result += remainder * " "
    lines.append(result)
    return lines



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
        
class Bubble:
    def __init__(self, colour, text, text_size, text_colour):
        self.colour = colour
        self.text = text
        self.text_size = text_size
        self.text_colour = text_colour
        self.width = 0
        self.height = 0
        font = pygame.font.SysFont(None, text_size)
        lines = multi_line_separator(self.text, 40)
        self.line_objects = []
        for line in lines:
            self.line_objects.append(font.render(line, True, self.text_colour))
        
    def draw(self, surface, x, y):
        height_multiplier = len(self.line_objects)#The length of the number of lines is the length of the line_objects list, which is the number the height is multiplied by
        #add 5% of the width and height of the fonts on to the rectangle to act as padding
        self.width = int(self.line_objects[0].get_width() * 1.05)
        self.height = int(self.line_objects[0].get_height() * height_multiplier * 1.05)
        new_x = convert_coords(x, y)[0]
        new_y = convert_coords(x, y)[1]
        centred_x = new_x - self.width//2
        centred_y = new_y - self.height//2
        bubble_rect = pygame.Rect(centred_x, centred_y, self.width, self.height)
        pygame.draw.rect(surface, self.colour, bubble_rect, 0, min(self.width, self.height)//2)

        for iter, object in enumerate(self.line_objects):
            surface.blit(object, (centred_x + (self.width//2) - self.line_objects[0].get_width()//2, centred_y + ((self.height//(2*height_multiplier)) + (iter*self.line_objects[0].get_height()) - self.line_objects[0].get_height()//2)))
        
        
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
                return function()
    
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
        font = pygame.font.SysFont(None, self.text_size)
        self.img = font.render(self.text, True, self.text_colour)
        if self.img.get_width() > self.width - 20:
            self.box = pygame.Surface((self.img.get_width() + 20, self.height))
        else:
            self.box = pygame.Surface((self.width, self.height))
        new_x, new_y = convert_coords(x, y)
        centred_x = new_x - self.box.get_width()//2
        centred_y = new_y - self.height//2
        self.box.fill(pygame.Color(self.colour))
        surface.blit(self.box, (centred_x, centred_y))
        surface.blit(self.img, (centred_x + (self.box.get_width()//2) - self.img.get_width()//2, centred_y + (self.height//2) - self.img.get_height()//2))
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
                if event.key != pygame.K_RETURN:
                    self.text += event.unicode
    
    def get_text(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return self.text
            

# draw(animate_x(any_var, var1, var2)[0], animate_x(any_var, var1, var2)[1])

###     return var1, var2