
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self, settings, screen, ship):
        super().__init__() #bullet class is a subclass of Sprite superclass
        self.settings = settings
        self.screen = screen
        self.rect = pygame.Rect(0,0, settings.bullet_height, settings.bullet_width)
        #create a rectangle from scratch using x and y coordinates and dimensions
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #we align where the bullets will appear with where the ship currently is

        self.y = float(self.rect.y)
        #we store a decimal value for the bullet’s y-coordinate so we can make fine adjustments to the bullet’s speed

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        self.y -= self.speed_factor #move the y-coordinate of the bulet
        self.rect.y = self.y #update the rect position

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
        #we use 'draw' to show a sprite on a creen
        #notice that it requires different attributes than blitme, which was a method on a screen








