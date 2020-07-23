
import pygame


class Ship():
    """Initialize the ship and set its starting position."""
    def __init__(self, screen, settings):

        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('images/ship.bmp')
        #this function returns a surface representing the ship - that's how you lad the image with pygame,
        #bmp (bitmap) is the most comfortable extension beacuse it's pygame's default
        self.rect = self.image.get_rect() #an object - a rectangle from the ship
        self.screen_rect = self.screen.get_rect() #an object - a rectangle from the screen
        #one reason Pygame is so efficient is that it lets you treat game elements like rectangles (rects),
        #even if they’re not exactly shaped like rectangles. Treating an element as a rectangle is efficient because rectangles are simple geometric shapes.
        #This approach usually works well enough that no one playing the game will notice that we’re not working with the exact shape of each game element.

        #we make each new ship start at the bottom center of the screen
        #by aligining the ship's and screen's coordinates with 'centerx' and 'bottom' variables
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #when working with a rect object, you can use the x- and y-coordinates of the top, bottom, left, and right edges of the rectangle, as well as the center.
        #You can set any of these values to determine the current position of the rect.
        #When you’re centering a game element, work with the center, centerx, or centery attributes of a rect. When you’re working at an edge of the screen,
        #work with the top, bottom, left, or right attributes. When you’re adjusting the horizontal or vertical placement of the rect, you can just use the x and
        #y attributes, which are the x- and y-coordinates of its top-left corner. 

        #in Pygame, the origin (0, 0) is at the top-left corner of the screen, and coordinates increase as you go down and to the right. 

        self.moving_right = False #a flag for the ship moving right
        self.moving_left = False #a flag for the ship moving left

        #store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        
    def update(self):
        """Update the ship's position based on movement flags."""
        #update the ship's center value, not the rect.
        if self.moving_right and self.center < self.screen_rect.right: #if moving_right flag is on and if we're not outside the screen
            self.center += self.settings.speed_factor
        if self.moving_left and self.rect.left > 0: #if moving_left flag is on and if we're not outside the screen
            self.center -= self.settings.speed_factor

        #update rect object from self.center (we need it in the blitme())
        self.rect.centerx = self.center


    def blitme(self):
        """draws an image of the ship in its current location"""
        self.screen.blit(self.image, self.rect) #on what draw (what, where)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx








