import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Initialize the alien and set its starting position."""
    def __init__(self, screen, settings):

        super().__init__()
        self.screen = screen
        self.settings = settings

        #load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen.
        #adding a space to the left of it that’s equal to the alien’s width and a space above it equal to its height
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact position.
        self.x = float(self.rect.x)


    def blitme(self):
        """draws an image in its current location"""
        self.screen.blit(self.image, self.rect)


    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x






