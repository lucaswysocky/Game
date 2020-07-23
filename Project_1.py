
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
#a Group behaves like a list with some extra functionality that’s helpful when building games
#in our case, it is going to be a list of objects, where each object is an instance of a class
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    #initialize game and create a screen object.

    settings = Settings() #initialize settings

    pygame.init() #initializes background settings that Pygame needs to work properly
    screen = pygame.display.set_mode(( settings.screen_width, settings.screen_height))
    #create a display window called screen, on which we’ll draw all of the game’s graphical elements.
    #The argument is a tuple that defines the dimensions of the game window
    #the screen object is called a surface. A surface in Pygame is a part of the screen where you display a game element.
    #Each element in the game, like the aliens or the ship, is a surface. The surface returned by display.set_mode() represents
    #the entire game window. When we activate the game’s animation loop, this surface is automatically redrawn on every pass through the loop.
    pygame.display.set_caption("Alien Invasion")

    #create an instance to store game statistics.
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)

    ship = Ship(screen, settings) #make a ship.
    bullets = Group() #make a group to store bullets in
    aliens = Group() #make a group for aliens

    #create the fleet of aliens.
    gf.create_fleet(settings, screen, ship, aliens)

    #make a play button
    play_button = Button(settings, screen, 'Play')

    while True:
        #start the main loop for the game.
        gf.check_events(settings, screen, ship, bullets, stats, play_button, aliens, sb)

        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, ship, aliens, bullets, stats, sb)
            gf.update_aliens(settings, stats, screen, ship, aliens, bullets, sb)
        
        gf.update_screen(settings, screen, stats, ship, aliens, bullets, play_button, sb)


run_game()