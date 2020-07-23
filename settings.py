
class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings"""

        # Screen settings
        self.screen_width = 1250
        self.screen_height = 650
        self.bg_color = (0, 0, 0)

        self.ship_limit = 3

        #bullet settings
        self.bullet_height = 3
        self.bullet_width = 15
        self.bullet_color = 255, 7, 7
        self.bullets_allowed = 5

        #aliens's settings
        self.fleet_drop_speed = 10

        #how quickly the game speeds up
        self.speedup_scale = 1.5

        #how many points to award with each new level
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):

        self.speed_factor = 25
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 10

        self.fleet_direction = 1

        #scoring
        self.alien_points = 10


    def increase_speed(self):

        self.speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale) 

