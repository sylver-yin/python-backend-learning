import sys

import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Intialise the game, and create game resources."""
        pygame.init()
        self.clock = (
            pygame.time.Clock()
        )  # NOTE: Makes an instance of "Clock" class so you can work with framerate.
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (
                self.settings.screen_width,
                self.settings.screen_height,
            )
        )  # NOTE: In pygame this is called surface. Elements are displayed there. Every elements have a surface of own.
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond for to keypress and mouse events."""
        for event in pygame.event.get():  # NOTE: This is called event loop. It runs everytime player produces an input considered as event in pygame.
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.backdrop_colour)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == "__main__":
    # NOTE: Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
