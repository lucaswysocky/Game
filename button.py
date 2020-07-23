
import pygame.font #allows to print text on the screen

class Button():
    def __init__(self, settings, screen, msg):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (195, 5, 43)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #build the button's rect object and center it.
        #notice that button and its text are two separate things
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #Pygame works with text by rendering the string you want to display as an image. Here, we call prep_msg() to handle this rendering.
        self.prep_msg(msg)


    def prep_msg(self, msg):
        """Turn a text message into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        #turns the text stored in msg into an image, which we then store in msg_image
        #it also takes a Boolean value to turn antialiasing on or off (antialias- ing makes the edges of the text smoother).
        #The remaining arguments are the specified font color and background color
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        #Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        #we call screen.fill() to draw the rectangular portion of the button.
        #Then we call screen.blit() to draw the text image to the screen, passing it an image and the rect object associated with the image



