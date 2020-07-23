
import pygame.font 
import json
from ship_left import Ship_left
from pygame.sprite import Group

class Scoreboard():
    """A class to report scoring information."""
    def __init__(self, settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.settigns = settings
        self.stats = stats
        self.screen_rect = screen.get_rect()

        #font settings for scoring information.
        self.txt_color = (192, 163, 163)
        self.font = pygame.font.SysFont(None, 30)

        #prepare the initial score image.
        self.prep_score() 
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_score(self):
        """Turn the score into a rendered image."""
        #the round() function normally rounds a decimal number to a set number of decimal places given as the second argument. However, if you pass
        #a negative number as the second argument, round() will round the value to the nearest 10, 100, 1000, and so on.
        rounded_score = int(round(self.stats.score, -1)) #this line tells Python to round the value of stats.score to the nearest 10 and store it in rounded_score
        txt_string = "{:,}".format(rounded_score) #this string formatting directive tells Python to insert commas into numbers when converting a numerical value to a string - for example, to output 1,000,000 instead of 1000000. 
        txt_string = str("Your score: " + str(txt_string))

        self.txt_image = self.font.render(txt_string, True, self.txt_color) #nothing for background so it is transparent

        #display the score at the top right of the screen.
        self.txt_rect = self.txt_image.get_rect()
        self.txt_rect.right = self.screen_rect.right - 20
        self.txt_rect.top = 20 #top of the score image 20 pixels from the screen's top


    def prep_high_score(self):
        """Turn the score into a rendered image."""
        high_score_file = "high_score.json"
        with open(high_score_file) as j_object: #we open json file where we store the highest score
            high_score = json.load(j_object)
        rounded_score_high = int(round(high_score, -1)) 
        txt_string_high = "{:,}".format(rounded_score_high)
        txt_string_high = str("Highest score: " + str(txt_string_high))

        self.txt_image_high = self.font.render(txt_string_high, True, self.txt_color) #nothing for background so it is transparent

        #display the score at the top right of the screen.
        self.txt_rect_high = self.txt_image_high.get_rect()
        self.txt_rect_high.centerx = self.screen_rect.centerx
        self.txt_rect_high.top = self.txt_rect.top 


    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render("Level: " + str(self.stats.level), True,
                self.txt_color)
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.txt_rect.right
        self.level_rect.top = self.txt_rect.bottom + 10


    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship_left(self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def show_score(self):
        """Draw scores and ships to the screen."""
        self.screen.blit(self.txt_image, self.txt_rect)
        self.screen.blit(self.txt_image_high, self.txt_rect_high)
        self.screen.blit(self.level_image, self.level_rect)
        #draw ships.
        self.ships.draw(self.screen)





