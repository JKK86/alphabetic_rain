import sys

import pygame

from letter import Letter
from settings import Settings


class AlphabeticRain:
    """Ogólna klasa do zarządzania sposobem działania gry"""

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alphabetical Rain")

        self.letters = pygame.sprite.Group()

        self._create_rain()

    def run_game(self):
        """Rozpoczęcie pętli głównej gry"""

        while True:
            self._check_events()
            self._update_letters()
            self._update_screen()

    def _create_rain(self):
        for i in range(10):
            letter = Letter(self)
            self.letters.add(letter)

    def _check_events(self):
        """Reakcje na zdarzenia generowane przez użytkownika"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        for letter in self.letters.sprites():
            # print(pygame.key.name(event.key))
            # print(letter.letter)
            if pygame.key.name(event.key) == letter.letter:
                self.letters.remove(letter)
                break

    def _update_letters(self):
        """Uaktualnienie położenia wszystkich spadających liter"""
        self.letters.update()

    def _update_screen(self):
        """Uaktualnianie obrazów na ekranie"""
        self.screen.fill(self.settings.bg_color)

        for letter in self.letters.sprites():
            letter.show_letter()

        pygame.display.flip()
        self.clock.tick(60)



if __name__ == '__main__':
    # Utworzenie egemplarza gry i jej uruchomienie
    ar = AlphabeticRain()
    ar.run_game()
