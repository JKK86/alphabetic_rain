import random
import string

import pygame.font
from pygame.sprite import Sprite


class Letter(Sprite):
    def __init__(self, ar_game):
        """Inicjalizacja liter i ich położenia początkowego"""
        super().__init__()
        self.screen = ar_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ar_game.settings

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 50)

        self.letter = random.choice(string.ascii_letters.lower() + string.digits)

        self.prepare_letter()

    def prepare_letter(self):
        self.letter_image = self.font.render(self.letter, True, self.text_color, self.settings.bg_color)
        self.letter_rect = self.letter_image.get_rect()
        self.letter_rect.x = random.randint(0, self.settings.screen_width)
        self.letter_rect.top = self.screen_rect.top

    def show_letter(self):
        self.screen.blit(self.letter_image, self.letter_rect)

    def update(self):
        self.letter_rect.y += self.settings.drop_speed
