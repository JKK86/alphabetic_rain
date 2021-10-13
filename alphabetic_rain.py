import sys
from time import sleep

import pygame

from button import Button
from game_stats import GameStats
from letter import Letter
from scoreboard import Scoreboard
from settings import Settings


class AlphabeticRain:
    """Ogólna klasa do zarządzania sposobem działania gry"""

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alphabetical Rain")

        self.stats = GameStats(self)

        self.scoreboard = Scoreboard(self)

        self.letters = pygame.sprite.Group()

        self._create_rain()

        self.play_button = Button(self, "Start")

    def run_game(self):
        """Rozpoczęcie pętli głównej gry"""

        while True:
            self._check_events()

            if self.stats.game_active:
                self._update_letters()

            self._update_screen()

    def _create_rain(self):
        for i in range(self.settings.number_of_letters):
            letter = Letter(self)
            self.letters.add(letter)

    def _check_events(self):
        """Reakcje na zdarzenia generowane przez użytkownika"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_s and not self.stats.game_active:
            self._start_game()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        else:
            for letter in self.letters.sprites():
                # print(pygame.key.name(event.key))
                # print(letter.letter)
                if pygame.key.name(event.key) == letter.letter:
                    self.letters.remove(letter)
                    self.stats.score += self.settings.letter_points
                    self.scoreboard.prep_score()
                    self.scoreboard.check_high_score()
                    break

    def _check_play_button(self, mouse_pos):
        """Rozpoczęcie nowej gry po kliknięciu przez użytkownika przycisku Start"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _start_game(self):
        # Wyzerowanie ustawień dotyczących gry
        self.stats.reset_stats()
        self.settings.initialize_dynamic_settings()
        self.stats.game_active = True
        self.scoreboard.prep_score()
        self.scoreboard.prep_level()
        self.scoreboard.prep_lives()

        self.letters.empty()
        self._create_rain()

        pygame.mouse.set_visible(False)

    def _check_letters_bottom(self):
        """Sprawdzenie czy któraś z opadających liter dotarła do dolnej krawędzi ekranu"""
        screen_rect = self.screen.get_rect()
        for letter in self.letters.sprites():
            if letter.letter_rect.bottom >= screen_rect.bottom:
                self._lose_life()
                break

    def _lose_life(self):
        if self.stats.lives_left >= 0:
            self.stats.lives_left -= 1
            self.scoreboard.prep_lives()
            self.letters.empty()
            self._create_rain()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_letters(self):
        """Uaktualnienie położenia wszystkich spadających liter"""
        self.letters.update()
        if not self.letters:
            self._create_rain()
            self.settings.increase_difficulty()
            self.stats.level += 1
            self.scoreboard.prep_level()
        self._check_letters_bottom()

    def _update_screen(self):
        """Uaktualnianie obrazów na ekranie"""
        self.screen.fill(self.settings.bg_color)

        for letter in self.letters.sprites():
            letter.show_letter()

        self.scoreboard.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()
        self.clock.tick(60)


if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie
    ar = AlphabeticRain()
    ar.run_game()
