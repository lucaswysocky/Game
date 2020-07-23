
import pygame
from pygame.sprite import Sprite


class Ship_left(Sprite):
    """Initialize the ship and set its starting position."""
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load('images/ship_left.bmp')
        self.rect = self.image.get_rect() 
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
