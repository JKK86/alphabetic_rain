import sys

import pygame

from settings import Settings


class AlphabeticRain:
    """Ogólna klasa do zarządzania sposobem działania gry"""

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alphabetical Rain")

    def run_game(self):
        """Rozpoczęcie pętli głównej gry"""

        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Reakcje na zdarzenia generowane przez użytkownika"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    def _update_screen(self):
        """Uaktualnianie obrazów na ekranie"""
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()


if __name__ == '__main__':
    # Utworzenie egemplarza gry i jej uruchomienie
    ar = AlphabeticRain()
    ar.run_game()
