import pygame.font


class Scoreboard:
    """Klasa przeznaczona do przedstawianie informacji o punktacji"""

    def __init__(self, ai_game):
        """Inicjalizacja atrybutów dotyczących punktacji"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Ustawienia czcionki dla informacji dotyczącej punktacji
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 50)

        # Przygotowanie początkowch obrazów z punktacją
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lives()

    def prep_score(self):
        """Przekształcenie punktacji na wygenerowany obraz"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"Score: {rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Wyświetlanie punktacji w prawym górnym rogu ekranu
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Przekształcenie najlepszego wyniku w grze na wygenerowany obraz"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"High score: {high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Wyświetlanie najlepszego wyniku na środku, przy górnej krawędzi ekranu
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Przekształcenie aktualnego poziomy na wygenerowany obraz"""
        level = str(self.stats.level)
        level_str = f"Level: {level}"
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Wyświetlanie aktualnego poziomu poniżej punktacji
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_lives(self):
        """Wyświetla liczbę żyć jakie pozostały graczowi"""
        lives = str(self.stats.lives_left)
        lives_str = f"Lives: {lives}"
        self.lives_image = self.font.render(lives_str, True, self.text_color, self.settings.bg_color)

        # Wyświetlanie aktualnego poziomu w lewym górnym rogu ekranu
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.left = self.screen_rect.left + 20
        self.lives_rect.top = 20

    def show_score(self):
        """Wyświetlanie punktacji, liczby statków i aktualnego poziomu na ekranie"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.lives_image, self.lives_rect)

    def check_high_score(self):
        """Sprawdzenie czy pobity został najlepszy dotąd wynik"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
