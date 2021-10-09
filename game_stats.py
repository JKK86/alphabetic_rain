class GameStats:
    """Monitorowanie danych statystycznych w grze"""

    def __init__(self, ai_game):
        """Inicjalizacja danych statystycznych"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Inicjalizacja danych statystycznych zmieniających się w czasie gry"""
        self.lives_left = self.settings.lives_limit
