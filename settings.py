class Settings:
    def __init__(self):
        """Inicjalizacja ustawień gry"""
        # Ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 255)

        self.lives_limit = 3

        self.speedup_scale = 1.1
        self.increase_scale = 1.2
        self.dispersion_reduce = 50

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicjalizacja ustawień dynamicznych, które zmieniają się w trakcie gry"""

        self.drop_speed = 1
        self.number_of_letters = 20
        self.letter_dispersion = -1000

    def increase_difficulty(self):
        """Zmiana ustawień dotyczących trudności"""
        self.drop_speed *= self.speedup_scale
        self.number_of_letters = int(self.number_of_letters * self.increase_scale)
        self.letter_dispersion = min(int(self.letter_dispersion + self.dispersion_reduce), 0)