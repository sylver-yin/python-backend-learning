class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.backdrop_colour = (0, 100, 200)  # Set the background colour in RGB.

        self.ship_speed = 1.5
