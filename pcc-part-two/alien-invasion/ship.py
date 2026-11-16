import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialise the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # NOTE: Load the ship image and get it's rect.
        self.image = pygame.image.load("pcc-part-two/alien-invasion/images/ship.bmp")
        self.rect = self.image.get_rect()

        # NOTE: Movement flags. Start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

        # NOTE: Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # NOTE: Stora a float for the ship's exact horisontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position based on the movement flags."""
        # NOTE: Update the ship's x value, not the rect.
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # NOTE: Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
