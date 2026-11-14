import sys

import pygame

from settings import Settings


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
            self.settings.screen_width,
            self.settings.screen_height,
            self.settings.backdrop_colour,
        )  # NOTE: In pygame this is called surface. Elements are displayed there. Every elements have a surface of own.
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # NOTE: Watch for keyboard and mouse events.
            for event in pygame.event.get():  # NOTE: This is called event loop. It runs everytime player produces an input considered as event in pygame.
                if event.type == pygame.QUIT:
                    sys.exit()

            # NOTE: Redraws the screen during each pass through the loop.
            self.screen.fill(self.backdrop_colour)

            # NOTE: Make the most recently drawn screen visible, meaning, refreshing it seamlessly for the user.
            pygame.display.flip()
            self.clock.tick(
                60
            )  # NOTE: Set tickspeed for 60, meaning - every second 60 ticks happens.


if __name__ == "__main__":
    # NOTE: Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
