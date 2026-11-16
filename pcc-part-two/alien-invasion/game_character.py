import pygame


class UncleChubby:
    """A simple class that represents the game character. 12-2 Homework."""

    def __init__(self, ai_game):
        """Initialise the character."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("pcc-part-two/alien-invasion/images/scary.bmp")
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
