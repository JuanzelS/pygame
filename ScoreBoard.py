import pygame  # Ensure pygame is imported

class ScoreBoard:
    def __init__(self, x, y, score):
        self.x = x
        self.y = y
        self.score = score
        self.font = pygame.font.Font(None, 36)  # Use pygame.font to create font

    def render(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))  # White color
        screen.blit(score_text, (self.x, self.y))

    def update(self, points):
        self.score += points
