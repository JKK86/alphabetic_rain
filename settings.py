class Settings:
    def __init__(self):
        """Inicjalizacja ustawień gry"""
        # Ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 255)

        self.drop_speed = 1

        self.lives_limit = 3